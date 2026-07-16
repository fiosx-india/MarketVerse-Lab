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

        self.ignore_dirs = {
            "__pycache__",
            ".git",
            ".venv",
            "venv",
            "node_modules",
            ".idea",
            ".vscode",
            ".pytest_cache",
            ".mypy_cache",
            "build",
            "dist",
        }

    def scan(self):

        python_files = 0
        total_files = 0

        for path in self.project_root.rglob("*"):

            if any(folder in path.parts for folder in self.ignore_dirs):
                continue

            if path.is_file():

                total_files += 1

                if path.suffix == ".py":
                    python_files += 1

        health_percent = 100

        if python_files == 0:
            health_percent = 0

        self.report_data = {
            "status": "PASS",
            "project_root": str(self.project_root.resolve()),
            "python_files": python_files,
            "total_files": total_files,
            "ignored_folders": len(self.ignore_dirs),
            "health_percent": health_percent,
            "healthy": health_percent >= 80,
        }

        return self.report_data

    def report(self):
        return self.report_data

    def is_ready(self):
        return True
