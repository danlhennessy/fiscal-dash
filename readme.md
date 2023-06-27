# Fiscal Dash

Python Flask app designed to test the capabilities of Kubernetes and container tools / addons.
<br> 
<br> 

## Cluster Features
<br> 
<table>
    <tr>
        <th>Feature</th>
        <th></th>
        <th>Tool</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>Container Runtime</td>
        <td><img width="48" src="https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png"></td>
        <td><a href="https://www.docker.com/">Docker Engine</a></td>
        <td>Image and Container management, CRI tool using cri-dockerd</td>
    </tr>
    <tr>
        <td>Cluster Initialization</td>
        <td><img width="48" src="https://user-images.githubusercontent.com/22591623/59856252-74656b00-936e-11e9-8dd9-d6092845981b.png"></td>
        <td><a href="https://kubernetes.io/docs/reference/setup-tools/kubeadm/">Kubeadm</a></td>
        <td>Kubernetes cluster setup, initialization and node joining</td>
    </tr>
    <tr>
        <td>CI</td>
        <td><img width="48" src="https://avatars.githubusercontent.com/u/44036562?s=200&v=4)"></td>
        <td><a href=https://github.com/features/actions>Github Actions</a></td>
        <td>Continuous Integration - unpacked and packed testing</td>
    </tr>
    <tr>
        <td>CD</td>
        <td><img width="48" src="https://cncf-branding.netlify.app/img/projects/argo/icon/color/argo-icon-color.svg"></td>
        <td><a href="https://argoproj.github.io/cd">ArgoCD</a></td>
        <td>Continuous Deployment - Synchronise app manifests with Kubernetes</td>
    </tr>
    <tr>
        <td>Infrastructure Provisioning</td>
        <td><img width="56" src="https://cncf-branding.netlify.app/img/projects/crossplane/icon/color/crossplane-icon-color.png"></td>
        <td><a href="https://www.crossplane.io/">Crossplane</a></td>
        <td>Define external resources as CRDs and manage them in Kubernetes</td>
    </tr>
    <tr>
        <td>Release Management</td>
        <td><img width="48" src="https://cncf-branding.netlify.app/img/projects/helm/icon/color/helm-icon-color.png"></td>
        <td><a href="https://helm.sh/">Helm</a></td>
        <td>Package management - configure app versioning, repositories and dependencies</td>
    </tr>
    <tr>
        <td>Storage Operator</td>
        <td><img width="48" src="https://cncf-branding.netlify.app/img/projects/rook/icon/color/rook-icon-color.png"></td>
        <td><a href="https://rook.io/">Rook</a></td>
        <td>Cloud native storage orchestrator - link with distributed storage solution</td>
    </tr>
    <tr>
        <td>Service Mesh</td>
        <td><img width="42" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Istio-bluelogo-nobackground-unframed.svg/1365px-Istio-bluelogo-nobackground-unframed.svg.png"></td>
        <td><a href="https://istio.io/">Istio</a></td>
        <td>Cluster networking management and observability</td>
    </tr>
    <tr>
        <td>Policy Enforcement</td>
        <td><img width="48" src="https://landscape.cncf.io/logos/open-policy-agent-opa.svg"></td>
        <td><a href="https://www.openpolicyagent.org/">Open Policy Agent</a></td>
        <td>Polic-based control - manages and evaluates policies against incoming requests and configuration changes</td>
    </tr>
    <tr>
        <td>Vulnerability Scanning</td>
        <td><img width="48" src="https://api.civo.com/k3s-marketplace/kube-hunter.png"></td>
        <td><a href="https://github.com/aquasecurity/kube-hunter">kube-hunter</a></td>
        <td>Dynamic security tests (passive and active). Highlights potential threats </td>
    </tr>
    <tr>
        <td>Monitoring</td>
        <td><img width="48" src="https://artifacthub.io/image/0503add5-3fce-4b63-bbf3-b9f649512a86@1x"></td>
        <td><a href="https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack">kube-prometheus-stack</a></td>
        <td>Monitoring, alerting and visualisation stack including Prometheus, Alert Manager and Grafana</td>
    </tr>
    <tr>
        <td>Logging</td>
        <td><img width="48" src="https://seeklogo.com/images/E/elasticsearch-logo-C75C4578EC-seeklogo.com.png"></td>
        <td><a href="https://www.elastic.co/guide/en/cloud-on-k8s/2.8/k8s-quickstart.html">ECK</a></td>
        <td>Log management and delivery with Elastic Cloud on Kubernetes. Beats -> ElasticSearch -> Kibana</td>
    </tr>
    <tr>
        <td>APM</td>
        <td><img width="48" src="https://static-www.elastic.co/v3/assets/bltefdd0b53724fa2ce/blt5ceddec3c8f0ca55/5d082bb6877575d0584761ac/logo-apm-32-color.svg"></td>
        <td><a href="https://www.elastic.co/guide/en/cloud-on-k8s/2.8/k8s-apm-server.html">Elastic APM Server</a></td>
        <td>Application Performance Monitoring - integrated with ECK service</td>
    </tr>
    <tr>
        <td>Troubleshooting</td>
        <td><img width="48" src="https://lh5.googleusercontent.com/-hf9J6_pbnTk/AAAAAAAAAAI/AAAAAAAAAAA/-Ewgawd0NH4/s44-p-k-no-ns-nd/photo.jpg"></td>
        <td><a href="https://komodor.com/">Komodor</a></td>
        <td>Cluster troubleshooting platform - health monitoring and automated root cause detection</td>
    </tr>
    <tr>
        <td>Disaster Recovery</td>
        <td><img width="48" src="https://velero.io/img/Velero.svg"></td>
        <td><a href="https://velero.io/">Velero</a></td>
        <td>Data backups, migration and disaster recovery for cluster resources and PVs</td>
    </tr>
    <tr>
        <td>Secrets Management</td>
        <td><img width="48" src="https://www.nicepng.com/png/full/827-8272881_vault-logo-black-and-white-hashicorp-vault-logo.png"></td>
        <td><a href="https://www.vaultproject.io/">Vault</a></td>
        <td>Hashicorp Vault cluster for all project secrets, connection established with Github Actions environment secrets</td>
    </tr>
    <!-- Add more rows for other tools -->
</table>
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
