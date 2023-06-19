helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install prom-stack prometheus-community/kube-prometheus-stack

helm uninstall prom-stack