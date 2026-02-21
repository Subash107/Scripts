import logging

def scan_logs(file_path, keywords):
    alerts = []

    try:
        with open(file_path, "r", errors="ignore") as f:
            for line in f:
                for keyword in keywords:
                    if keyword in line:
                        message = f"Log Alert: {line.strip()}"
                        logging.warning(message)
                        alerts.append(message)
    except Exception as e:
        logging.error(f"Log scan error: {str(e)}")

    return alerts
