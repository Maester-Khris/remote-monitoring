#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

echo "Starting infrastructure deployment on Minikube..."

# Check if .env file exists
if [ ! -f .env ]; then
  echo "❌ .env file not found!"
  exit 1
fi

# Create config map from .env
echo "🔧 Creating ConfigMap from .env..."
kubectl create configmap django-config --from-env-file=.env --dry-run=client -o yaml | kubectl apply -f -

# Apply Redis Persistent Volume
echo "📦 Applying Redis Persistent Volume..."
kubectl apply -f redis-persistent-volume.yaml

# Apply Redis Deployment
echo "🚀 Applying Redis Deployment..."
kubectl apply -f redis-deployment.yaml

# Apply Django Secret
echo "🔐 Applying Django Secret..."
kubectl apply -f django-secret.yaml

# Apply Django Web Deployment
echo "🌐 Applying Django Web Deployment..."
kubectl apply -f django-web-deployment.yaml

# Apply Celery Worker Deployment
echo "🔧 Applying Celery Worker Deployment..."
kubectl apply -f celery-worker-deployment.yaml

# Apply Celery Beat Deployment
echo "⏰ Applying Celery Beat Deployment..."
kubectl apply -f celery-beat-deployment.yaml

echo "✅ Infrastructure deployment completed successfully."
