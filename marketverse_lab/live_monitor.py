"""
MarketVerse Lab
live_monitor.py

Purpose:
Monitor project files in real time and
notify GuardianCore when changes occur.
"""

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict


@dataclass
class FileState:

    path: str
    modified: float
    size: int


class LiveMonitor:

    def __init__(self):

        # Core Connections
        self.guardian = None
        self.blueprint = None
        self.mapper = None
        self.locator = None
        self.dependency_graph = None
        self.integration_checker = None
        self.error_intelligence = None
        self.knowledge_base = None
        self.change_planner = None
        self.auto_patch_engine = None
        self.project_memory = None

        # File Cache
        self.files: Dict[str, FileState] = {}

    # ----------------------------------------

    def connect_guardian(
        self,
        guardian
    ):

        self.guardian = guardian

    # ----------------------------------------

    def connect_blueprint(
        self,
        blueprint
    ):

        self.blueprint = blueprint

    # ----------------------------------------

    def connect_mapper(
        self,
        mapper
    ):

        self.mapper = mapper

    # ----------------------------------------

    def connect_locator(
        self,
        locator
    ):

        self.locator = locator

    # ----------------------------------------

    def connect_dependency_graph(
        self,
        graph
    ):

        self.dependency_graph = graph

    # ----------------------------------------

    def connect_integration_checker(
        self,
        checker
    ):

        self.integration_checker = checker

    # ----------------------------------------

    def connect_error_intelligence(
        self,
        intelligence
    ):

        self.error_intelligence = intelligence

    # ----------------------------------------

    def connect_knowledge_base(
        self,
        knowledge
    ):

        self.knowledge_base = knowledge

    # ----------------------------------------

    def connect_change_planner(
        self,
        planner
    ):

        self.change_planner = planner

    # ----------------------------------------

    def connect_auto_patch_engine(
        self,
        engine
    ):

        self.auto_patch_engine = engine

    # ----------------------------------------

    def connect_project_memory(
        self,
        memory
    ):

        self.project_memory = memory

    # ----------------------------------------
    # Register File
    # ----------------------------------------

    def register_file(
        self,
        file
    ):

        path = Path(file)

        if not path.exists():
            return False

        stat = path.stat()

        self.files[str(path)] = FileState(
            path=str(path),
            modified=stat.st_mtime,
            size=stat.st_size
        )

        return True

    # ----------------------------------------
    # Scan Folder
    # ----------------------------------------

    def scan_folder(
        self,
        folder="."
    ):

        folder = Path(folder)

        for file in folder.rglob("*.py"):
            self.register_file(file)

        return len(self.files)

    # ----------------------------------------
    # Detect Changes
    # ----------------------------------------

    def detect_changes(self):

        changes = []

        for file, state in self.files.items():

            path = Path(file)

            if not path.exists():
                continue

            stat = path.stat()

            if (
                stat.st_mtime != state.modified
                or
                stat.st_size != state.size
            ):

                changes.append(file)

                self.files[file] = FileState(
                    path=file,
                    modified=stat.st_mtime,
                    size=stat.st_size
                )

        return changes

    # ----------------------------------------
    # New Files
    # ----------------------------------------

    def new_files(
        self,
        folder="."
    ):

        folder = Path(folder)

        found = []

        for file in folder.rglob("*.py"):

            if str(file) not in self.files:

                self.register_file(file)

                found.append(str(file))

        return found

    # ----------------------------------------
    # Deleted Files
    # ----------------------------------------

    def deleted_files(self):

        deleted = []

        for file in list(self.files.keys()):

            if not Path(file).exists():

                deleted.append(file)

                del self.files[file]

        return deleted

    # ----------------------------------------
    # Notify Guardian
    # ----------------------------------------

    def notify_guardian(self, changes):

        if self.guardian is None:
            return None

        return self.guardian.scan_project()

    # ----------------------------------------
    # Auto Scan
    # ----------------------------------------

    def auto_scan(self):

        changes = self.detect_changes()

        if not changes:
            return {
                "status": "NO_CHANGES",
                "files": []
            }

        report = self.notify_guardian(changes)

        return {
            "status": "SCANNED",
            "files": changes,
            "report": report
        }

    # ----------------------------------------
    # Record Changes
    # ----------------------------------------

    def record_changes(self, changes):

        if self.project_memory is None:
            return

        for file in changes:

            self.project_memory.record_change(
                file=file,
                action="FILE_CHANGED",
                description="Detected by LiveMonitor"
            )

    # ----------------------------------------
    # Auto Plan
    # ----------------------------------------

    def auto_plan(self, changes):

        if self.change_planner is None:
            return []

        plans = []

        for file in changes:

            plans.append(
                self.change_planner.generate_plan(
                    target_file=file,
                    action="REVIEW"
                )
            )

        return plans

    # ----------------------------------------
    # Live Check
    # ----------------------------------------

    def check(self):

        changes = self.detect_changes()

        self.record_changes(changes)

        return {
            "changes": changes,
            "plans": self.auto_plan(changes),
            "count": len(changes)
        }

    # ----------------------------------------
    # Event History
    # ----------------------------------------

    def history(self):

        if self.project_memory is None:
            return []

        return self.project_memory.recent_changes()

    # ----------------------------------------
    # Statistics
    # ----------------------------------------

    def statistics(self):

        return {
            "tracked_files": len(self.files),
            "recent_changes": len(
                self.detect_changes()
            )
        }

    # ----------------------------------------
    # Diagnostics
    # ----------------------------------------

    def diagnostics(self):

        return {
            "guardian_connected":
                self.guardian is not None,
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
            "auto_patch_engine_connected":
                self.auto_patch_engine is not None,
            "project_memory_connected":
                self.project_memory is not None
        }

    # ----------------------------------------
    # Health Report
    # ----------------------------------------

    def report(self):

        return {
            "statistics": self.statistics(),
            "diagnostics": self.diagnostics(),
            "tracked_files": list(self.files.keys())
        }

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):

        return all(
            self.diagnostics().values()
        )

    # ----------------------------------------
    # Future AI Monitor Hook
    # ----------------------------------------

    def ai_monitor(self):

        """
        Reserved for future autonomous
        monitoring engine.
        """

        return {
            "status": "READY"
        }

    # ----------------------------------------
    # Reset Monitor
    # ----------------------------------------

    def reset(self):

        self.files.clear()

        return True

    # ----------------------------------------
    # String Representation
    # ----------------------------------------

    def __str__(self):

        return (
            f"LiveMonitor("
            f"tracked_files={len(self.files)})"
        )

    __repr__ = __str__
