"""
MarketVerse Lab
import_analyzer.py

Purpose:
Analyze Python imports and
return dependency list.
"""

import ast
from pathlib import Path


class ImportAnalyzer:

    def __init__(self):

        self.total_files = 0
        self.total_imports = 0

    def analyze(self, file_path):

        imports = []

        file_path = Path(file_path)

        if not file_path.exists():
            return imports

        try:

            source = file_path.read_text(
                encoding="utf-8"
            )

            tree = ast.parse(source)

        except Exception:
            return imports

        self.total_files += 1

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for module in node.names:

                    imports.append(module.name)

            elif isinstance(node, ast.ImportFrom):

                if node.module:

                    imports.append(node.module)

        imports = sorted(
            list(set(imports))
        )

        self.total_imports += len(imports)

        return imports

    def statistics(self):

        return {

            "files_scanned": self.total_files,

            "imports_found": self.total_imports

        }

    def reset(self):

        self.total_files = 0
        self.total_imports = 0

        return True

    def report(self):

        return {

            "statistics": self.statistics()

        }

    def is_ready(self):

        return True

    def __str__(self):

        return (
            f"ImportAnalyzer("
            f"files={self.total_files}, "
            f"imports={self.total_imports})"
        )

    __repr__ = __str__
