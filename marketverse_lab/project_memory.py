"""
MarketVerse Lab
project_memory.py

Purpose:
Store project history, changes,
versions and development memory.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


@dataclass
class MemoryEntry:

    file: str
    action: str
    timestamp: str
    description: str
    metadata: Dict = field(default_factory=dict)


class ProjectMemory:

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
        self.auto_patch_engine = None
        self.project_memory = None
        self.live_monitor = None
        self.workflow_engine = None

        # Memory Storage
        self.history: List[MemoryEntry] = []

    def connect_live_monitor(self, monitor):

        self.live_monitor = monitor


    def connect_workflow_engine(self, workflow):

        self.workflow_engine = workflow


    def connect_project_memory(self, memory):

        self.project_memory = memory
        
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

    def connect_auto_patch_engine(self, engine):

        self.auto_patch_engine = engine

    # ----------------------------------------

    def reset(self):

        self.history.clear()

        return True

    # ----------------------------------------
    # Record Change
    # ----------------------------------------

    def record_change(
        self,
        file,
        action,
        description,
        metadata=None
    ):

        if metadata is None:
            metadata = {}

        entry = MemoryEntry(
            file=file,
            action=action,
            timestamp=datetime.now().isoformat(),
            description=description,
            metadata=metadata
        )

        self.history.append(entry)

        return entry

    # ----------------------------------------
    # File History
    # ----------------------------------------

    def file_history(
        self,
        file
    ):

        return [

            item

            for item in self.history

            if item.file == file

        ]

    # ----------------------------------------
    # Recent Changes
    # ----------------------------------------

    def recent_changes(
        self,
        limit=10
    ):

        return self.history[-limit:]

    # ----------------------------------------
    # Create Snapshot
    # ----------------------------------------

    def snapshot(self):

        return [

            {
                "file": item.file,
                "action": item.action,
                "timestamp": item.timestamp,
                "description": item.description
            }

            for item in self.history

        ]

    # ----------------------------------------
    # Search History
    # ----------------------------------------

    def search(
        self,
        keyword
    ):

        keyword = keyword.lower()

        return [

            item

            for item in self.history

            if (
                keyword in item.file.lower()
                or
                keyword in item.action.lower()
                or
                keyword in item.description.lower()
            )

        ]

    # ----------------------------------------
    # Total Changes
    # ----------------------------------------

    def count(self):

        return len(self.history)

    # ----------------------------------------
    # Version History
    # ----------------------------------------

    def versions(self):

        return [
            {
                "version": index + 1,
                "file": item.file,
                "timestamp": item.timestamp
            }
            for index, item in enumerate(self.history)
        ]

    # ----------------------------------------
    # Undo Point
    # ----------------------------------------

    def undo_point(self):

        if not self.history:
            return None

        return self.history[-1]

    # ----------------------------------------
    # AI Notes
    # ----------------------------------------

    def add_note(
        self,
        file,
        note
    ):

        return self.record_change(
            file=file,
            action="AI_NOTE",
            description=note
        )

    # ----------------------------------------
    # Timeline
    # ----------------------------------------

    def timeline(
        self
    ):

        return sorted(
            self.history,
            key=lambda item: item.timestamp
        )
    # ----------------------------------------
    # Files Changed
    # ----------------------------------------

    def changed_files(self):

        return sorted(
            {
                item.file
                for item in self.history
            }
        )

    # ----------------------------------------
    # Last Change
    # ----------------------------------------

    def last_change(self):

        if not self.history:
            return None

        return self.history[-1]

    # ----------------------------------------
    # Statistics
    # ----------------------------------------

    def statistics(self):

        return {
            "total_changes": len(self.history),
            "files_changed": len(self.changed_files())
        }

    # ----------------------------------------
    # Diagnostics
    # ----------------------------------------

    def diagnostics(self):

        return {
            "history": len(self.history),
            "knowledge": self.knowledge_base is not None,
            "planner": self.change_planner is not None,
            "patch_engine": self.auto_patch_engine is not None
        }

    # ----------------------------------------
    # Report
    # ----------------------------------------

    def report(self):

        return {
            "statistics": self.statistics(),
            "diagnostics": self.diagnostics(),
            "recent": self.recent_changes()
        }

    # ----------------------------------------
    # Ready
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
            and self.auto_patch_engine is not None
        )

    # ----------------------------------------
    # Future AI Memory Hook
    # ----------------------------------------

    def ai_memory(self):

        return {
            "status": "READY"
        }

    # ----------------------------------------
    # String Representation
    # ----------------------------------------

    def __str__(self):

        return (
            f"ProjectMemory("
            f"changes={len(self.history)})"
        )

    __repr__ = __str__
