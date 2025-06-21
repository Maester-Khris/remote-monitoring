#!/bin/bash

set -e

echo "🔻 Starting cleanup of all related Kubernetes resources..."

# Delete deployments
echo "🧹 Deleting Deployments..."
kubectl delete deployment django-web-deployment nginx-static-server celery-worker-deployment celery-beat-deployment mysql-server redis-deployment --ignore-not-found
kubectl delete job django-migrate-job --ignore-not-found

# Delete services
echo "🧹 Deleting Services..."
kubectl delete svc django-service redis-service --ignore-not-found

# Delete pods (optional; they'll go with deployments, but included for safety)
echo "🧹 Deleting Pods..."
kubectl delete pods --selector=app=django --ignore-not-found
kubectl delete pods --selector=app=redis --ignore-not-found
kubectl delete pods --selector=app=celery --ignore-not-found

# Delete PVCs
echo "🧹 Deleting PersistentVolumeClaims..."
kubectl delete pvc --selector=app=redis --ignore-not-found

# Delete PersistentVolumes (optional: only if you're OK losing data)
echo "🧹 Deleting PersistentVolumes (⚠️ this removes any retained volume data)..."
kubectl delete pv --selector=app=redis --ignore-not-found
kubectl delete pv --selector=app=nginx-shared-pvc --ignore-not-found

# Delete ConfigMap
echo "🧹 Deleting ConfigMap..."
kubectl delete configmap django-config --ignore-not-found
kubectl delete configmap nginx-config --ignore-not-found

# Delete Secrets
echo "🧹 Deleting Secret..."
kubectl delete -f ./configs/django-secret.yaml --ignore-not-found

# Optionally: delete any created yaml-based resources
echo "🧹 Deleting YAML-defined resources..."
kubectl delete -f ./configs/django-secret.yaml --ignore-not-found
kubectl delete -f ./volumes/redis-persistent-volume.yaml --ignore-not-found  
# kubectl delete -f ./volumes/nginx-shared-volumel.yaml -force --grace-period=0 --ignore-not-found
kubectl delete -f ./deployments/redis-deployment.yaml --ignore-not-found
kubectl delete -f ./deployments/nginx-deployment.yaml --ignore-not-found
kubectl delete -f ./deployments/django-web-deployment.yaml --ignore-not-found
kubectl delete -f ./deployments/celery-worker-deployment.yaml --ignore-not-found
kubectl delete -f ./deployments/celery-beat-deployment.yaml --ignore-not-found
kubectl delete -f ./deployments/debug_pod.yaml --ignore-not-found
kubectl delete -f ./deployments/mysql-deployment.yaml --ignore-not-found
kubectl delete -f ./jobs/django-migrations-deployment.yaml --ignore-not-found

echo "✅ Cleanup complete. Your cluster is now in a clean state."
