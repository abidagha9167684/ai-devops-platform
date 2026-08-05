# AI DevOps Platform Architecture

```text
                 GitHub
                    │
                    ▼
           GitHub Actions (CI/CD)
                    │
                    ▼
              Docker Hub
                    │
                    ▼
             Kubernetes Cluster
                    │
     ┌──────────────┼──────────────┐
     │              │              │
 Deployment      Service       Ingress
     │              │              │
     ▼              ▼              ▼
   Flask Pods  ConfigMap     ai-devops.local
       │
       ├──────────────┐
       ▼              ▼
    Secret          PVC
       │              │
       └──────────────┘
              │
              ▼
      Persistent Volume

Monitoring
──────────
Prometheus ─────► Grafana

Infrastructure
──────────────
Terraform
```