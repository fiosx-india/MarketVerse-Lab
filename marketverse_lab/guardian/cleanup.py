"""
Cleanup Engine

Purpose:
Detect unwanted files and keep the project clean.
"""

from pathlib import Path


class CleanupEngine:

    def __init__(self):
        self.project_root = Path(".")
        self.report_data = {}

    def scan(self):

        unwanted = []

        patterns = [
            "*.bak",
            "*.old",
            "*.tmp",
            "*.copy",
            "*.pyc"
        ]

        for pattern in patterns:
            unwanted.extend(self.project_root.rglob(pattern))

        pycache = list(self.project_root.rglob("__pycache__"))

        self.report_data = {
            "status": "PASS",
            "unwanted_files": len(unwanted),
            "pycache_folders": len(pycache),
            "files": [str(f) for f in unwanted],
            "folders": [str(f) for f in pycache],
        }

        return self.report_data

    def report(self):
        return self.report_data

    def is_ready(self):
        return True
