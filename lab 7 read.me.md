# Lab 7 – Kubernetes on AWS

## Overview
In this lab, we containerized the Appointment Scheduler app and deployed it to a **Kubernetes cluster** on AWS (EKS or Minikube).  
This lab introduces container orchestration concepts, scaling, and service discovery.

---

## Objectives
- Package the application into a **Docker container**.
- Create Kubernetes **manifests** (Deployment, Service, ConfigMap).
- Deploy the app to a Kubernetes cluster.
- Expose the app externally using a **LoadBalancer Service**.
- Verify scaling and rolling updates.

---

## Prerequisites
- Docker installed and running  
- kubectl CLI installed  
- AWS CLI configured  
- EKS or Minikube cluster available  

---

## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/HiwotJewore/hairsalon-appointment-scheducler.git
cd hairsalon-appointment-scheducler
