# modules/process_monitor.py

import psutil
from config import SUSPICIOUS_KEYWORDS

def scan_processes():
    alerts = []

    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmd = " ".join(proc.info['cmdline']).lower()
            for keyword in SUSPICIOUS_KEYWORDS:
                if keyword in cmd:
                    alerts.append({
                        "type": "process",
                        "severity": "high",
                        "details": cmd
                    })
        except:
            pass

    return alerts
