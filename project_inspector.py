"""
MarketVerse Lab
project_inspector.py

AI Project Inspector
"""

from pathlib import Path
from datetime import datetime
import ast


class ProjectInspector:

    def __init__(self):

        self.root = None

        self.files = 0

        self.critical = []
        self.warnings = []
        self.recommendations = []

        self.statistics_data = {}
        self.last_scan = None

    # --------------------------------------------------

    def inspect(self, root="."):

        self.reset()

        self.root = Path(root).resolve()

        for file in self.root.rglob("*.py"):

            self.files += 1

            try:

                source = file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )

                if not source.strip():
                    self.warnings.append(
                        f"Empty file : {file.name}"
                    )

                if len(source.splitlines()) > 1000:
                    self.warnings.append(
                        f"Large file : {file.name}"
                    )

                ast.parse(source)

            except SyntaxError:

                self.critical.append(
                    f"Syntax error : {file.name}"
                )

            except Exception as e:

                self.critical.append(
                    f"{file.name} : {e}"
                )

        self.last_scan = str(datetime.now())

        self._generate_recommendations()

        self.statistics_data = {
            "python_files": self.files,
            "critical": len(self.critical),
            "warnings": len(self.warnings)
        }

        return self.report()

    # --------------------------------------------------

    def _generate_recommendations(self):

        if self.critical:
            self.recommendations.append(
                "Fix all critical issues."
            )

        if self.warnings:
            self.recommendations.append(
                "Review warning messages."
            )

        if not self.critical and not self.warnings:
            self.recommendations.append(
                "Project looks healthy."
            )

    # --------------------------------------------------

    def summary(self):

        return {
            "files": self.files,
            "critical": len(self.critical),
            "warnings": len(self.warnings)
        }

    # --------------------------------------------------

    def statistics(self):

        return self.statistics_data

    # --------------------------------------------------

    def diagnostics(self):

        return {
            "ready": self.is_ready(),
            "last_scan": self.last_scan
        }

    # --------------------------------------------------

    def report(self):

        return {
            "ready": self.is_ready(),
            "summary": self.summary(),
            "critical": self.critical,
            "warnings": self.warnings,
            "recommendations": self.recommendations,
            "statistics": self.statistics(),
            "diagnostics": self.diagnostics()
        }

    # --------------------------------------------------

    def reset(self):

        self.files = 0

        self.critical.clear()
        self.warnings.clear()
        self.recommendations.clear()

        self.statistics_data = {}
        self.last_scan = None

    # --------------------------------------------------

    def is_ready(self):

        return len(self.critical) == 0
