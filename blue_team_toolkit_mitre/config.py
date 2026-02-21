# config.py

FAILED_THRESHOLD = 5

SUSPICIOUS_KEYWORDS = [
    "nc.exe",
    "powershell -enc",
    "xmrig",
    "mimikatz",
    "whoami /priv"
]

RISK_WEIGHTS = {
    "low": 5,
    "medium": 10,
    "high": 20,
    "critical": 40
}

# MITRE ATT&CK Mapping
MITRE_MAPPING = {
    "reverse_shell": {"tactic": "Execution", "technique": "T1059"},
    "bruteforce": {"tactic": "Credential Access", "technique": "T1110"},
    "process": {"tactic": "Execution", "technique": "T1059"},
    "suspicious_connection": {"tactic": "Command and Control", "technique": "T1071"},
    "privilege_escalation": {"tactic": "Privilege Escalation", "technique": "T1068"},
    "windows_event": {"tactic": "Credential Access", "technique": "T1110"}
}
