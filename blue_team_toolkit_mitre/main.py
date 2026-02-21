# main.py

from modules.process_monitor import scan_processes
from modules.reverse_shell_detector import detect_reverse_shell
from modules.network_monitor import detect_suspicious_connections
from modules.privilege_monitor import detect_privilege_escalation
from modules.bruteforce_detector import detect_bruteforce
from modules.threat_score import calculate_score
from modules.mitre_tagger import apply_mitre_tags

def main():
    all_alerts = []

    all_alerts.extend(scan_processes())
    all_alerts.extend(detect_reverse_shell())
    all_alerts.extend(detect_suspicious_connections())
    all_alerts.extend(detect_privilege_escalation())
    all_alerts.extend(detect_bruteforce("security.log"))

    # Apply MITRE tagging
    all_alerts = apply_mitre_tags(all_alerts)

    score = calculate_score(all_alerts)

    print("=== Alerts ===")
    for alert in all_alerts:
        print(alert)

    print("\nTotal Risk Score:", score)

if __name__ == "__main__":
    main()
