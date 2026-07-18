"""
MarketVerse Lab
snapshot_manager.py

Purpose:
Create complete project snapshots before major changes.
"""

from datetime import datetime


class SnapshotManager:

    def __init__(self):
        self.guardian = None
        self.snapshots = []

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def create_snapshot(self, name="Snapshot"):

        snapshot = {
            "name": name,
            "time": datetime.now().isoformat()
        }

        if hasattr(self.guardian, "backup_manager"):
            self.guardian.backup_manager.create_backup(name)

        if hasattr(self.guardian, "version_manager"):
            self.guardian.version_manager.create_version(name)

        self.snapshots.append(snapshot)

        return {
            "status": "SUCCESS",
            "snapshot": snapshot
        }

    def list_snapshots(self):
        return {
            "count": len(self.snapshots),
            "snapshots": self.snapshots
        }

    def report(self):
        return {
            "connected": self.guardian is not None,
            "snapshot_count": len(self.snapshots)
        }

    def is_ready(self):
        return self.guardian is not None

    def __str__(self):
        return "SnapshotManager"

    __repr__ = __str__
