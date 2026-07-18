"""
MarketVerse Lab
version_manager.py

Purpose:
Manage project versions.
"""

from datetime import datetime


class VersionManager:

    def __init__(self):
        self.guardian = None
        self.versions = []

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def create_version(self, name):

        version = {
            "name": name,
            "created": datetime.now().isoformat()
        }

        self.versions.append(version)

        return {
            "status": "SUCCESS",
            "version": version
        }

    def list_versions(self):
        return self.versions

    def latest(self):
        if self.versions:
            return self.versions[-1]
        return {}

    def report(self):
        return {
            "connected": self.guardian is not None,
            "version_count": len(self.versions)
        }

    def is_ready(self):
        return self.guardian is not None

    def __str__(self):
        return "VersionManager"

    __repr__ = __str__
