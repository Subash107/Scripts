# modules/bruteforce_detector.py

from collections import Counter
from config import FAILED_THRESHOLD

def detect_bruteforce(logfile):
    ips = []
    alerts = []

    try:
        with open(logfile) as f:
            for line in f:
                if "Failed password" in line:
                    ip = line.split()[-1]
                    ips.append(ip)

        counter = Counter(ips)

        for ip, count in counter.items():
            if count >= FAILED_THRESHOLD:
                alerts.append({
                    "type": "bruteforce",
                    "severity": "critical",
                    "details": f"{ip} - {count} attempts"
                })
    except FileNotFoundError:
        pass

    return alerts
