import yaml
import time
import json
from utils.logger import setup_logger
from modules.health_check import check_service
from modules.disk_monitor import check_disk
from modules.docker_monitor import check_containers
from modules.log_monitor import scan_logs
from modules.backup_manager import create_backup
from modules.alert_manager import send_slack_alert

def run_toolkit():
    setup_logger()

    with open("config.yaml") as f:
        config = yaml.safe_load(f)

    service_status = check_service(config["service"]["name"])
    disk_alerts = check_disk(config["disk"]["threshold"])
    container_alerts = check_containers()
    log_alerts = scan_logs(
        config["log_monitor"]["file_path"],
        config["log_monitor"]["keywords"]
    )

    all_alerts = disk_alerts + container_alerts + log_alerts

    report = {
        "service_status": service_status,
        "alerts": all_alerts
    }

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)

    for alert in all_alerts:
        send_slack_alert(config["alerts"]["slack_webhook"], alert)

    create_backup(".")
