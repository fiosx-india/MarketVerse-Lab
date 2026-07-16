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

        self.patterns = [
            "*.bak",
            "*.old",
            "*.tmp",
            "*.copy",
            "*.pyc",
            "*.log",
        ]

    def scan(self):

        unwanted = []
        pycache = []

        for pattern in self.patterns:
            unwanted.extend(self.project_root.rglob(pattern))

        pycache = list(
            self.project_root.rglob("__pycache__")
        )

        self.report_data = {

            "status": "PASS",

            "unwanted_files": len(unwanted),

            "pycache_folders": len(pycache),

            "recommended_cleanup":
                len(unwanted) + len(pycache),

            "sample_files": [
                str(f)
                for f in unwanted[:10]
            ],

            "sample_folders": [
                str(f)
                for f in pycache[:10]
            ],

            "auto_cleanup": False

        }

        return self.report_data

    def report(self):

        return self.report_data

    def connect_blueprint(self, blueprint):

        self.blueprint = blueprint

    def connect_mapper(self, mapper):

        self.mapper = mapper

    def connect_locator(self, locator):

        self.locator = locator

    def connect_dependency_graph(self, dependency_graph):

        self.dependency_graph = dependency_graph

    def is_ready(self):

        return True
