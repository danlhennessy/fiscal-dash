from src import database, rest_api
from src.vault_actions import FISCAL_VAULT
from flask import Flask, render_template, session, request, redirect, url_for
from flask_session import Session
import requests
import matplotlib.pyplot as plt
import msal
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.trace import get_tracer_provider, set_tracer_provider
import plotly.graph_objects as go
import io
import base64
from werkzeug.middleware.proxy_fix import ProxyFix

fiscal_dict = FISCAL_VAULT.dict_all('secret')

app = Flask(__name__)
app.config.from_mapping(fiscal_dict)
Session(app)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)


@app.route("/")
def index():
    if not session.get("user"):
        return redirect(url_for("login"))
    return render_template(
        'index.html',
        user=session["user"],
        version=msal.__version__
        )


@app.route("/login")
def login():
    session["flow"] = _build_auth_code_flow(scopes=fiscal_dict['SCOPE'])
    return render_template(
        "login.html",
        auth_url=session["flow"]["auth_uri"],
        version=msal.__version__
        )


@app.route(fiscal_dict['REDIRECT_PATH'])
def authorized():
    try:
        cache = _load_cache()
        result = _build_msal_app(cache=cache).acquire_token_by_auth_code_flow(
            session.get("flow", {}), request.args)
        if "error" in result:
            return render_template("auth_error.html", result=result)
        session["user"] = result.get("id_token_claims")
        _save_cache(cache)
    except ValueError:
        pass
    return redirect(url_for("index"))


@app.route("/logout")
def logout():
    session.clear()  # Wipe out user and its token cache from session
    return redirect(  # Also logout from your tenant's web session
        fiscal_dict['AUTHORITY'] + "/oauth2/v2.0/logout" +
        "?post_logout_redirect_uri=" + url_for("index", _external=True))


@app.route("/graphcall")
def graphcall():
    token, accounts = _get_token_from_cache(fiscal_dict['SCOPE'])
    if not token:
        return redirect(url_for("login"))
    graph_data = requests.get(  # Use token to call downstream service
        fiscal_dict['ENDPOINT'],
        headers={'Authorization': 'Bearer ' + token['access_token']},
        ).json()
    return render_template(
        'display.html',
        result=graph_data,
        accounts=accounts
        )


@app.route("/dashboard")
def dashboard():
    token, accounts = _get_token_from_cache(fiscal_dict['SCOPE'])
    if not token:
        return redirect(url_for("login"))
    user = (accounts[0]['username'])
    labels = ['Category A', 'Category B', 'Category C']
    values = [30, 50, 20]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.set_title('Sample Pie Chart')

    chart_bytes = io.BytesIO()
    plt.savefig(chart_bytes, format='png')
    plt.close()
    chart_base64 = base64.b64encode(chart_bytes.getvalue()).decode('utf-8')

    return render_template(
        'dashboard.html',
        chart_base64=chart_base64,
        user=user
        )


@app.route('/update_piechart', methods=['POST'])
def update_piechart():
    user = request.form.get('user')
    category = request.form.get('category')
    value = int(request.form.get('value'))

    database.update_database(
        table="pie_data",
        keys=["user", "category", "value"],
        values=[user, category, value],
        connection=database.FISCALDB
        )

    return redirect('/plotly')


@app.route("/plotly")
def plotly():
    token, accounts = _get_token_from_cache(fiscal_dict['SCOPE'])
    if not token:
        return redirect(url_for("login"))

    result = database.retrieve_database(
        table="pie_data",
        keys=["id", "user", "category", "value"],
        connection=database.FISCALDB
        )

    chart_html = create_pie_chart(result)

    return render_template('plotly.html', chart_html=chart_html)


# # REST API routes # #

app.route('/api/all', methods=['GET'])(rest_api.get_all)

app.route('/api/users', methods=['GET'])(rest_api.get_users)

app.route('/api/key/<key>', methods=['GET'])(rest_api.get_key)

# #                 # #


def _load_cache():
    cache = msal.SerializableTokenCache()
    if session.get("token_cache"):
        cache.deserialize(session["token_cache"])
    return cache


def _save_cache(cache):
    if cache.has_state_changed:
        session["token_cache"] = cache.serialize()


def _build_msal_app(cache=None, authority=None):
    return msal.ConfidentialClientApplication(
        fiscal_dict['CLIENT_ID'], authority=authority or fiscal_dict['AUTHORITY'],
        client_credential=fiscal_dict['CLIENT_SECRET'], token_cache=cache)


def _build_auth_code_flow(authority=None, scopes=None):
    return _build_msal_app(authority=authority).initiate_auth_code_flow(
        scopes or [],
        redirect_uri=url_for("authorized", _external=True))


def _get_token_from_cache(scope=None):
    cache = _load_cache()  # This web app maintains one cache per session
    cca = _build_msal_app(cache=cache)
    accounts = cca.get_accounts()
    if accounts:  # So all account(s) belong to the current signed-in user
        result = cca.acquire_token_silent(scope, account=accounts[0])
        _save_cache(cache)
        return result, accounts
    

def create_pie_chart(data: list[tuple]) -> str:
    """Create pie chart with data from database
    and return chart as an HTML string"""
    categories = [row[2] for row in data]
    values = [row[3] for row in data]
    fig = go.Figure(data=[go.Pie(labels=categories, values=values, hole=0.4)])
    return fig.to_html(full_html=False)


app.jinja_env.globals.update(_build_auth_code_flow=_build_auth_code_flow)


set_tracer_provider(TracerProvider())
get_tracer_provider().add_span_processor(
    BatchSpanProcessor(ConsoleSpanExporter())
)

instrumentor = FlaskInstrumentor()

instrumentor.instrument_app(app)

if __name__ == "__main__":
    app.run()
