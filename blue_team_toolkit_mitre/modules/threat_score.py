# modules/threat_score.py

from config import RISK_WEIGHTS

def calculate_score(alerts):
    total_score = 0

    for alert in alerts:
        total_score += RISK_WEIGHTS.get(alert["severity"], 0)

    return total_score
