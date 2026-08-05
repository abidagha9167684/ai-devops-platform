# DevOps Interview Notes

## What happens when code is pushed?

GitHub Actions checks out the repository, installs dependencies, runs tests, validates Terraform and Kubernetes files, builds the Docker image, and pushes it to Docker Hub.

## Why use Kubernetes?

Kubernetes provides self-healing, scaling, rolling updates, service discovery, and high availability for containerized applications.

## Why use Helm?

Helm packages Kubernetes resources, separates templates from configuration, and supports upgrades, release history, and rollbacks.

## What is the difference between ConfigMap and Secret?

A ConfigMap stores non-sensitive configuration. A Secret stores sensitive values such as tokens, passwords, and API keys.

## What is the difference between readiness and liveness probes?

Readiness decides whether a Pod should receive traffic. Liveness decides whether Kubernetes should restart the container.

## What does the HPA do?

The Horizontal Pod Autoscaler changes the number of Pods based on metrics such as CPU utilization.

## What is a PVC?

A PersistentVolumeClaim is an application request for persistent storage.

## Why run containers as non-root?

Running as non-root reduces the impact of a container compromise and follows the principle of least privilege.

## What is a rolling update?

A rolling update replaces old Pods gradually while keeping the application available.

## What is a Pod Disruption Budget?

It limits voluntary Pod disruptions so a minimum number of Pods remain available during maintenance.