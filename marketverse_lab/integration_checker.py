"""
MarketVerse Lab
integration_checker.py

Purpose:
Validate and verify module integration
before applying changes.
"""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class IntegrationResult:

    success: bool
    score: float
    messages: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    required_files: List[str] = field(default_factory=list)


class IntegrationChecker:

    def __init__(self):

        self.blueprint = None
        self.mapper = None
        self.code_locator = None
        self.dependency_graph = None

        # Future Connections
        self.error_intelligence = None
        self.knowledge_base = None
        self.test_runner = None
        self.release_checker = None

        self.history = []

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

    def reset(self):

        self.history.clear()

        return True

    # ----------------------------------------
    # Validate Integration
    # ----------------------------------------

    def validate(self, target_file):

        result = IntegrationResult(
            success=True,
            score=100.0
        )

        # File Exists
        if self.mapper is None:

            result.success = False
            result.score = 0.0
            result.messages.append(
                "ProjectMapper is not connected."
            )

            return result

        if target_file not in self.mapper.files:

            result.success = False
            result.score = 0.0
            result.messages.append(
                f"{target_file} not found."
            )

            return result

        result.messages.append(
            "Target file found."
        )

        return result

    # ----------------------------------------
    # Compatibility Check
    # ----------------------------------------

    def check_compatibility(
        self,
        source_module,
        target_file
    ):

        result = self.validate(target_file)

        if not result.success:
            return result

        result.messages.append(
            f"{source_module} is compatible."
        )

        result.score += 5

        if result.score > 100:
            result.score = 100

        return result

    # ----------------------------------------
    # Required Files
    # ----------------------------------------

    def required_files(
        self,
        target_file
    ):

        if self.dependency_graph is None:
            return []

        affected = self.dependency_graph.impact(
            target_file
        )

        return affected

    # ----------------------------------------
    # Integration Score
    # ----------------------------------------

    def integration_score(
        self,
        target_file
    ):

        result = self.validate(target_file)

        return result.score

    # ----------------------------------------
    # Auto Import Check
    # ----------------------------------------

    def check_imports(self, target_file):

        report = {
            "status": True,
            "missing": [],
            "existing": []
        }

        if self.dependency_graph is None:
            report["status"] = False
            return report

        dependencies = self.dependency_graph.dependencies_of(target_file)

        for module in dependencies:

            if module in self.dependency_graph.nodes:
                report["existing"].append(module)
            else:
                report["missing"].append(module)

        if report["missing"]:
            report["status"] = False

        return report

    # ----------------------------------------
    # Missing Module Detection
    # ----------------------------------------

    def detect_missing_modules(self):

        if self.dependency_graph is None:
            return {}

        return self.dependency_graph.missing_dependencies()

    # ----------------------------------------
    # Integration Warnings
    # ----------------------------------------

    def warnings(self, target_file):

        warnings = []

        imports = self.check_imports(target_file)

        if imports["missing"]:
            warnings.append(
                f"{len(imports['missing'])} missing dependencies detected."
            )

        affected = self.required_files(target_file)

        if len(affected) > 0:
            warnings.append(
                f"{len(affected)} related files may require updates."
            )

        return warnings

    # ----------------------------------------
    # Safe Insert Recommendation
    # ----------------------------------------

    def recommend_insert(self, keyword):

        if self.code_locator is None:
            return None

        suggestion = self.code_locator.suggest_insert(keyword)

        if suggestion is None:
            return None

        return {
            "status": "SAFE",
            "file": suggestion["file"],
            "line": suggestion["line"],
            "action": suggestion["action"],
            "reason": suggestion["reason"]
        }

    # ----------------------------------------
    # Full Integration Analysis
    # ----------------------------------------

    def analyze(self, target_file):

        result = self.validate(target_file)

        analysis = {
            "validation": result,
            "warnings": self.warnings(target_file),
            "imports": self.check_imports(target_file),
            "affected_files": self.required_files(target_file)
        }

        self.history.append(analysis)

        return analysis

    # ----------------------------------------
    # Diagnostics
    # ----------------------------------------

    def diagnostics(self):

        return {
            "blueprint_connected": self.blueprint is not None,
            "mapper_connected": self.mapper is not None,
            "locator_connected": self.code_locator is not None,
            "dependency_graph_connected": self.dependency_graph is not None,
            "history_count": len(self.history)
        }

    # ----------------------------------------
    # Statistics
    # ----------------------------------------

    def statistics(self):

        total = len(self.history)

        success = sum(
            1
            for item in self.history
            if item["validation"].success
        )

        failed = total - success

        return {
            "total_checks": total,
            "successful": success,
            "failed": failed
        }

    # ----------------------------------------
    # Export History
    # ----------------------------------------

    def export_history(self):

        exported = []

        for item in self.history:

            exported.append({
                "success": item["validation"].success,
                "score": item["validation"].score,
                "warnings": item["warnings"],
                "affected_files": item["affected_files"]
            })

        return exported

    # ----------------------------------------
    # Complete Report
    # ----------------------------------------

    def report(self):

        return {
            "diagnostics": self.diagnostics(),
            "statistics": self.statistics(),
            "history": self.export_history()
        }

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):

        return (
            self.blueprint is not None and
            self.mapper is not None and
            self.code_locator is not None and
            self.dependency_graph is not None
        )

    # ----------------------------------------
    # String Representation
    # ----------------------------------------

    def __str__(self):

        stats = self.statistics()

        return (
            f"IntegrationChecker("
            f"Checks={stats['total_checks']}, "
            f"Success={stats['successful']}, "
            f"Failed={stats['failed']})"
        )

    __repr__ = __str__
