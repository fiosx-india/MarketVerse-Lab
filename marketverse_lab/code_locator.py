"""
MarketVerse Lab
code_locator.py

Purpose:
Locate the exact location where a new
code block should be inserted.
"""

from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional
from .project_blueprint import ProjectBlueprint
from .project_mapper import ProjectMapper
from .dependency_graph import DependencyGraph
from .integration_checker import IntegrationChecker
from .error_intelligence import ErrorIntelligence
from .knowledge_base import KnowledgeBase

@dataclass
class LocationResult:

    file: str
    line: int
    score: float
    reason: str


class CodeLocator:

    def __init__(self):

        self.blueprint = None
        self.mapper = None

        # Future Connections
        self.dependency_graph = None
        self.integration_checker = None
        self.error_intelligence = None
        self.knowledge_base = None
        self.test_runner = None
        self.release_checker = None

        self.results = []

    # ----------------------------------------

    def connect_blueprint(self, blueprint):

        self.blueprint = blueprint

    # ----------------------------------------

    def connect_mapper(self, mapper):

        self.mapper = mapper

    # ----------------------------------------

    def clear(self):

        self.results.clear()

    # ----------------------------------------

    def scan_project(self):

        if self.mapper is None:
            return False

        self.mapper.build()

        return True

    # ----------------------------------------
    # Find by File Name
    # ----------------------------------------

    def find_file(self, filename):

        self.clear()

        if self.mapper is None:
            return []

        for path, node in self.mapper.files.items():

            if filename.lower() in node.name.lower():

                self.results.append(
                    LocationResult(
                        file=path,
                        line=1,
                        score=100.0,
                        reason="File name matched"
                    )
                )

        return self.results

    # ----------------------------------------
    # Find by Keyword
    # ----------------------------------------

    def find_keyword(self, keyword):

        self.clear()

        if self.mapper is None:
            return []

        for path in self.mapper.files.keys():

            file_path = Path(self.mapper.root) / path

            try:
                text = file_path.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )

                if keyword in text:

                    self.results.append(
                        LocationResult(
                            file=path,
                            line=text.count("\n", 0, text.find(keyword)) + 1,
                            score=95.0,
                            reason=f"Keyword '{keyword}' found"
                        )
                    )

            except Exception:
                continue

        return self.results

    # ----------------------------------------
    # Best Match
    # ----------------------------------------

    def best_match(self):

        if not self.results:
            return None

        return max(
            self.results,
            key=lambda item: item.score
        )

    # ----------------------------------------
    # Find Class
    # ----------------------------------------

    def find_class(self, class_name):

        return self.find_keyword(f"class {class_name}")

    # ----------------------------------------
    # Find Function
    # ----------------------------------------

    def find_function(self, function_name):

        return self.find_keyword(f"def {function_name}")

    # ----------------------------------------
    # Suggest Insert Location
    # ----------------------------------------

    def suggest_insert(self, keyword):

        matches = self.find_keyword(keyword)

        if not matches:
            return None

        best = self.best_match()

        return {
            "file": best.file,
            "line": best.line + 1,
            "action": "INSERT_AFTER",
            "reason": best.reason
        }

    # ----------------------------------------
    # Suggest Replace Location
    # ----------------------------------------

    def suggest_replace(self, keyword):

        matches = self.find_keyword(keyword)

        if not matches:
            return None

        best = self.best_match()

        return {
            "file": best.file,
            "line": best.line,
            "action": "REPLACE",
            "reason": best.reason
        }

    # ----------------------------------------
    # Complete Search
    # ----------------------------------------

    def locate(self, target):

        result = self.find_file(target)

        if result:
            return self.best_match()

        result = self.find_class(target)

        if result:
            return self.best_match()

        result = self.find_function(target)

        if result:
            return self.best_match()

        result = self.find_keyword(target)

        if result:
            return self.best_match()

        return None

    # ----------------------------------------
    # Diagnostics
    # ----------------------------------------

    def diagnostics(self):

        return {
            "connected_blueprint": self.blueprint is not None,
            "connected_mapper": self.mapper is not None,
            "matches_found": len(self.results),
            "last_match": (
                self.results[-1].file
                if self.results else None
            )
        }

    # ----------------------------------------
    # Confidence Score
    # ----------------------------------------

    def confidence(self):

        if not self.results:
            return 0.0

        return max(result.score for result in self.results)

    # ----------------------------------------
    # Complete Report
    # ----------------------------------------

    def report(self):

        return {
            "diagnostics": self.diagnostics(),
            "confidence": self.confidence(),
            "results": [
                {
                    "file": r.file,
                    "line": r.line,
                    "score": r.score,
                    "reason": r.reason
                }
                for r in self.results
            ]
        }

    # ----------------------------------------
    # Reset
    # ----------------------------------------

    def reset(self):

        self.results.clear()

        return True

    # ----------------------------------------
    # String Representation
    # ----------------------------------------

    def __str__(self):

        return (
            f"CodeLocator("
            f"Matches={len(self.results)}, "
            f"Confidence={self.confidence():.1f})"
        )

    __repr__ = __str__
