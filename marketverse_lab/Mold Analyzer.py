"""
MarketVerse Lab
mold_analyzer.py

Purpose:
Analyze mold files and generate analysis reports.
"""

from pathlib import Path


class MoldAnalyzer:

    def __init__(self):
        self.guardian = None
        self.last_report = {}

    def connect_guardian(self, guardian):
        self.guardian = guardian

    def analyze(self, file_path):

        path = Path(file_path)

        self.last_report = {
            "file": str(path),
            "exists": path.exists(),
            "extension": path.suffix.lower(),
            "size_bytes": path.stat().st_size if path.exists() else 0,
            "status": "Ready" if path.exists() else "File Not Found"
        }

        return self.last_report

    def report(self):
        return self.last_report

    def is_ready(self):
        return True
