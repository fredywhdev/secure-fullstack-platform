# 🔐 Secure Full-Stack Platform – DevSecOps Project

## 📌 Descripción

Plataforma Full-Stack desarrollada con enfoque DevSecOps, que integra desarrollo, contenedores, CI/CD y seguridad desde el pipeline.
El objetivo del proyecto es demostrar habilidades prácticas, no crear una app comercial.

## 🧩 Arquitectura

```text
[ Client ]
    |
    v
[ Nginx ]
    |
    +--> Frontend (Vue / React)
    |
    +--> Backend API (FastAPI)
            |
            v
        PostgreSQL
```

Reverse proxy con **Nginx**

Backend protegido con **JWT**

Base de datos aislada en red interna

Contenedores separados por responsabilidad

## 🛠️ Stack Tecnológico
### Backend

Python 3.11

FastAPI

SQLAlchemy

JWT (python-jose)

PostgreSQL

### Frontend

Vue 3 (o React)

Axios

Autenticación por token

### Infraestructura

Docker

Docker Compose

Nginx

### CI/CD & Seguridad

GitHub Actions

Bandit (SAST)

Trivy (Container Security Scan)

## 🔐 Seguridad Implementada

Hash de contraseñas con **bcrypt**

Autenticación JWT con expiración

Variables sensibles vía **ENV**

Usuario no root en contenedores

Escaneo de código (Bandit)

Escaneo de imágenes Docker (Trivy)

Pipeline falla ante vulnerabilidades HIGH/CRITICAL

Separación de redes en Docker

## 🔄 Pipeline CI/CD (DevSecOps)

El pipeline ejecuta automáticamente:

Checkout del código

Instalación de dependencias

Análisis estático de seguridad (Bandit)

Build de imagen Docker

Escaneo de vulnerabilidades en contenedor (Trivy)

Falla automática si se detectan riesgos críticos

## ☁️ Adaptación del proyecto a entornos Cloud (AKS / Azure)

Este proyecto fue diseñado como una **plataforma full-stack segura y automatizada**, siguiendo principios que permiten su despliegue y evolución en entornos cloud modernos basados en Kubernetes gestionado.

A continuación, se describe cómo este stack puede adaptarse y escalarse en plataformas como **Azure Kubernetes Service (AKS)**.

## ☸️ Kubernetes / AKS

El sistema utiliza manifiestos declarativos compatibles con Kubernetes estándar.

En un entorno AKS:

Separación por namespaces (*dev*, *staging*, *prod*).

Autoescalado horizontal (HPA) basado en métricas.

Integración con Ingress Controller y balanceo gestionado.

El enfoque prioriza **aislamiento, resiliencia y escalabilidad**.

## 🔁 CI/CD

El pipeline implementa un flujo típico de:

validación

build

containerización

despliegue

Puede integrarse fácilmente con:

GitLab CI

GitHub Actions

Azure Container Registry (ACR)

El objetivo es **despliegue continuo con bajo acoplamiento**.

## 🧱 Infraestructura como Código

La estructura del proyecto está pensada para convivir con definiciones de infraestructura versionadas.

En un escenario cloud:

Terraform puede usarse para gestionar AKS, redes, identidades y storage.

Se mantiene separación clara entre infraestructura y aplicación.

## 📊 Observabilidad y Monitorización

El diseño prioriza visibilidad del sistema y detección temprana de fallos.

Compatible con:

Prometheus para métricas

Grafana para visualización

centralización de logs (Loki / ELK / servicios gestionados)

Facilita **operación y troubleshooting en producción**.

## 🔐 Seguridad y Mentalidad de Plataforma

Aplica principios de:

mínimo privilegio

segmentación

automatización segura

Pensado para plataformas **API-first, escalables y orientadas a operación continua**.

## ▶️ Ejecución local
### Requisitos

Docker

Docker Compose

### Pasos
```text
git clone https://github.com/fredywhdev/secure-fullstack-platform.git
cd secure-fullstack-platform
cp .env.example .env
docker compose up -d --build
```

Accesos:

Frontend: http://localhost

Backend health: http://localhost/api/health

## 📂 Estructura del proyecto

```text
.
├── backend/
├── frontend/
├── nginx/
├── .github/workflows/
├── docker-compose.yml
├── .env.example
└── README.md
```
## 🎯 Objetivo del proyecto

Este proyecto demuestra:

Implementación **DevSecOps real**

Integración Full-Stack

Automatización CI/CD

Seguridad aplicada desde desarrollo

Buenas prácticas de contenedores

No es un tutorial, es una base **profesional reproducible**.

## 📌 Próximos pasos (roadmap)

Tests automatizados

HTTPS con certificados

Rate limiting

Roles avanzados

Deploy en cloud (AWS / GCP / Azure)

Integración real con AKS

Terraform para Azure

GitOps con ArgoCD

Dashboards avanzados de observabilidad

## 👤 Autor

### Fredy Hernandez
DevSecOps Specialist | Cloud · CI/CD · Secure Infrastructure · Full-Stack
