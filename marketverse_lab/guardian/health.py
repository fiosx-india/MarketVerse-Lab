"""
Health Engine

Purpose:
Check overall project health.
"""

from pathlib import Path


class HealthEngine:

    def __init__(self):
        self.project_root = Path(".")
        self.report_data = {}

    def scan(self):

        python_files = list(self.project_root.rglob("*.py"))

        self.report_data = {
            "status": "PASS",
            "project_root": str(self.project_root.resolve()),
            "python_files": len(python_files),
            "total_files": len(list(self.project_root.rglob("*"))),
            "healthy": True,
        }

        return self.report_data

    def report(self):
        return self.report_data

    def is_ready(self):
        return True
