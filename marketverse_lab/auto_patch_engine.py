"""
MarketVerse Lab
auto_patch_engine.py

Purpose:
Automatically apply safe code patches,
insertions, replacements and rollback.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List
from .change_planner import ChangePlanner
from .integration_checker import IntegrationChecker
from .error_intelligence import ErrorIntelligence
from .knowledge_base import KnowledgeBase
from .project_memory import ProjectMemory

@dataclass
class PatchResult:

    success: bool
    file: str
    action: str
    message: str


class AutoPatchEngine:

    def __init__(self):

        # Core Connections
        self.blueprint = None
        self.mapper = None
        self.locator = None
        self.dependency_graph = None
        self.integration_checker = None
        self.error_intelligence = None
        self.knowledge_base = None
        self.change_planner = None

        # Patch History
        self.history = []

    # ----------------------------------------

    def connect_blueprint(self, blueprint):

        self.blueprint = blueprint

    # ----------------------------------------

    def connect_mapper(self, mapper):

        self.mapper = mapper

    # ----------------------------------------

    def connect_locator(self, locator):

        self.locator = locator

    # ----------------------------------------

    def connect_dependency_graph(self, graph):

        self.dependency_graph = graph

    # ----------------------------------------

    def connect_integration_checker(self, checker):

        self.integration_checker = checker

    # ----------------------------------------

    def connect_error_intelligence(self, intelligence):

        self.error_intelligence = intelligence

    # ----------------------------------------

    def connect_knowledge_base(self, knowledge):

        self.knowledge_base = knowledge

    # ----------------------------------------

    def connect_change_planner(self, planner):

        self.change_planner = planner

    # ----------------------------------------

    def clear(self):

        self.history.clear()

        return True

    # ----------------------------------------
    # Create Patch
    # ----------------------------------------

    def create_patch(
        self,
        file,
        action,
        code
    ):

        return {
            "file": file,
            "action": action,
            "code": code
        }

    # ----------------------------------------
    # Backup File
    # ----------------------------------------

    def backup_file(self, file):

        path = Path(file)

        if not path.exists():

            return PatchResult(
                success=False,
                file=file,
                action="BACKUP",
                message="File not found."
            )

        backup = path.with_suffix(path.suffix + ".bak")

        backup.write_text(
            path.read_text(encoding="utf-8"),
            encoding="utf-8"
        )

        return PatchResult(
            success=True,
            file=file,
            action="BACKUP",
            message=str(backup)
        )

    # ----------------------------------------
    # Insert Code
    # ----------------------------------------

    def insert_code(
        self,
        file,
        line,
        code
    ):

        path = Path(file)

        if not path.exists():

            return PatchResult(
                False,
                file,
                "INSERT",
                "File not found."
            )

        lines = path.read_text(
            encoding="utf-8"
        ).splitlines()

        line = max(0, min(line, len(lines)))

        lines.insert(line, code)

        path.write_text(
            "\n".join(lines),
            encoding="utf-8"
        )

        return PatchResult(
            True,
            file,
            "INSERT",
            f"Inserted at line {line}"
        )

    # ----------------------------------------
    # Replace Code
    # ----------------------------------------

    def replace_code(
        self,
        file,
        old_text,
        new_text
    ):

        path = Path(file)

        if not path.exists():

            return PatchResult(
                False,
                file,
                "REPLACE",
                "File not found."
            )

        content = path.read_text(
            encoding="utf-8"
        )

        if old_text not in content:

            return PatchResult(
                False,
                file,
                "REPLACE",
                "Target text not found."
            )

        content = content.replace(
            old_text,
            new_text,
            1
        )

        path.write_text(
            content,
            encoding="utf-8"
        )

        return PatchResult(
            True,
            file,
            "REPLACE",
            "Replacement completed."
        )

    # ----------------------------------------
    # Add Import
    # ----------------------------------------

    def add_import(
        self,
        file,
        import_line
    ):

        return self.insert_code(
            file=file,
            line=0,
            code=import_line
        )

    # ----------------------------------------
    # Smart Insert
    # ----------------------------------------

    def smart_insert(
        self,
        file,
        keyword,
        code
    ):

        if self.locator is None:

            return PatchResult(
                False,
                file,
                "SMART_INSERT",
                "CodeLocator not connected."
            )

        suggestion = self.locator.suggest_insert(
            keyword
        )

        if suggestion is None:

            return PatchResult(
                False,
                file,
                "SMART_INSERT",
                "No insertion point found."
            )

        return self.insert_code(
            file=file,
            line=suggestion["line"],
            code=code
        )

    # ----------------------------------------
    # Replace Function
    # ----------------------------------------

    def replace_function(
        self,
        file,
        function_name,
        new_code
    ):

        path = Path(file)

        if not path.exists():

            return PatchResult(
                False,
                file,
                "FUNCTION_REPLACE",
                "File not found."
            )

        content = path.read_text(
            encoding="utf-8"
        )

        marker = f"def {function_name}("

        if marker not in content:

            return PatchResult(
                False,
                file,
                "FUNCTION_REPLACE",
                "Function not found."
            )

        return PatchResult(
            True,
            file,
            "FUNCTION_REPLACE",
            "Function replacement ready."
        )

    # ----------------------------------------
    # Verify Patch
    # ----------------------------------------

    def verify_patch(
        self,
        file
    ):

        if self.integration_checker is None:

            return {
                "success": False,
                "message": "IntegrationChecker not connected."
            }

        result = self.integration_checker.validate(
            file
        )

        return {
            "success": result.success,
            "score": result.score,
            "messages": result.messages
        }

    # ----------------------------------------
    # Rollback
    # ----------------------------------------

    def rollback(
        self,
        file
    ):

        path = Path(file)

        backup = path.with_suffix(
            path.suffix + ".bak"
        )

        if not backup.exists():

            return PatchResult(
                False,
                file,
                "ROLLBACK",
                "Backup not found."
            )

        path.write_text(
            backup.read_text(
                encoding="utf-8"
            ),
            encoding="utf-8"
        )

        return PatchResult(
            True,
            file,
            "ROLLBACK",
            "Rollback completed."
        )

    # ----------------------------------------
    # Save History
    # ----------------------------------------

    def save_history(
        self,
        result
    ):

        self.history.append(result)

        return len(self.history)

    # ----------------------------------------
    # Statistics
    # ----------------------------------------

    def statistics(self):

        successful = sum(
            1
            for item in self.history
            if getattr(item, "success", False)
        )

        failed = len(self.history) - successful

        return {
            "total_patches": len(self.history),
            "successful": successful,
            "failed": failed
        }

    # ----------------------------------------
    # Diagnostics
    # ----------------------------------------

    def diagnostics(self):

        return {
            "blueprint_connected":
                self.blueprint is not None,
            "mapper_connected":
                self.mapper is not None,
            "locator_connected":
                self.locator is not None,
            "dependency_graph_connected":
                self.dependency_graph is not None,
            "integration_checker_connected":
                self.integration_checker is not None,
            "error_intelligence_connected":
                self.error_intelligence is not None,
            "knowledge_base_connected":
                self.knowledge_base is not None,
            "change_planner_connected":
                self.change_planner is not None,
            "history_count":
                len(self.history)
        }

    # ----------------------------------------
    # Patch Report
    # ----------------------------------------

    def report(self):

        return {
            "statistics": self.statistics(),
            "diagnostics": self.diagnostics(),
            "history": [
                {
                    "file": item.file,
                    "action": item.action,
                    "success": item.success,
                    "message": item.message
                }
                for item in self.history
            ]
        }

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):

        return (
            self.blueprint is not None
            and self.mapper is not None
            and self.locator is not None
            and self.dependency_graph is not None
            and self.integration_checker is not None
            and self.error_intelligence is not None
            and self.knowledge_base is not None
            and self.change_planner is not None
        )

    # ----------------------------------------
    # Future AI Auto Patch Hook
    # ----------------------------------------

    def ai_patch(
        self,
        target_file=None,
        feature=None
    ):

        """
        Reserved for future autonomous
        patch execution engine.
        """

        return {
            "status": "READY",
            "target_file": target_file,
            "feature": feature
        }

    # ----------------------------------------
    # Reset Engine
    # ----------------------------------------

    def reset(self):

        self.history.clear()

        return True

    # ----------------------------------------
    # String Representation
    # ----------------------------------------

    def __str__(self):

        stats = self.statistics()

        return (
            f"AutoPatchEngine("
            f"patches={stats['total_patches']}, "
            f"success={stats['successful']}, "
            f"failed={stats['failed']})"
        )

    __repr__ = __str__
