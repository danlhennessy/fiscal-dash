kubectl apply -f deployment.yml
kubectl apply -f service.yml

argocd app sync fiscal-dash

Access app externally at nodeIP:nodeport , or internally at clusterIP:port

kubectl delete -f deployment.yml
kubectl delete -f service.yml