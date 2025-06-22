## cloud architecture deployment component
- EKS Cluster 
- EC2 node for cluster worker nodes: django app, celery worker, celery beat
- Fargate instance for djangoapp migration job
- EFS IA tier as shared volume (between nginx and django app)
- EBS gp3 for redis volume
- ec2 t3 small for mysql server, celery worker, celery beat

Node Group Size	Recommendation
EC2 Instances	2–3 t3.medium or t3.small
Capacity	Enough to run:
- 3 Django pods
- 1 Celery Worker
- 1 Celery Beat
- 1 MySQL pod
- 1 Redis pod
- 1 NGINX pod

questions
- how is nginx deployed
- is ec2 T2.micro instance with 10gb enough for mysql server 8
- the local cluster deployment integra a 3 replica for the django app with a loadbalancer service how will the be deployed inside the eks cluster


## System design phases
Here’s a **step-by-step plan** to transform your local dev infrastructure into a production-grade AWS deployment using **EKS (Kubernetes), NGINX, S3, and RDS MySQL**:

---

### 🌐 **Phase 1: Preparation and Infrastructure Setup**



3. **Set Up S3 Buckets** (not mandatory)

   * Create S3 buckets for static and media files (with proper policies).

4. **Create ECR Repository**

   * Set up a private ECR to host your Docker images.

5. **Provision EKS Cluster**

   * Create the Kubernetes control plane and worker nodes (Fargate or EC2-backed).

---

### 🚢 **Phase 2: Docker Image and Registry**

6. **Build and Tag Production Docker Image**

   * Ensure your image uses collectstatic and production settings.

7. **Push Docker Image to ECR**

   * Authenticate and upload your image to AWS ECR.

---

### ☁️ **Phase 3: Kubernetes Manifests & Secrets**

8. **Create Kubernetes Secrets and ConfigMaps**

   * Store environment variables, Django secrets, and AWS credentials.

9. **Write K8s Manifests for Django App**

   * Define Deployments, Services, Volumes, and Readiness/Liveness probes.

10. **Add Celery and Celery Beat Deployments**

    * Separate deployments for background task processing.

11. **Set Up NGINX Ingress Controller**

    * Use Ingress with TLS for routing and SSL termination.

---

### 🗃️ **Phase 4: Static/Media File Handling**

12. **Configure Django for S3 Storage**

    * Use `django-storages` to route static/media to S3.

13. **Set Appropriate S3 Bucket Policies**

    * Secure buckets with correct read/write permissions.

---

### 🧪 **Phase 5: Testing and Optimization**

14. **Deploy to EKS**

    * Apply all manifests to the cluster using `kubectl`.

15. **Monitor and Debug**

    * Use `kubectl logs`, `describe`, and CloudWatch for troubleshooting.

16. **Add Auto-Scaling and Resource Limits**

    * Define HPA, CPU/memory requests/limits.

---

### 🔐 **Phase 6: Security and Observability**

17. **Configure HTTPS via ACM + Ingress**

    * Use AWS Certificate Manager for TLS certificates.

18. **Enable CloudWatch Logs and Metrics**

    * Stream logs and monitor app health in AWS.

19. **Set Up IAM Roles for Service Accounts (IRSA)**

    * Securely give pods access to S3 or other AWS services.

---

Let me know if you'd like this translated into Terraform steps or a GitOps pipeline.


## Visual Overview
            