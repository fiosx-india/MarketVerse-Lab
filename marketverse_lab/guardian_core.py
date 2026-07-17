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
        self.mapper = ProjectMapper()
        self.dependency_graph = DependencyGraph()
        self.integration_checker = IntegrationChecker()
        self.error_intelligence = ErrorIntelligence()
        self.knowledge_base = KnowledgeBase()

        # Build Project Blueprint
        self.blueprint.build(project_root)

        # Register Modules
        self.blueprint.register_module("ProjectMapper", "Project Structure Mapper")

        self.blueprint.register_module("CodeLocator", "Code Locator")

        self.blueprint.register_module("DependencyGraph", "Dependency Analyzer")

        self.blueprint.register_module("IntegrationChecker", "Integration Checker")

        self.blueprint.register_module("ErrorIntelligence", "AI Error Intelligence")

        self.blueprint.register_module("KnowledgeBase", "Knowledge Repository")

        self.blueprint.register_module("ChangePlanner", "Change Planner")

        self.blueprint.register_module("AutoPatchEngine", "Auto Patch Engine")

        self.blueprint.register_module("ProjectMemory", "Project Memory")

        self.blueprint.register_module("LiveMonitor", "Live Monitor")

        self.blueprint.register_module("WorkflowEngine", "Workflow Engine")

        self.blueprint.register_module("AIAssistant", "AI Assistant")

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

        # Module Connections

    def report(self):
        return self.blueprint.report()

    def is_ready(self):
        return self.blueprint.is_ready()

    def health_report(self):
        return self.blueprint.validate()

    def dashboard_report(self):
        return self.blueprint.summary()

    def locate(self, target):
        return self.locator.locate(target)

    def map_project(self, root="."):
        return self.mapper.build(root)

    def mapper_report(self):
        return self.mapper.report()

    def mapper_ready(self):
        return self.mapper.is_ready()

    def build_dependency_graph(self):
        return self.dependency_graph.build()

    def dependency_report(self):
        return self.dependency_graph.report()

    def dependency_ready(self):
        return self.dependency_graph.is_ready()

    def check_integration(self, target_file):
        return self.integration_checker.validate(target_file)

    def integration_report(self):
        return self.integration_checker.report()

    def integration_ready(self):
        return self.integration_checker.is_ready()

    def error_report(self):
        return self.error_intelligence.report()

    def error_ready(self):
        return self.error_intelligence.is_ready()

    def ai_recommendation(self):
        return self.error_intelligence.recommendations()
    def knowledge_report(self):
        return self.knowledge_base.report()

    def knowledge_ready(self):
        return self.knowledge_base.is_ready()

    def knowledge_statistics(self):
        return self.knowledge_base.statistics()
