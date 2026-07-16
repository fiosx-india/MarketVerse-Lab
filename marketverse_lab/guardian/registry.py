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

    def scan(self):

        self.files = []

        for file in self.project_root.rglob("*"):

            if file.is_file():

                stat = file.stat()

                self.files.append({
                    "name": file.name,
                    "path": str(file),
                    "suffix": file.suffix,
                    "size": stat.st_size,
                    "modified": datetime.fromtimestamp(
                        stat.st_mtime
                    ).isoformat()
                })

        return self.files

    def report(self):

        return {
            "status": "PASS",
            "total_files": len(self.files),
            "files": self.files
        }

    def find(self, filename):

        for file in self.files:
            if file["name"] == filename:
                return file

        return None

    def is_ready(self):
        return True
