kubectl apply -f deployment.yml
kubectl apply -f service.yml

kubectl port-forward fiscal-service 5001:5000