"""
MarketVerse Lab
error_intelligence.py

Purpose:
AI-powered error detection, analysis,
classification and recovery engine.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Dict
from .project_blueprint import ProjectBlueprint
from .project_mapper import ProjectMapper
from .code_locator import CodeLocator
from .dependency_graph import DependencyGraph
from .integration_checker import IntegrationChecker

@dataclass
class ErrorRecord:

    file: str
    line: int
    error_type: str
    severity: str
    message: str
    suggestion: str = ""
    auto_fixable: bool = False


class ErrorIntelligence:

    def __init__(self):

        self.blueprint = None
        self.mapper = None
        self.code_locator = None
        self.dependency_graph = None
        self.integration_checker = None

        # Future Connections
        self.knowledge_base = None
        self.test_runner = None
        self.release_checker = None
        self.auto_fixer = None

        self.errors = []

    # ----------------------------------------

    def connect_blueprint(self, blueprint):

        self.blueprint = blueprint

    # ----------------------------------------

    def connect_mapper(self, mapper):

        self.mapper = mapper

    # ----------------------------------------

    def connect_locator(self, locator):

        self.code_locator = locator

    # ----------------------------------------

    def connect_dependency_graph(self, graph):

        self.dependency_graph = graph

    # ----------------------------------------

    def connect_integration_checker(self, checker):

        self.integration_checker = checker

    # ----------------------------------------

    def clear(self):

        self.errors.clear()

        return True

    # ----------------------------------------
    # Register Error
    # ----------------------------------------

    def register(
        self,
        file,
        line,
        error_type,
        severity,
        message,
        suggestion="",
        auto_fixable=False
    ):

        self.errors.append(

            ErrorRecord(
                file=file,
                line=line,
                error_type=error_type,
                severity=severity,
                message=message,
                suggestion=suggestion,
                auto_fixable=auto_fixable
            )

        )

    # ----------------------------------------
    # Syntax Error
    # ----------------------------------------

    def syntax_error(
        self,
        file,
        line,
        message
    ):

        self.register(
            file=file,
            line=line,
            error_type="SyntaxError",
            severity="HIGH",
            message=message,
            suggestion="Check Python syntax.",
            auto_fixable=False
        )

    # ----------------------------------------
    # Import Error
    # ----------------------------------------

    def import_error(
        self,
        file,
        line,
        module
    ):

        self.register(
            file=file,
            line=line,
            error_type="ImportError",
            severity="HIGH",
            message=f"Missing module: {module}",
            suggestion=f"Import or install '{module}'.",
            auto_fixable=True
        )

    # ----------------------------------------
    # Indentation Error
    # ----------------------------------------

    def indentation_error(
        self,
        file,
        line
    ):

        self.register(
            file=file,
            line=line,
            error_type="IndentationError",
            severity="HIGH",
            message="Invalid indentation.",
            suggestion="Correct the indentation.",
            auto_fixable=False
        )

    # ----------------------------------------
    # File Missing
    # ----------------------------------------

    def file_missing(
        self,
        file
    ):

        self.register(
            file=file,
            line=0,
            error_type="FileNotFound",
            severity="CRITICAL",
            message="Required file not found.",
            suggestion="Create or restore the file.",
            auto_fixable=False
        )

    # ----------------------------------------
    # Module Missing
    # ----------------------------------------

    def module_missing(
        self,
        file,
        module
    ):

        self.register(
            file=file,
            line=0,
            error_type="ModuleMissing",
            severity="MEDIUM",
            message=f"Module '{module}' not found.",
            suggestion="Verify project structure.",
            auto_fixable=True
        )

    # ----------------------------------------
    # Wrong File Detection
    # ----------------------------------------

    def wrong_file(
        self,
        current_file,
        expected_file,
        line=0
    ):

        self.register(
            file=current_file,
            line=line,
            error_type="WrongFile",
            severity="HIGH",
            message=(
                f"Code belongs in '{expected_file}', "
                f"not '{current_file}'."
            ),
            suggestion=(
                f"Move the code to '{expected_file}'."
            ),
            auto_fixable=True
        )

    # ----------------------------------------
    # Wrong Position Detection
    # ----------------------------------------

    def wrong_position(
        self,
        file,
        line,
        expected_line
    ):

        self.register(
            file=file,
            line=line,
            error_type="WrongPosition",
            severity="HIGH",
            message=(
                f"Code inserted at line {line}."
            ),
            suggestion=(
                f"Move it near line {expected_line}."
            ),
            auto_fixable=True
        )

    # ----------------------------------------
    # Integration Error
    # ----------------------------------------

    def integration_error(
        self,
        file,
        message
    ):

        self.register(
            file=file,
            line=0,
            error_type="IntegrationError",
            severity="CRITICAL",
            message=message,
            suggestion="Review module integration.",
            auto_fixable=False
        )

    # ----------------------------------------
    # Connection Validation
    # ----------------------------------------

    def validate_connections(self):

        missing = []

    if self.blueprint is None:
        missing.append("ProjectBlueprint")

    if self.mapper is None:
        missing.append("ProjectMapper")

    if self.code_locator is None:
        missing.append("CodeLocator")

    if self.dependency_graph is None:
        missing.append("DependencyGraph")

    if self.integration_checker is None:
        missing.append("IntegrationChecker")

    if missing:

        self.register(
            file="SYSTEM",
            line=0,
            error_type="ConnectionError",
            severity="CRITICAL",
            message=f"Missing connections: {', '.join(missing)}",
            suggestion="Connect missing modules before execution.",
            auto_fixable=False
        )

    return {
        "success": len(missing) == 0,
        "missing": missing
    }

    # ----------------------------------------
    # Priority Sort
    # ----------------------------------------

    def priority(self):

        order = {
            "CRITICAL": 4,
            "HIGH": 3,
            "MEDIUM": 2,
            "LOW": 1
        }

        return sorted(
            self.errors,
            key=lambda e: order.get(
                e.severity,
                0
            ),
            reverse=True
        )

    # ----------------------------------------
    # Auto Fix Candidates
    # ----------------------------------------

    def auto_fix_candidates(self):

        return [
            error
            for error in self.errors
            if error.auto_fixable
        ]

    # ----------------------------------------
    # Error Count
    # ----------------------------------------

    def count(self):

        return len(self.errors)

    # ----------------------------------------
    # Statistics
    # ----------------------------------------

    def statistics(self):

        stats = {
            "total": len(self.errors),
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0
        }

        for error in self.errors:

            level = error.severity.lower()

            if level in stats:
                stats[level] += 1

        return stats

    # ----------------------------------------
    # AI Recommendation
    # ----------------------------------------

    def recommendations(self):

        recommendations = []

        for error in self.priority():

            recommendations.append({
                "file": error.file,
                "line": error.line,
                "type": error.error_type,
                "suggestion": error.suggestion,
                "auto_fixable": error.auto_fixable
            })

        return recommendations

    # ----------------------------------------
    # Full Report
    # ----------------------------------------

    def report(self):

        return {
            "statistics": self.statistics(),
            "recommendations": self.recommendations(),
            "auto_fix_candidates": len(
                self.auto_fix_candidates()
            )
        }

    # ----------------------------------------
    # Diagnostics
    # ----------------------------------------

    def diagnostics(self):

        return {
            "blueprint": self.blueprint is not None,
            "mapper": self.mapper is not None,
            "locator": self.code_locator is not None,
            "dependency_graph": self.dependency_graph is not None,
            "integration_checker": self.integration_checker is not None,
            "errors": len(self.errors)
        }

    # ----------------------------------------
    # Ready
    # ----------------------------------------

    def is_ready(self):

        return (

            self.blueprint is not None
            and self.mapper is not None
            and self.code_locator is not None
            and self.dependency_graph is not None
            and self.integration_checker is not None

        )

    # ----------------------------------------
    # Reset
    # ----------------------------------------

    def reset(self):

        self.errors.clear()

        return True

    # ----------------------------------------
    # Future AI Hook
    # ----------------------------------------

    def ai_review(self):

        """
        Reserved for future AI review engine.
        """

        return {
            "status": "READY"
        }

    # ----------------------------------------
    # String
    # ----------------------------------------

    def __str__(self):

        return (
            f"ErrorIntelligence("
            f"errors={len(self.errors)})"
        )

    __repr__ = __str__
