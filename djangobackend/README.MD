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


python manage.py shell
# Then in the shell:
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()


#### Project running command
docker run -e SECRET_KEY='___your_secret_key____' --name djangobackend --rm -p8000:8000 remote_monitoring

### build docker image locally and make them accessible by minikue
eval $(minikube docker-env)
docker build -t your_image_name .
docker image ls
eval $(minikube docker-env)
docker build --no-cache -t remote_monitoring_kube:latest .
unset DOCKER_TLS_VERIFY DOCKER_HOST DOCKER_CERT_PATH DOCKER_PROMPT

### Kubernetes deployment step
kubectl apply -f redis-persistent-volume.yaml
kubectl apply -f redis-deployment.yaml
kubectl create configmap django-config --from-env-file=.env
kubectl apply -f django-secret.yaml
kubectl apply -f django-web-deployment.yaml
--on new terminal
minikube tunnel
--on new terminal
kubectl get svc django-web-service
kubectl apply -f celery-worker-deployment.yaml
kubectl apply -f celery-beat-deployment.yaml

kubectl exec -it <pod-name> -- curl -v http://localhost:8000/health


