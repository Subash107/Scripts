import requests
import logging

def send_slack_alert(webhook_url, message):
    if not webhook_url:
        return

    payload = {"text": message}

    try:
        requests.post(webhook_url, json=payload)
        logging.info("Slack alert sent")
    except Exception as e:
        logging.error(f"Slack alert failed: {str(e)}")
