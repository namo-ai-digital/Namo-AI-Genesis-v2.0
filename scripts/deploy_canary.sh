#!/usr/bin/env bash
set -euo pipefail
PROJECT_ID="${PROJECT_ID:-arctic-signer-471822-i8}"
REGION="${REGION:-asia-southeast1}"
SERVICE="${SERVICE:-namo-genesis}"
IMAGE="gcr.io/${PROJECT_ID}/${SERVICE}:$(date +%Y%m%d-%H%M%S)"

gcloud builds submit --tag "$IMAGE"
# สร้างรีวิชั่นใหม่
gcloud run deploy "$SERVICE" --image "$IMAGE" --region "$REGION" --no-traffic
REV_NEW=$(gcloud run revisions list --service="$SERVICE" --region="$REGION" --format='value(metadata.name)' --sort-by=~metadata.creationTimestamp | head -n1)
REV_OLD=$(gcloud run services describe "$SERVICE" --region="$REGION" --format='value(status.traffic[0].revisionName)')

# ปล่อย Canary 10%
gcloud run services update-traffic "$SERVICE" --region="$REGION" --to-revisions "$REV_NEW"=10 "$REV_OLD"=90
echo "Canary: $REV_NEW → 10% | Stable: $REV_OLD → 90%"
