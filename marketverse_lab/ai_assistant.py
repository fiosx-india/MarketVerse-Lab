"""
MarketVerse Lab
ai_assistant.py

Purpose:
Natural Language AI Assistant for
MarketVerse Lab.
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class AIRequest:

    command: str
    target: Optional[str] = None
    feature: Optional[str] = None


class AIAssistant:

    def __init__(self):

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
        self.live_monitor = None

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

    def connect_live_monitor(
        self,
        monitor
    ):

        self.live_monitor = monitor

    # ----------------------------------------
    # Parse Request
    # ----------------------------------------

    def parse_request(
        self,
        text
    ):

        text = text.strip()

        request = AIRequest(
            command=text
        )

        lower = text.lower()

        if "scan" in lower:
            request.command = "SCAN"

        elif "plan" in lower:
            request.command = "PLAN"

        elif "patch" in lower:
            request.command = "PATCH"

        elif "report" in lower:
            request.command = "REPORT"

        elif "monitor" in lower:
            request.command = "MONITOR"

        return request

    # ----------------------------------------
    # Scan Project
    # ----------------------------------------

    def scan_project(self):

        if self.guardian is None:

            return {
                "success": False,
                "message": "GuardianCore not connected."
            }

        return self.guardian.scan_project()

    # ----------------------------------------
    # Plan Change
    # ----------------------------------------

    def plan_change(
        self,
        target_file,
        action
    ):

        if self.change_planner is None:

            return []

        return self.change_planner.generate_plan(
            target_file,
            action
        )

    # ----------------------------------------
    # Generate Report
    # ----------------------------------------

    def generate_report(self):

        if self.guardian is None:

            return {}

        return self.guardian.health_report()

    # ----------------------------------------
    # Start Monitor
    # ----------------------------------------

    def start_monitor(self):

        if self.live_monitor is None:

            return {
                "success": False
            }

        return self.live_monitor.auto_scan()

    # ----------------------------------------
    # Execute Command
    # ----------------------------------------

    def execute(
        self,
        text
    ):

        request = self.parse_request(
            text
        )

        if request.command == "SCAN":

            return self.scan_project()

        elif request.command == "REPORT":

            return self.generate_report()

        elif request.command == "MONITOR":

            return self.start_monitor()

        return {
            "success": False,
            "message": "Unknown command."
        }

    # ----------------------------------------
    # Tamil / English Command Parser
    # ----------------------------------------

    def understand(self, text):

        text = text.lower().strip()

        if any(word in text for word in [
            "scan", "ஸ்கேன்", "சோதனை"
        ]):
            return "SCAN"

        if any(word in text for word in [
            "plan", "திட்டம்", "மாற்றம்"
        ]):
            return "PLAN"

        if any(word in text for word in [
            "patch", "சரி", "பேட்ச்"
        ]):
            return "PATCH"

        if any(word in text for word in [
            "report", "அறிக்கை"
        ]):
            return "REPORT"

        if any(word in text for word in [
            "monitor", "கண்காணி"
        ]):
            return "MONITOR"

        return "UNKNOWN"

    # ----------------------------------------
    # Analyze Errors
    # ----------------------------------------

    def analyze_errors(self):

        if self.error_intelligence is None:
            return None

        return self.error_intelligence.report()

    # ----------------------------------------
    # Recommend Fix
    # ----------------------------------------

    def recommend_fix(self):

        if self.change_planner is None:
            return {
                "status": "Planner not connected."
            }

        return {
            "status": "READY",
            "recommendation":
                "Review affected files before patch."
        }

    # ----------------------------------------
    # AI Suggestion
    # ----------------------------------------

    def suggest(self):

        return {
            "health": self.generate_report(),
            "errors": self.analyze_errors(),
            "fix": self.recommend_fix()
        }

    # ----------------------------------------
    # Smart Execute
    # ----------------------------------------

    def smart_execute(self, text):

        command = self.understand(text)

        if command == "SCAN":
            return self.scan_project()

        elif command == "REPORT":
            return self.generate_report()

        elif command == "MONITOR":
            return self.start_monitor()

        elif command == "PLAN":
            return {
                "status": "Planning Ready"
            }

        elif command == "PATCH":
            return {
                "status": "Patch Engine Ready"
            }

        return {
            "status": "Unknown Command"
        }

    # ----------------------------------------
    # Statistics
    # ----------------------------------------

    def statistics(self):

        return {
            "guardian_connected": self.guardian is not None,
            "modules_connected": sum([
                self.blueprint is not None,
                self.mapper is not None,
                self.locator is not None,
                self.dependency_graph is not None,
                self.integration_checker is not None,
                self.error_intelligence is not None,
                self.knowledge_base is not None,
                self.change_planner is not None,
                self.auto_patch_engine is not None,
                self.project_memory is not None,
                self.live_monitor is not None
            ])
        }

    # ----------------------------------------
    # Diagnostics
    # ----------------------------------------

    def diagnostics(self):

        return {
            "guardian": self.guardian is not None,
            "blueprint": self.blueprint is not None,
            "mapper": self.mapper is not None,
            "locator": self.locator is not None,
            "dependency_graph": self.dependency_graph is not None,
            "integration_checker": self.integration_checker is not None,
            "error_intelligence": self.error_intelligence is not None,
            "knowledge_base": self.knowledge_base is not None,
            "change_planner": self.change_planner is not None,
            "auto_patch_engine": self.auto_patch_engine is not None,
            "project_memory": self.project_memory is not None,
            "live_monitor": self.live_monitor is not None
        }

    # ----------------------------------------
    # Full AI Report
    # ----------------------------------------

    def report(self):

        return {
            "statistics": self.statistics(),
            "diagnostics": self.diagnostics(),
            "suggestions": self.suggest()
        }

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):

        return all(
            self.diagnostics().values()
        )

    # ----------------------------------------
    # Future Autonomous AI Hook
    # ----------------------------------------

    def autonomous_mode(self):

        """
        Reserved for future autonomous
        AI operation.
        """

        return {
            "status": "READY",
            "mode": "AUTONOMOUS"
        }

    # ----------------------------------------
    # Reset Assistant
    # ----------------------------------------

    def reset(self):

        return {
            "status": "RESET_COMPLETE"
        }

    # ----------------------------------------
    # String Representation
    # ----------------------------------------

    def __str__(self):

        stats = self.statistics()

        return (
            f"AIAssistant("
            f"modules={stats['modules_connected']})"
        )

    __repr__ = __str__
