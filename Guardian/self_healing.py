"""
MarketVerse Guardian
self_healing.py

Purpose:
Automatically recover from common project failures.
"""

from pathlib import Path
import shutil


class SelfHealing:

    def backup(self, file_path):
        file_path = Path(file_path)

        backup_path = file_path.with_suffix(file_path.suffix + ".bak")

        try:
            shutil.copy(file_path, backup_path)
            return {
                "status": "OK",
                "backup": str(backup_path)
            }

        except Exception as e:
            return {
                "status": "ERROR",
                "error": str(e)
            }

    def restore(self, file_path):
        file_path = Path(file_path)

        backup_path = file_path.with_suffix(file_path.suffix + ".bak")

        try:
            if backup_path.exists():
                shutil.copy(backup_path, file_path)

            return {
                "status": "RESTORED"
            }

        except Exception as e:
            return {
                "status": "ERROR",
                "error": str(e)
            }
