# Production CI/CD with GitLab

This document outlines the steps to configure a production CI/CD pipeline for the Namo-AI-Genesis-v2.0 project using GitLab.

## 1. Mirror GitHub Repository to GitLab

To ensure that the GitLab repository is always up-to-date with the main GitHub repository, we will configure a pull mirror.

1.  **Navigate to your GitLab project.**
2.  Go to **Settings > Repository**.
3.  Expand the **Mirroring repositories** section.
4.  Configure the following settings:
    *   **Mirror direction:** `Pull from`
    *   **Git repository URL:** `https://github.com/icezingza/Namo-AI-Genesis-v2.0.git`
    *   **Authentication method:** `Password`
    *   **Password:** Use a GitHub Personal Access Token (PAT) with `read_repo` permissions.

## 2. Configure GitLab CI/CD Variables

The `.gitlab-ci.yml` file requires the following CI/CD variables to be set in your GitLab project for authentication and configuration:

1.  Navigate to **Settings > CI/CD**.
2.  Expand the **Variables** section.
3.  Add the following variables:
    *   **`PROJECT_ID`**: Your Google Cloud Project ID (e.g., `arctic-signer-471822-i8`).
        *   *Flags*: Protected, Masked
    *   **`REGION`**: The Google Cloud region for your Cloud Run service (e.g., `asia-southeast1`).
        *   *Flags*: Protected
    *   **`GCLOUD_SERVICE_KEY`**: The JSON content of your Google Cloud service account key.
        *   *Flags*: Protected, Masked
