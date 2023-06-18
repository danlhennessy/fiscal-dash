# Fiscal Dash

Python Flask app designed to test the capabilities of Kubernetes and container tools / addons.
<br> 
<br> 

## Features
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
        <td><img width="32" src="https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png"></td>
        <td><a href="https://www.docker.com/">Docker Engine</a></td>
        <td>Image and Container management, CRI tool using cri-dockerd</td>
    </tr>
    <tr>
        <td>Cluster Initialization</td>
        <td><img width="32" src="https://user-images.githubusercontent.com/22591623/59856252-74656b00-936e-11e9-8dd9-d6092845981b.png"></td>
        <td><a href="https://kubernetes.io/docs/reference/setup-tools/kubeadm/">Kubeadm</a></td>
        <td>Kubernetes cluster setup, initialization and node joining</td>
    </tr>
    <tr>
        <td>CI</td>
        <td><img width="32" src="https://avatars.githubusercontent.com/u/44036562?s=200&v=4)"></td>
        <td><a href=https://github.com/features/actions>Github Actions</a></td>
        <td>Continuous Integration - unpacked and packed testing</td>
    </tr>
    <tr>
        <td>CD</td>
        <td><img width="32" src="https://cncf-branding.netlify.app/img/projects/argo/icon/color/argo-icon-color.svg"></td>
        <td><a href="https://argoproj.github.io/cd">ArgoCD</a></td>
        <td>Continuous Delivery - deploy app manifests to Kubernetes</td>
    </tr>
    <tr>
        <td>Secrets Management</td>
        <td><img width="32" src="https://www.nicepng.com/png/full/827-8272881_vault-logo-black-and-white-hashicorp-vault-logo.png"></td>
        <td><a href="https://www.vaultproject.io/">Vault</a></td>
        <td>Hashicorp Vault cluster for all project secrets, connection established with Github Actions environment secrets</td>
    </tr>
    <tr>
        <td>Infrastructure Provisioning</td>
        <td><img width="40" src="https://cncf-branding.netlify.app/img/projects/crossplane/icon/color/crossplane-icon-color.png"></td>
        <td><a href="https://www.crossplane.io/">Crossplane</a></td>
        <td>Define external resources as CRDs and manage them in Kubernetes</td>
    </tr>
    <tr>
        <td>Release Management</td>
        <td><img width="32" src="https://cncf-branding.netlify.app/img/projects/helm/icon/color/helm-icon-color.png"></td>
        <td><a href="https://helm.sh/">Helm</a></td>
        <td>Package management - configure app versioning, repositories and dependencies</td>
    </tr>
    <tr>
        <td>Service Mesh</td>
        <td><img width="32" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Istio-bluelogo-nobackground-unframed.svg/1365px-Istio-bluelogo-nobackground-unframed.svg.png"></td>
        <td><a href="https://istio.io/">Istio</a></td>
        <td>Cluster networking management and observability</td>
    </tr>
    <tr>
        <td>Monitoring</td>
        <td><img width="32" src="https://artifacthub.io/image/0503add5-3fce-4b63-bbf3-b9f649512a86@1x"></td>
        <td><a href="https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack">kube-prometheus-stack</a></td>
        <td>Monitoring, alerting and visualisation stack including Prometheus, Alert Manager and Grafana</td>
    </tr>
    <tr>
        <td>Logging</td>
        <td><img width="32" src="https://seeklogo.com/images/E/elasticsearch-logo-C75C4578EC-seeklogo.com.png"></td>
        <td><a href="https://www.elastic.co/">Elasticsearch</a></td>
        <td>Log management and delivery with Elasticsearch, Filebeat and Logstash</td>
    </tr>
    <tr>
        <td>Instrumentation</td>
        <td><img width="32" src="https://cncf-branding.netlify.app/img/projects/opentelemetry/icon/color/opentelemetry-icon-color.png"></td>
        <td><a href="https://opentelemetry.io/">OpenTelemetry</a></td>
        <td>OpenTelemetry integration with app for additional metrics and traces</td>
    </tr>
    <tr>
        <td>Troubleshooting</td>
        <td><img width="32" src="https://lh5.googleusercontent.com/-hf9J6_pbnTk/AAAAAAAAAAI/AAAAAAAAAAA/-Ewgawd0NH4/s44-p-k-no-ns-nd/photo.jpg"></td>
        <td><a href="https://komodor.com/">Komodor</a></td>
        <td>Cluster troubleshooting platform - health monitoring and automated root cause detection</td>
    </tr>
    <tr>
        <td>RBAC</td>
        <td><img width="32" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Microsoft_Azure.svg/1200px-Microsoft_Azure.svg.png"></td>
        <td><a href="https://azure.microsoft.com/en-gb/products/active-directory">Azure Active Directory</a></td>
        <td>Azure AD tenant built for app authentication with SSO using MSAL</td>
    </tr>
    <tr>
        <td>Web App Framework</td>
        <td><img width="32" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAJ1BMVEVHcEw4qL44qL44qL44qL44qL44qL44qL44qL44qL44qL44qL44qL4lcOQyAAAADHRSTlMAYZ42gQ7zt03gIst5VRyuAAAAr0lEQVQ4jb1Syw7DIAyDEF5p/v97BypUpJjdNkucbCWxjXP/RaTwjQ5Z1Z9pX1XPgsh6g4+zB+g4eyDvfNIV1y4gI0jgPiMAK1YFRWhieugWuSAbna2+J419unZ8eNJAgiLtzTRwXTzTSLgMXugCnaRJhwtG4cLddKMbkFPHLQS5xiaBdzz0yYlpdcYVV1Prt2it+SCSbLK2+IFqvKSNf+dWlksrS0ShFaZMBGv/FT7xQgzNC1BGFQAAAABJRU5ErkJggg=="></td>
        <td><a href="https://kubernetes.io/docs/reference/setup-tools/kubeadm/">Flask</a></td>
        <td>Micro Web App framework used as the base for the application</td>
    </tr>
    <tr>
        <td>API</td>
        <td><img width="32" src="https://restfulapi.net/wp-content/uploads/rest.png"></td>
        <td><a href="https://www.redhat.com/en/topics/api/what-is-a-rest-api">Flask-RESTful</a></td>
        <td>RESTful API built into Flask application</td>
    </tr>
        <tr>
        <td>Database</td>
        <td><img width="32" src="https://1000logos.net/wp-content/uploads/2020/08/MySQL-Logo.png"></td>
        <td><a href="https://www.mysql.com/">MySQL</a></td>
        <td>MySQL database hosted in an Amazon RDS. Interact securely via Flask app or API</td>
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
