# Fiscal Dash

Python Flask app designed to test the capabilities of Kubernetes and container tools / addons.
<br> 
<br> 

## Application Features
<br>

### Fiscal Dash
<br>
<table>
    <tr>
        <th>Feature</th>
        <th></th>
        <th>Tool</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>RBAC</td>
        <td><img width="48" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Microsoft_Azure.svg/1200px-Microsoft_Azure.svg.png"></td>
        <td><a href="https://azure.microsoft.com/en-gb/products/active-directory">Azure Active Directory</a></td>
        <td>Azure AD tenant built for app authentication with SSO using MSAL</td>
    </tr>
    <tr>
        <td>Web App Framework</td>
        <td><img width="48" src="https://cdn.icon-icons.com/icons2/2389/PNG/512/flask_logo_icon_145276.png"></td>
        <td><a href="https://kubernetes.io/docs/reference/setup-tools/kubeadm/">Flask</a></td>
        <td>Micro Web App framework used as the base for the application</td>
    </tr>
    <tr>
        <td>API</td>
        <td><img width="48" src="https://restfulapi.net/wp-content/uploads/rest.png"></td>
        <td><a href="https://www.redhat.com/en/topics/api/what-is-a-rest-api">Flask-RESTful</a></td>
        <td>RESTful API built into Flask application</td>
    </tr>
        <tr>
        <td>Database</td>
        <td><img width="48" src="https://1000logos.net/wp-content/uploads/2020/08/MySQL-Logo.png"></td>
        <td><a href="https://www.mysql.com/">MySQL</a></td>
        <td>MySQL database hosted in an Amazon RDS. Interact securely via Flask app or API</td>
    </tr>
    <tr>
        <td>Instrumentation</td>
        <td><img width="48" src="https://cncf-branding.netlify.app/img/projects/opentelemetry/icon/color/opentelemetry-icon-color.png"></td>
        <td><a href="https://opentelemetry.io/">OpenTelemetry</a></td>
        <td>OpenTelemetry configured for additional metrics and traces</td>
    </tr>
    <tr>
        <td>Security Testing (Static)</td>
        <td><img width="48" src="https://files.readme.io/bb9fa64-bandit-logo.png"></td>
        <td><a href="https://github.com/PyCQA/bandit">Bandit</a></td>
        <td>Security linter automatically ran during Continuous Integration checks</td>
    </tr>
    <tr>
        <td>Security Testing (Dynamic)</td>
        <td><img width="48" src="https://avatars.githubusercontent.com/u/6716868?s=280&v=4"></td>
        <td><a href="https://www.zaproxy.org/">OWASP ZAP</a></td>
        <td>Dynamic security tests for semi-deployed and deployed application</td>
    </tr>
    <!-- Add more rows for other tools -->
</table>

## Getting Started

Work in progress...

### Installing

A step by step series of examples that tell you how to get a development
environment running

Say what the step will be

    Give the example

And repeat

    until finished

End with an example of getting some data out of the system or using it
for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Sample Tests

Explain what these tests test and why

    Give an example

### Style test

Checks if the best practices and the right coding style has been used.

    Give an example

## Deployment

Add additional notes to deploy this on a live system

## License

This project is licensed under the [CC0 1.0 Universal](LICENSE.md)
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for
details
