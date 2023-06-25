https://blog.ediri.io/kube-prometheus-stack-and-argocd-25-server-side-apply-to-the-rescue

argocd app sync kube-prometheus-stack

https://prometheus.io/docs/instrumenting/exporters/

The exporter I am using for this app is Python lib prometheus-flask-exporter

ServiceMonitor (monitor.yaml) tells Prometheus to scrape the /metrics endpoint for my app