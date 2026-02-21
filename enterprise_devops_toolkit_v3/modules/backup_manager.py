import shutil
import os
import logging
from datetime import datetime

def create_backup(source_folder):
    if not os.path.exists("backups"):
        os.makedirs("backups")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backups/backup_{timestamp}"

    try:
        shutil.make_archive(backup_name, 'zip', source_folder)
        logging.info(f"Backup created: {backup_name}.zip")
        return f"{backup_name}.zip"
    except Exception as e:
        logging.error(f"Backup failed: {str(e)}")
        return None
