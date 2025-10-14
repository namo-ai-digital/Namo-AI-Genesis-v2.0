name: Namo Genesis — Deploy Cloud Run

on:
  workflow_dispatch:
  push:
    branches: [ main ]
    paths:
      - "Dockerfile"
      - "api/**"
      - "core/**"
      - ".github/workflows/deploy-cloudrun.yml"

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write
    env:
      PROJECT_ID: ${{ secrets.GCP_PROJECT_ID }}
      REGION: ${{ secrets.GCP_REGION }}
      SERVICE: "namo-genesis"
      IMAGE: "gcr.io/${{ secrets.GCP_PROJECT_ID }}/namo-genesis:latest"
    steps:
      - uses: actions/checkout@v4

      - name: Set up gcloud
        uses: google-github-actions/setup-gcloud@v2
        with:
          project_id: ${{ secrets.GCP_PROJECT_ID }}
          service_account_key: ${{ secrets.GCLOUD_SERVICE_KEY }}
          export_default_credentials: true

      - name: Build & Push Container
        run: |
          gcloud builds submit --tag "$IMAGE"

      - name: Deploy to Cloud Run
        run: |
          gcloud run deploy "$SERVICE" \
            --image "$IMAGE" \
            --region "$REGION" \
            --allow-unauthenticated \
            --set-env-vars MODEL_NAME="namo-stub"

      - name: Print URL
        run: |
          gcloud run services describe "$SERVICE" --region "$REGION" --format='value(status.url)'
