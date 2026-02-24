import os
import re
import csv
import math
from datetime import datetime

BACKUP_DIR = r"D:\backup"

SUSPICIOUS_PATTERNS = {
    "Hardcoded Password": (r"password\s*=\s*['\"].+['\"]", "CRITICAL"),
    "API Key": (r"api[_-]?key\s*=\s*['\"].+['\"]", "HIGH"),
    "JWT Secret": (r"secret\s*=\s*['\"].+['\"]", "CRITICAL"),
    "Private Key": (r"-----BEGIN PRIVATE KEY-----", "CRITICAL"),
    "Debug Enabled": (r"debug\s*=\s*true", "MEDIUM"),
    "AWS Secret": (r"aws_secret_access_key", "CRITICAL"),
    "Token": (r"token\s*=\s*['\"].+['\"]", "HIGH"),
}

ALLOWED_CODE_EXTENSIONS = [
    ".py", ".js", ".ts", ".java", ".kt",
    ".env", ".yml", ".yaml", ".json",
    ".php", ".rb", ".go", ".cs"
]

EXCLUDED_DIRS = {"node_modules", ".git", "__pycache__", "venv", "dist", "build"}


def calculate_entropy(string):
    prob = [float(string.count(c)) / len(string) for c in dict.fromkeys(list(string))]
    entropy = -sum([p * math.log(p) / math.log(2.0) for p in prob])
    return entropy


def scan_project(project_path):
    findings = []

    for root, dirs, files in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

        for file in files:
            file_path = os.path.join(root, file)

            if any(file.lower().endswith(ext) for ext in ALLOWED_CODE_EXTENSIONS):
                try:
                    with open(file_path, "r", errors="ignore") as f:
                        lines = f.readlines()

                    for line_number, line in enumerate(lines, start=1):

                        for issue, (pattern, severity) in SUSPICIOUS_PATTERNS.items():
                            if re.search(pattern, line, re.IGNORECASE):
                                findings.append([
                                    datetime.now().isoformat(),
                                    issue,
                                    severity,
                                    file_path,
                                    line_number
                                ])

                        if "TODO" in line or "FIXME" in line:
                            findings.append([
                                datetime.now().isoformat(),
                                "TODO/FIXME Found",
                                "LOW",
                                file_path,
                                line_number
                            ])

                        secrets = re.findall(r"[A-Za-z0-9+/=]{20,}", line)
                        for secret in secrets:
                            if calculate_entropy(secret) > 4.5:
                                findings.append([
                                    datetime.now().isoformat(),
                                    "High Entropy Secret",
                                    "HIGH",
                                    file_path,
                                    line_number
                                ])

                except Exception:
                    pass

    return findings


def save_csv_report(findings):
    os.makedirs(BACKUP_DIR, exist_ok=True)

    filename = f"security_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    full_path = os.path.join(BACKUP_DIR, filename)

    with open(full_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Timestamp", "Issue Type", "Severity", "File Path", "Line"])
        writer.writerows(findings)

    print(f"\n[+] CSV Report saved to: {full_path}")


if __name__ == "__main__":
    project_folder = input("Enter full project path to scan: ").strip()

    if not os.path.exists(project_folder):
        print("Invalid path.")
    else:
        print("Scanning project...")
        results = scan_project(project_folder)
        save_csv_report(results)
