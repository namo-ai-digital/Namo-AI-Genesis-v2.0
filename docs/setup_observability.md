# Observability Setup for Namo AI

This guide provides a brief overview of how to monitor the Namo AI service using Google Cloud's operations suite (formerly Stackdriver).

## 1. Viewing Logs in Logs Explorer

All output from the Cloud Run service, including `print` statements and exceptions, is automatically sent to Logs Explorer.

1.  Go to the **[Logs Explorer](https://console.cloud.google.com/logs/viewer)** in the GCP Console.
2.  In the query builder, select the resource **Cloud Run Revision > namo-genesis**.
3.  You can filter logs by severity (e.g., `severity=ERROR`) or search for specific text.

## 2. Monitoring Metrics in Cloud Monitoring

Cloud Run provides several key metrics out-of-the-box, such as request count, request latencies, and container CPU/memory utilization.

1.  Go to **[Cloud Monitoring](https://console.cloud.google.com/monitoring)** in the GCP Console.
2.  Navigate to **Dashboards**.
3.  You will find a pre-built dashboard for Cloud Run. Select your service (`namo-genesis`) to view its performance metrics.

## 3. Creating an Uptime Check

An uptime check periodically verifies that your service is responding to requests.

1.  In **Cloud Monitoring**, go to **Uptime checks**.
2.  Click **Create uptime check**.
3.  Configure the check:
    *   **Target:**
        *   **Protocol:** `HTTPS`
        *   **Resource Type:** `URL`
        *   **Hostname:** Your service's Cloud Run URL.
        *   **Path:** `/` (or a dedicated health check endpoint if you create one).
    *   **Response Validation:** You can set rules for what constitutes a successful response (e.g., expected text in the response body).
    *   **Alerting:** Configure a notification channel (e.g., email, Slack) to be notified if the uptime check fails.
4.  The `scripts/monitor_status.sh` script can be used locally to perform a similar check.
