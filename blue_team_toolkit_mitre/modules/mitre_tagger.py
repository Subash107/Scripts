# modules/mitre_tagger.py

from config import MITRE_MAPPING

def apply_mitre_tags(alerts):
    for alert in alerts:
        mapping = MITRE_MAPPING.get(alert["type"])
        if mapping:
            alert["mitre_tactic"] = mapping["tactic"]
            alert["mitre_technique"] = mapping["technique"]
        else:
            alert["mitre_tactic"] = "Unknown"
            alert["mitre_technique"] = "Unknown"

    return alerts
