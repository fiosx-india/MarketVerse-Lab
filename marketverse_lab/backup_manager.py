"""
MarketVerse Lab
backup_manager.py

Purpose:
Create and manage project backups before applying changes.
"""

from copy import deepcopy
from datetime import datetime


class BackupManager:

    def __init__(self):
        self.guardian = None
        self.backups = {}

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def create_backup(self, file_name, data=None):

        backup = {
            "file": file_name,
            "timestamp": datetime.now().isoformat(),
            "data": deepcopy(data),
        }

        self.backups[file_name] = backup

        return {
            "status": "SUCCESS",
            "backup_created": True,
            "backup": backup,
        }

    def restore_backup(self, file_name):

        if file_name not in self.backups:
            return {
                "status": "FAILED",
                "reason": "Backup not found",
            }

        return {
            "status": "READY",
            "backup": self.backups[file_name],
        }

    def delete_backup(self, file_name):

        if file_name in self.backups:
            del self.backups[file_name]

        return {
            "status": "SUCCESS"
        }

    def list_backups(self):

        return {
            "count": len(self.backups),
            "files": list(self.backups.keys()),
        }

    def report(self):

        return {
            "connected": self.guardian is not None,
            "backup_count": len(self.backups),
        }

    def is_ready(self):
        return self.guardian is not None

    def __str__(self):
        return "BackupManager"

    __repr__ = __str__
