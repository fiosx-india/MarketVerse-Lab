"""
MarketVerse Guardian
file_analyzer.py

Purpose:
Analyze a single Python file by coordinating
existing Guardian components.
"""

from pathlib import Path

from .validator import ProjectValidator
from .dependency import DependencyAnalyzer
from .import_checker import ImportChecker


class FileAnalyzer:
    """Analyze a single project file."""

    def __init__(self):

        self.validator = ProjectValidator()
        self.dependency = DependencyAnalyzer()
        self.import_checker = ImportChecker()

    def analyze(self, file_path):

        file_path = Path(file_path)

        report = {
            "file": str(file_path),
            "exists": file_path.exists(),
            "validation": None,
            "imports": [],
            "import_check": {},
            "status": "OK"
        }

        if not file_path.exists():

            report["status"] = "ERROR"

            report["message"] = "File not found."

            return report

        # Validation
        validation = self.validator.validate(file_path)

        report["validation"] = validation

        if not validation.valid:
            report["status"] = "ERROR"

        # Dependency Analysis
        imports = self.dependency.analyze(file_path)

        report["imports"] = imports

        # Import Check
        report["import_check"] = self.import_checker.check(imports)

        if not report["import_check"]["success"]:
            report["status"] = "WARNING"

        return report
