#!/usr/bin/env bash
set -euo pipefail

echo "🔐 gcloud auth"
gcloud auth list

echo "📦 Project:"
gcloud config list project

echo "☁️ Services (Cloud Run):"
gcloud run services list --platform=managed --limit=5 || true

echo "🔗 Git remotes:"
git remote -v || true

echo "✅ Done."
