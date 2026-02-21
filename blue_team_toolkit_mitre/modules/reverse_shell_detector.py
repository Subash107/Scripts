# modules/reverse_shell_detector.py

import psutil

PATTERNS = ["nc -e", "bash -i", "powershell tcpclient", "invoke-expression"]

def detect_reverse_shell():
    alerts = []

    for proc in psutil.process_iter(['pid', 'cmdline']):
        try:
            cmd = " ".join(proc.info['cmdline']).lower()
            for pattern in PATTERNS:
                if pattern in cmd:
                    alerts.append({
                        "type": "reverse_shell",
                        "severity": "critical",
                        "details": cmd
                    })
        except:
            pass

    return alerts
