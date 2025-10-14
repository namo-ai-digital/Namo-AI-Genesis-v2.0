# Namo-AI-Genesis-v2.0 — The Living Ethical Intelligence System

[![GitLab CI](https://gitlab.com/NaMo_Nexus/Namo-AI-Genesis-v2.0/badges/main/pipeline.svg)](https://gitlab.com/NaMo_Nexus/Namo-AI-Genesis-v2.0/-/pipelines)

Namo AI (Genesis v2.0) is a comprehensive cognitive architecture designed to simulate emotional resonance, ethical reasoning, and compassionate intelligence. This project provides the full implementation of Namo AI, including its core cognitive modules, a REST API for interaction, and deployment scripts for Google Cloud Run.

## Project Overview

The core of Namo AI is built upon four key subsystems:

- **Emotional Mirror (`core/emotional_mirror.py`):** An engine for analyzing sentiment and generating empathetic responses.
- **Memory Nexus (`core/memory_nexus.py`):** A contextual memory system that stores and retrieves semantic and emotional data from interactions.
- **Ethical Engine (`core/ethical_engine.py`):** A controller for evaluating actions based on a framework of compassion and ethics.
- **Reasoning Core (`core/reasoning_core.py`):** The central logic unit that processes information, solves problems, and aligns its reasoning with the principles of the Ethical Engine.

These subsystems are integrated into a unified `NamoAI` class (`core/namo_ai.py`), which orchestrates the entire cognitive process.

## Getting Started

### Prerequisites

- Python 3.8+
- Docker
- Google Cloud SDK (for deployment)

### Local Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/icezingza/Namo-AI-Genesis-v2.0.git
    cd Namo-AI-Genesis-v2.0
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    uvicorn api.server:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`.

### Interacting with the API

You can interact with Namo AI by sending a `POST` request to the `/namo/interact` endpoint.

**Example using `curl`:**
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/namo/interact' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_id": "user123",
  "text": "I am feeling a bit uncertain about the future."
}'
```

### Docker

To build and run the application using Docker:

1.  **Build the image:**
    ```bash
    docker build -t namo-ai-genesis .
    ```

2.  **Run the container:**
    ```bash
    docker run -p 8000:8000 namo-ai-genesis
    ```

### Deployment to Google Cloud Run

The `scripts/deploy_cloud_run.sh` script automates the deployment process.

1.  **Set environment variables:**
    ```bash
    export PROJECT_ID="your-gcp-project-id"
    export REGION="your-gcp-region"
    ```

2.  **Run the deployment script:**
    ```bash
    bash scripts/deploy_cloud_run.sh
    ```

The script will build the Docker image, push it to Google Container Registry, and deploy it to Cloud Run. The service URL will be printed to the console upon completion.

**Cloud Run URL:** (To be added after deployment)

## CI/CD
- GitHub Actions: `.github/workflows/namo-build.yml` (build/test)
- Optional Deploy: `.github/workflows/deploy-cloudrun.yml`
- GitLab CI (prod deploy): `.gitlab-ci.yml`

### Deploy (local)
```bash
PROJECT_ID=<your-project> REGION=asia-southeast1 bash scripts/deploy_cloud_run.sh
```

### Canary Deployment
To perform a canary release, use the `deploy_canary.sh` script. This will deploy a new revision and split traffic 10/90 between the new and old revisions.
```bash
bash scripts/deploy_canary.sh
```

### Rollback
To rollback to the previous revision, run the following command, replacing `$REV_OLD` with the name of the revision you want to roll back to:
```bash
gcloud run services update-traffic namo-genesis --region asia-southeast1 --to-latest=false --to-revisions $REV_OLD=100
```

### Monitor

```bash
bash scripts/monitor_status.sh https://<your-service-url>
```
