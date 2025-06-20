#!/bin/bash

set -e

echo "🔻 Starting cleanup of all related Kubernetes resources..."

# Delete deployments
echo "🧹 Deleting Deployments..."
kubectl delete deployment django-web-deployment celery-worker-deployment celery-beat-deployment redis-deployment --ignore-not-found

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
kubectl delete -f django-secret.yaml --ignore-not-found

# Optionally: delete any created yaml-based resources
echo "🧹 Deleting YAML-defined resources..."
kubectl delete -f redis-persistent-volume.yaml --ignore-not-found
kubectl delete -f redis-deployment.yaml --ignore-not-found
kubectl delete -f nginx-deployment.yaml --ignore-not-found
kubectl delete -f django-secret.yaml --ignore-not-found
kubectl delete -f django-web-deployment.yaml --ignore-not-found
kubectl delete -f celery-worker-deployment.yaml --ignore-not-found
kubectl delete -f celery-beat-deployment.yaml --ignore-not-found

echo "✅ Cleanup complete. Your cluster is now in a clean state."
