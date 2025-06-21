## Full stack app project real life application
- log all event(incomming http request) in a separate file
- use the celery task to read the log file and send new update to streaming endpoint
- which streaming protocol would be better; sse(because other way direction communication is not needed) or websocket
- in the case of sse : when does the backend stop sendng update ?

# Future update on log streaming
- logs file autodiscovery - ❕
- logs chunks merging and push to remote instance - ✅
- when pushing a single line to the client how to tie it with the file is coming from - ✅
- what will happen when a new celery beat will happen does all the files and all their content be pushed again -> keep track of the last read point (irrelevant: celery is confgured to work with ws, actually we are working with sse steam)- ✅

# New update: long live sse stream connection
## keys to architecture design: small stateful pipeline with per-file tracking mechanism and log tailing
- how to keep track of log files last read times: per file offsets - ✅
- how to fire sse_stream to push new change: loop forever - ✅

# Actual system application
- real time troubleshooting
- monitoring server health
- security auditing

# Notes:
- Log tailing in a web server is the process of monitoring the server's log files in real-time as new entries are written to them.
- Implemented a polling based tailing loop in the sse view: similar to tail -f, with low latency and no duplication

# Then in the shell:
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()


#### Project running command
docker run -e SECRET_KEY='___your_secret_key____' --name djangobackend --rm -p8000:8000 remote_monitoring

### build docker image locally and make them accessible by minikube
#### working session start
minikube start
eval $(minikube docker-env)
sh ./infra_deployment/cleanup.sh
docker container prune -f
docker image prune -f 
docker build --no-cache -t remote_monitoring_kube:latest .
cd infra_deployment
sh deployment.sh
kubectl get deployment
kubectl get pods

#### infrastructure live interaction
gnome-terminal --tab --working-directory="$(pwd)" -- bash -c "minikube tunnel; exec bash"
gnome-terminal --tab --working-directory="$(pwd)" -- bash -c "kubectl get svc nginx-service; exec bash"
kubectl get svc nginx-service
kubectl get svc django-web-service

#### code update
sh cleanup.sh
sh deployment.sh
kubectl rollout restart deployment nginx-static-server django-web-deployment mysql-server django-migrate-job

#### interacting with cluster
##### code (env) files changes
kubectl delete pods -l app=django-web
kubectl rollout restart deployment nginx-static-server && django-web-deployment

##### pods monitoring
kubectl describe pod django-web-deployment-7f69566db7-9542f
kubectl exec -it <pod-name> -- curl -v http://localhost:8000/health
kubectl exec -it django-web-deployment-7f69566db7-9542f  -- python manage.py shell 

##### debug pod analysis
kubectl apply -f debug_pod.yaml
kubectl exec -it debug-pod -- sh

#### working session close
unset DOCKER_TLS_VERIFY DOCKER_HOST DOCKER_CERT_PATH DOCKER_PROMPT


### Kubernetes deployment step
kubectl create configmap django-config --from-env-file=.env
kubectl apply -f redis-persistent-volume.yaml
kubectl apply -f redis-deployment.yaml
kubectl apply -f django-secret.yaml
kubectl apply -f django-web-deployment.yaml
kubectl apply -f celery-worker-deployment.yaml
kubectl apply -f celery-beat-deployment.yaml


### nginx conf updates
kubectl create configmap nginx-config --from-file=default.conf=nginx.conf --dry-run=client -o yaml | kubectl apply -f -
kubectl apply -f nginx-deployment.yaml
kubectl rollout restart deployment nginx-static-server

--on new terminal




