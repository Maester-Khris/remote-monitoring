#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

echo "Starting infrastructure deployment on Minikube..."

# Check if configs file exists
if [ ! -f ./configs/.env ] || [ ! -f ./configs/nginx.conf ]; then
  if [ ! -f ./configs/.env ]; then
    echo "❌ .env file not found!"
  fi
  if [ ! -f ./configs/nginx.conf ]; then
    echo "❌ nginx.conf not found!"
  fi
  exit 1
fi

# ======= Apply configs: config map and secrets
echo "🔧 Creating ConfigMap from .env..."
kubectl create configmap django-config --from-env-file=./configs/.env --dry-run=client -o yaml | kubectl apply -f -
echo "🔧 Creating ConfigMap from nginx.conf..."
kubectl create configmap nginx-config --from-file=default.conf=./configs/nginx.conf --dry-run=client -o yaml | kubectl apply -f -
echo "🔐 Applying Django Secret..."
kubectl apply -f ./configs/django-secret.yaml

# ======= Apply Persistent Volume
echo "📦 Applying Redis Persistent Volume..."
kubectl apply -f ./volumes/redis-persistent-volume.yaml
kubectl apply -f ./volumes/nginx-shared-volumel.yaml

# ======= Deployments
echo "🚀 Applying Redis Deployment..."
kubectl apply -f ./deployments/redis-deployment.yaml
echo "🚀 Applying Mysql Deployment..."
kubectl apply -f ./deployments/mysql-deployment.yaml
echo "🌐 Applying Nginx prox Web Deployment..."
kubectl apply -f ./deployments/nginx-deployment.yaml
echo "🌐 Applying Django Web Deployment..."
kubectl apply -f ./deployments/django-web-deployment.yaml
echo "🌐 Applying Django Migration Deployment..."
kubectl apply -f ./jobs/django-migrations-deployment.yaml
echo "🔧 Applying Celery Worker Deployment..s."
kubectl apply -f ./deployments/celery-worker-deployment.yaml
echo "⏰ Applying Celery Beat Deployment..."
kubectl apply -f ./deployments/celery-beat-deployment.yaml
# echo "⏰ Applying Debug pod Deployment..."
# kubectl apply -f ./deployments/debug_pod.yaml

echo "✅ Infrastructure deployment completed successfully."
