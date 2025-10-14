#!/usr/bin/env bash
set -euo pipefail
URL="${1:-$CLOUD_RUN_URL}"
test -z "$URL" && { echo "Usage: $0 <CLOUD_RUN_URL>"; exit 1; }

echo "💬 Interact"
curl -s -X POST "$URL/namo/interact" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "monitor", "text":"สวัสดี NAMO"}' | jq .
