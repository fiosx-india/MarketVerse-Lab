"""
File Registry

Purpose:
Register every project file and provide
a searchable file inventory.
"""

from pathlib import Path
from datetime import datetime


class FileRegistry:

    def __init__(self):

        self.project_root = Path(".")
        self.files = []

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

        self.allowed_extensions = {
            ".py",
            ".json",
            ".yaml",
            ".yml",
            ".md",
            ".txt",
        }

    def scan(self):

        self.files = []

        for file in self.project_root.rglob("*"):

            if any(folder in file.parts for folder in self.ignore_dirs):
                continue

            if not file.is_file():
                continue

            if file.suffix.lower() not in self.allowed_extensions:
                continue

            stat = file.stat()

            self.files.append({

                "name": file.name,
                "path": str(file.relative_to(self.project_root)),
                "suffix": file.suffix,
                "size": stat.st_size,
                "modified": datetime.fromtimestamp(
                    stat.st_mtime
                ).isoformat()

            })

        self.files.sort(
            key=lambda x: x["path"]
        )

        return self.files

    def report(self):

        return {

            "status": "PASS",
            "total_files": len(self.files)

        }

    def find(self, filename):

        for file in self.files:

            if file["name"] == filename:
                return file

        return None

    def list_files(self):

        return self.files

    # ----------------------------------------
    # Guardian Connections
    # ----------------------------------------

    def connect_blueprint(self, blueprint):
        self.blueprint = blueprint

    def connect_mapper(self, mapper):
        self.mapper = mapper

    def connect_locator(self, locator):
        self.locator = locator

    def connect_dependency_graph(self, dependency_graph):
        self.dependency_graph = dependency_graph

    # ----------------------------------------
    # Ready Status
    # ----------------------------------------

    def is_ready(self):
        return True
