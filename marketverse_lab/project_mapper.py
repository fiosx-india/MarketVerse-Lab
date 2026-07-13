"""
MarketVerse Lab
project_mapper.py

Purpose:
Maps the complete project structure and
categorizes folders, files and modules.
"""

from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class FileNode:

    name: str
    path: str
    file_type: str
    size: int = 0


@dataclass
class FolderNode:

    name: str
    path: str
    files: List[str] = field(default_factory=list)


class ProjectMapper:

    def __init__(self):

        self.root = None

        self.files = {}
        self.folders = {}

        # Future Connections
        self.blueprint = None
        self.code_locator = None
        self.dependency_graph = None
        self.integration_checker = None
        self.error_intelligence = None
        self.knowledge_base = None
        self.test_runner = None
        self.release_checker = None

        # AI Mapping Database
        self.class_index = {}
        self.function_index = {}
        self.import_index = {}

    # ----------------------------------------

    def connect_blueprint(self, blueprint):

        self.blueprint = blueprint
        return True

    # ----------------------------------------

    def scan(self, root="."):

        root = Path(root)

        self.root = root

        self.files.clear()
        self.folders.clear()

        return True

    # ----------------------------------------
    # Folder Mapping
    # ----------------------------------------

    def map_folders(self):

        for folder in self.root.rglob("*"):

            if folder.is_dir():

                relative = str(folder.relative_to(self.root))

                self.folders[relative] = FolderNode(
                    name=folder.name,
                    path=relative
                )

        return self.folders

    # ----------------------------------------
    # File Mapping
    # ----------------------------------------

    def map_files(self):

        for file in self.root.rglob("*"):

            if file.is_file():

                relative = str(file.relative_to(self.root))

                self.files[relative] = FileNode(
                    name=file.name,
                    path=relative,
                    file_type=file.suffix,
                    size=file.stat().st_size
                )

        return self.files

    # ----------------------------------------
    # Folder Relationships
    # ----------------------------------------

    def build_relationships(self):

        for path, node in self.files.items():

            parent = str(Path(path).parent)

            if parent in self.folders:
                self.folders[parent].files.append(path)

        return True

    # ----------------------------------------
    # Complete Mapping
    # ----------------------------------------

    def build(self, root="."):

        self.scan(root)

        self.map_folders()
        self.map_files()
        self.build_relationships()
        self.build_code_index()

        return True

    # ----------------------------------------
    # Statistics
    # ----------------------------------------

    def statistics(self):

        return {
            "folders": len(self.folders),
            "files": len(self.files),
            "python_files": len(
                [f for f in self.files.values() if f.file_type == ".py"]
            )
        }

    # ----------------------------------------
    # Find File
    # ----------------------------------------

    def find_file(self, filename):

        for path, node in self.files.items():

            if node.name == filename:
                return node

        return None

    # ----------------------------------------
    # Find Folder
    # ----------------------------------------

    def find_folder(self, foldername):

        for path, node in self.folders.items():

            if node.name == foldername:
                return node

        return None

    # ----------------------------------------
    # Export Mapping
    # ----------------------------------------

    def export(self):

        return {
            "folders": list(self.folders.keys()),
            "files": list(self.files.keys()),
            "statistics": self.statistics()
        }

    # ----------------------------------------
    # Validation
    # ----------------------------------------

    def validate(self):

        return {
            "root_found": self.root is not None,
            "folder_count": len(self.folders),
            "file_count": len(self.files),
            "mapping_complete":
                self.root is not None and
                len(self.files) > 0
        }

    # ----------------------------------------
    # Diagnostics
    # ----------------------------------------

    def diagnostics(self):

        return {
            "root": str(self.root) if self.root else None,
            "folders": len(self.folders),
            "files": len(self.files),
            "statistics": self.statistics(),
            "validation": self.validate()
        }

    # ----------------------------------------
    # Register Future Extension
    # ----------------------------------------

    def register_extension(self, name, extension):

        if not hasattr(self, "_extensions"):
            self._extensions = {}

        self._extensions[name] = extension

        return True

    # ----------------------------------------
    # Get Extension
    # ----------------------------------------

    def get_extension(self, name):

        if not hasattr(self, "_extensions"):
            return None

        return self._extensions.get(name)

    # ----------------------------------------
    # Generate Report
    # ----------------------------------------

    def report(self):

        return {
            "summary": self.statistics(),
            "diagnostics": self.diagnostics(),
            "folders": list(self.folders.keys()),
            "files": list(self.files.keys())
        }

    # ----------------------------------------
    # Reset Mapper
    # ----------------------------------------

    def reset(self):

        self.root = None
        self.files.clear()
        self.folders.clear()

        return True

    # ----------------------------------------
    # String Representation
    # ----------------------------------------

    def __str__(self):

        return (
            f"ProjectMapper("
            f"Folders={len(self.folders)}, "
            f"Files={len(self.files)})"
        )

    __repr__ = __str__

    # ----------------------------------------
    # Function List
    # ----------------------------------------

    def function_list(self, filename):

        import ast

        node = self.find_file(filename)

        if node is None or self.root is None:
            return []

        file_path = self.root / node.path

        try:

            with open(file_path, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read())

            functions = []

            for item in tree.body:

                if isinstance(item, ast.FunctionDef):
                    functions.append(item.name)

                elif isinstance(item, ast.ClassDef):

                    for member in item.body:

                        if isinstance(member, ast.FunctionDef):
                            functions.append(member.name)

            return functions

        
    def function_list(self):
        except Exception:
            return []

    # ----------------------------------------
    # Build Code Index
    # ----------------------------------------

    def build_code_index(self):
        return True


    # ----------------------------------------
    # Wrong File Detection
    # ----------------------------------------

    def find_wrong_files(self):

        return []

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):

        validation = self.validate()

        return validation["mapping_complete"]
