"""
Change Report

Purpose:
Track project changes.
"""

from datetime import datetime


class ChangeReport:

    MAX_HISTORY = 20

    def __init__(self):
        self.changes = []

    def scan(self):

        self.changes.append({

            "time": datetime.now().isoformat(),

            "status": "SCAN_COMPLETED"

        })

        # Keep only latest history
        if len(self.changes) > self.MAX_HISTORY:
            self.changes = self.changes[-self.MAX_HISTORY:]

        return self.report()

    def report(self):

        latest = (
            self.changes[-1]
            if self.changes
            else None
        )

        return {

            "status": "PASS",

            "total_changes": len(self.changes),

            "last_change": latest

        }

    def history(self):

        return self.changes

    def clear(self):

        self.changes.clear()

    def connect_blueprint(self, blueprint):

        self.blueprint = blueprint

    def connect_mapper(self, mapper):

        self.mapper = mapper

    def connect_locator(self, locator):

        self.locator = locator

    def connect_dependency_graph(self, dependency_graph):

        self.dependency_graph = dependency_graph

    def is_ready(self):

        return True
