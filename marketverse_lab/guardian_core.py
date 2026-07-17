"""
MarketVerse Lab
guardian_core.py

Purpose:
Central AI Brain for MarketVerse Lab.
Coordinates every module.
"""

from .project_blueprint import ProjectBlueprint
from .project_mapper import ProjectMapper
from .code_locator import CodeLocator
from .dependency_graph import DependencyGraph
from .integration_checker import IntegrationChecker
from .error_intelligence import ErrorIntelligence
from .knowledge_base import KnowledgeBase
from .change_planner import ChangePlanner
from .auto_patch_engine import AutoPatchEngine
from .project_memory import ProjectMemory
from .live_monitor import LiveMonitor
from .workflow_engine import WorkflowEngine
from .ai_assistant import AIAssistant


class GuardianCore:

    def __init__(self, project_root="."):

        # Blueprint
        self.blueprint = ProjectBlueprint()
        self.locator = CodeLocator()

        # Build Project Blueprint
        self.blueprint.build(project_root)

        # Register Modules
        self.blueprint.register_module(
            "ProjectMapper",
            "Project Structure Mapper"
        )

        self.blueprint.register_module(
            "CodeLocator",
            "Code Locator"
        )

        self.blueprint.register_module(
            "DependencyGraph",
            "Dependency Analyzer"
        )

        self.blueprint.register_module(
            "IntegrationChecker",
            "Integration Checker"
        )

        self.blueprint.register_module(
            "ErrorIntelligence",
            "AI Error Intelligence"
        )

        self.blueprint.register_module(
            "KnowledgeBase",
            "Knowledge Repository"
        )

        self.blueprint.register_module(
            "ChangePlanner",
            "Change Planner"
        )

        self.blueprint.register_module(
            "AutoPatchEngine",
            "Auto Patch Engine"
        )

        self.blueprint.register_module(
            "ProjectMemory",
            "Project Memory"
        )

        self.blueprint.register_module(
            "LiveMonitor",
            "Live Monitor"
        )

        self.blueprint.register_module(
            "WorkflowEngine",
            "Workflow Engine"
        )

        self.blueprint.register_module(
            "AIAssistant",
            "AI Assistant"
        )

        # Enable Modules
        for module in (
            "ProjectMapper",
            "CodeLocator",
            "DependencyGraph",
            "IntegrationChecker",
            "ErrorIntelligence",
            "KnowledgeBase",
            "ChangePlanner",
            "AutoPatchEngine",
            "ProjectMemory",
            "LiveMonitor",
            "WorkflowEngine",
            "AIAssistant",
        ):
            self.blueprint.enable_module(module)

        # Blueprint Connections
        # (இந்த self.mapper, self.locator போன்ற objects
        # உருவாக்கப்பட்ட பிறகு connect செய்ய வேண்டும்.)

    def report(self):
        return self.blueprint.report()

    def is_ready(self):
        return self.blueprint.is_ready()

    def health_report(self):
        return self.blueprint.validate()

    def dashboard_report(self):
        return self.blueprint.summary()
