# modules/privilege_monitor.py

import psutil

def detect_privilege_escalation():
    alerts = []

    for proc in psutil.process_iter(['pid', 'username', 'name']):
        try:
            if proc.info['username'] and "system" in proc.info['username'].lower():
                if proc.info['name'].lower() not in ["services.exe", "lsass.exe"]:
                    alerts.append({
                        "type": "privilege_escalation",
                        "severity": "critical",
                        "details": f"{proc.info['name']} running as SYSTEM"
                    })
        except:
            pass

    return alerts
