import requests
from flask import Flask, render_template, session, request, redirect, url_for
from flask_session import Session  # https://pythonhosted.org/Flask-Session
import matplotlib.pyplot as plt
import msal
import mysql.connector
import plotly.graph_objects as go
import io
import base64
import app_config
# This section is needed for url_for("foo", _external=True) to automatically
# generate http scheme when this sample is running on localhost,
# and to generate https scheme when it is deployed behind reversed proxy.
# See also https://flask.palletsprojects.com/en/1.0.x/deploying/wsgi-standalone/#proxy-setups
from werkzeug.middleware.proxy_fix import ProxyFix


app = Flask(__name__)
app.config.from_object(app_config)
Session(app)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

conn = mysql.connector.connect(
    host='localhost',
    user=app_config.DB_USER,
    password=app_config.DB_PASS,
    database=app_config.DB_NAME
)


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
    session["flow"] = _build_auth_code_flow(scopes=app_config.SCOPE)
    return render_template(
        "login.html",
        auth_url=session["flow"]["auth_uri"],
        version=msal.__version__
        )


@app.route(app_config.REDIRECT_PATH)
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
        app_config.AUTHORITY + "/oauth2/v2.0/logout" +
        "?post_logout_redirect_uri=" + url_for("index", _external=True))


@app.route("/graphcall")
def graphcall():
    token, accounts = _get_token_from_cache(app_config.SCOPE)
    if not token:
        return redirect(url_for("login"))
    graph_data = requests.get(  # Use token to call downstream service
        app_config.ENDPOINT,
        headers={'Authorization': 'Bearer ' + token['access_token']},
        ).json()
    return render_template('display.html', result=graph_data, accounts=accounts)


@app.route("/dashboard")
def dashboard():
    token, accounts = _get_token_from_cache(app_config.SCOPE)
    if not token:
        return redirect(url_for("login"))
    user = (accounts[0]['username'])
    labels = ['Category A', 'Category B', 'Category C']
    values = [30, 50, 20]

    # Create pie chart
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.set_title('Sample Pie Chart')

    # Save the chart image as bytes in memory
    chart_bytes = io.BytesIO()
    plt.savefig(chart_bytes, format='png')
    plt.close()

    # Encode the chart image data to base64
    chart_base64 = base64.b64encode(chart_bytes.getvalue()).decode('utf-8')

    # Render the template with the base64-encoded image data
    return render_template('dashboard.html', chart_base64=chart_base64, user=user)


@app.route('/update_piechart', methods=['POST'])
def update_piechart():
    # Get the values from the form submitted by the user
    user = request.form.get('user')
    category = request.form.get('category')
    value = int(request.form.get('value'))

    update_database(
        table="pie_data",
        keys=["user", "category", "value"],
        values=[user, category, value],
        connection=conn
        )

    # Redirect the user back to the pie chart page
    return redirect('/plotly')


@app.route("/plotly")
def plotly():
    token, accounts = _get_token_from_cache(app_config.SCOPE)
    if not token:
        return redirect(url_for("login"))

    result = retrieve_database(
        table="pie_data",
        keys=["id", "user", "category", "value"],
        connection=conn
        )

    # Create pie chart using selected values from the database
    categories = [row[2] for row in result]
    values = [row[3] for row in result]
    fig = go.Figure(data=[go.Pie(labels=categories, values=values, hole=0.4)])

    # Render the chart to an HTML string
    chart_html = fig.to_html(full_html=False)

    # Pass the chart HTML to the template
    return render_template('plotly.html', chart_html=chart_html)


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
        app_config.CLIENT_ID, authority=authority or app_config.AUTHORITY,
        client_credential=app_config.CLIENT_SECRET, token_cache=cache)


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


def retrieve_database(table: str, keys: list[str], connection: mysql.connector.MySQLConnection):
    cursor = connection.cursor()
    query = f"SELECT {', '.join(keys)} FROM {table}"
    cursor.execute(query)
    return cursor.fetchall()


def update_database(table: str, keys: list[str], values: list[str], connection: mysql.connector.MySQLConnection):
    try:
        cursor = connection.cursor()
        placeholders = ','.join(['%s'] * len(keys))
        query = f"INSERT INTO {table} ({','.join(keys)}) VALUES ({placeholders})"
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
    except ValueError as updateDB_error:
        print(f"Error: {updateDB_error}")


app.jinja_env.globals.update(_build_auth_code_flow=_build_auth_code_flow)  # Used in template

if __name__ == "__main__":
    app.run()
