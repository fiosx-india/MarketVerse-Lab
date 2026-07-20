"""
MarketVerse Lab
mold_inspector.py

Purpose:
Inspect mold files and generate inspection reports.
"""

from pathlib import Path


class MoldInspector:

    def __init__(self):
        self.guardian = None
        self.last_report = {}

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def inspect(self, file_path):
        path = Path(file_path)

        self.last_report = {
            "file": str(path),
            "exists": path.exists(),
            "extension": path.suffix.lower(),
            "readable": path.exists(),
            "status": "PASS" if path.exists() else "FAIL"
        }

        return self.last_report

    def report(self):
        return self.last_report

    def is_ready(self):
        return True
