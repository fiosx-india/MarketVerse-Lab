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
        self.change_planner = ChangePlanner()
        self.auto_patch_engine = AutoPatchEngine()
        self.project_memory = ProjectMemory()
        self.live_monitor = LiveMonitor()
        self.workflow_engine = WorkflowEngine()

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
        
    def change_report(self):
        return self.change_planner.report()

    def change_ready(self):
        return self.change_planner.is_ready()

    def plan_change(self, target_file, action):
        return self.change_planner.generate_plan(target_file, action)
        
    def patch_report(self):
        return self.auto_patch_engine.report()

    def patch_ready(self):
        return self.auto_patch_engine.is_ready()

    def apply_patch(self, file, line, code):
        return self.auto_patch_engine.insert_code(file, line, code)
        
    def memory_report(self):
        return self.project_memory.report()

    def memory_ready(self):
        return self.project_memory.is_ready()

    def record_change(self, file, action, description, metadata=None):
        return self.project_memory.record_change(
            file,
            action,
            description,
            metadata
        )
        
    def monitor_report(self):
        return self.live_monitor.report()

    def monitor_ready(self):
        return self.live_monitor.is_ready()

    def scan_project(self):
        return self.live_monitor.check()

    def workflow_report(self):
        return self.workflow_engine.health_report()

    def workflow_ready(self):
        return self.workflow_engine.is_ready()

    def create_workflow(self, feature_name):
        return self.workflow_engine.create_workflow(feature_name)

