# modules/network_monitor.py

import psutil

def detect_suspicious_connections():
    alerts = []

    for conn in psutil.net_connections(kind='inet'):
        if conn.raddr:
            if conn.raddr.port > 50000:
                alerts.append({
                    "type": "suspicious_connection",
                    "severity": "high",
                    "details": f"{conn.raddr.ip}:{conn.raddr.port}"
                })

    return alerts
