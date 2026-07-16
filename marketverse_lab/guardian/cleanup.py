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

    unwanted = []
    pycache = []

    for pattern in self.patterns:
        for file in self.project_root.rglob(pattern):
            if any(folder in file.parts for folder in self.ignore_dirs):
                continue
            unwanted.append(file)

    for folder in self.project_root.rglob("__pycache__"):
        if any(ignore in folder.parts for ignore in self.ignore_dirs):
            continue
        pycache.append(folder)

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
