# Deployment Guide

## Clone the repository

```bash
git clone <repository-url>
cd ai-devops-platform
```

## Run locally

```bash
docker compose up
```

## Deploy with Helm

```bash
helm install ai-devops-platform ./helm/ai-devops-platform -n ai-devops
```

## Upgrade

```bash
helm upgrade ai-devops-platform ./helm/ai-devops-platform -n ai-devops
```

## Rollback

```bash
helm rollback ai-devops-platform 1 -n ai-devops
```

## Verify

```bash
kubectl get all -n ai-devops
```