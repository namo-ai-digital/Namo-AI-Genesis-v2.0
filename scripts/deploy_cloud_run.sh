#!/usr/bin/env bash
set -euo pipefail
PROJECT_ID="${PROJECT_ID:-arctic-signer-471822-i8}"
REGION="${REGION:-asia-southeast1}"
SERVICE="${SERVICE:-namo-genesis}"
IMAGE="gcr.io/${PROJECT_ID}/${SERVICE}:latest"

echo "🛠 Build & Push: $IMAGE"
gcloud builds submit --tag "$IMAGE"

echo "🚀 Deploy: $SERVICE"
gcloud run deploy "$SERVICE" \
  --image "$IMAGE" \
  --region "$REGION" \
  --allow-unauthenticated \
  --set-env-vars MODEL_NAME="namo-stub"

echo "🌐 URL:"
gcloud run services describe "$SERVICE" --region "$REGION" --format='value(status.url)'
