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
        self.ai_assistant = AIAssistant()

        # Build Project Blueprint
        self.blueprint.build(project_root)

        # Build Project Mapper
        self.mapper.build(project_root)
        
        # Build Dependency Graph
        self.dependency_graph.build()

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

        # Project Blueprint
        self.mapper.connect_blueprint(self.blueprint)

        self.blueprint.connect("ProjectMapper", self.mapper)
        self.blueprint.connect("CodeLocator", self.locator)
        self.blueprint.connect("DependencyGraph", self.dependency_graph)
        self.blueprint.connect("IntegrationChecker", self.integration_checker)
        self.blueprint.connect("ErrorIntelligence", self.error_intelligence)
        self.blueprint.connect("KnowledgeBase", self.knowledge_base)
        self.blueprint.connect("ChangePlanner", self.change_planner)
        self.blueprint.connect("AutoPatchEngine", self.auto_patch_engine)
        self.blueprint.connect("ProjectMemory", self.project_memory)
        self.blueprint.connect("LiveMonitor", self.live_monitor)
        self.blueprint.connect("WorkflowEngine", self.workflow_engine)
        self.blueprint.connect("AIAssistant", self.ai_assistant)
        
        # Code Locator
        self.locator.connect_blueprint(self.blueprint)
        self.locator.connect_mapper(self.mapper)
        
        # Dependency Graph
        self.dependency_graph.connect_blueprint(self.blueprint)
        self.dependency_graph.connect_mapper(self.mapper)
        self.dependency_graph.connect_locator(self.locator)
        
        self.dependency_graph.build()
        
        # Integration Checker
        self.integration_checker.connect_blueprint(self.blueprint)
        self.integration_checker.connect_mapper(self.mapper)
        self.integration_checker.connect_locator(self.locator)
        self.integration_checker.connect_dependency_graph(self.dependency_graph)
        
        # Live Monitor
        self.live_monitor.connect_guardian(self)
        self.live_monitor.connect_blueprint(self.blueprint)
        self.live_monitor.connect_mapper(self.mapper)
        self.live_monitor.connect_locator(self.locator)
        self.live_monitor.connect_dependency_graph(self.dependency_graph)
        self.live_monitor.connect_integration_checker(self.integration_checker)
        self.live_monitor.connect_error_intelligence(self.error_intelligence)
        self.live_monitor.connect_knowledge_base(self.knowledge_base)
        self.live_monitor.connect_change_planner(self.change_planner)
        self.live_monitor.connect_auto_patch_engine(self.auto_patch_engine)
        self.live_monitor.connect_project_memory(self.project_memory)

        # AI Assistant
        self.ai_assistant.connect_guardian(self)
        self.ai_assistant.connect_blueprint(self.blueprint)
        self.ai_assistant.connect_mapper(self.mapper)
        self.ai_assistant.connect_locator(self.locator)
        self.ai_assistant.connect_dependency_graph(self.dependency_graph)
        self.ai_assistant.connect_integration_checker(self.integration_checker)
        self.ai_assistant.connect_error_intelligence(self.error_intelligence)
        self.ai_assistant.connect_knowledge_base(self.knowledge_base)
        self.ai_assistant.connect_change_planner(self.change_planner)
        self.ai_assistant.connect_auto_patch_engine(self.auto_patch_engine)
        self.ai_assistant.connect_project_memory(self.project_memory)
        self.ai_assistant.connect_live_monitor(self.live_monitor)

        # Workflow Engine
        self.workflow_engine.connect_guardian(self)
        self.workflow_engine.connect_ai_assistant(self.ai_assistant)
        self.workflow_engine.connect_change_planner(self.change_planner)
        self.workflow_engine.connect_auto_patch_engine(self.auto_patch_engine)
        self.workflow_engine.connect_project_memory(self.project_memory)
        self.workflow_engine.connect_live_monitor(self.live_monitor)
        self.workflow_engine.connect_blueprint(self.blueprint)
        self.workflow_engine.connect_mapper(self.mapper)
        self.workflow_engine.connect_locator(self.locator)
        self.workflow_engine.connect_dependency_graph(self.dependency_graph)
        self.workflow_engine.connect_integration_checker(self.integration_checker)
        self.workflow_engine.connect_error_intelligence(self.error_intelligence)
        self.workflow_engine.connect_knowledge_base(self.knowledge_base)
        
        # Error Intelligence
        self.error_intelligence.connect_blueprint(self.blueprint)
        self.error_intelligence.connect_mapper(self.mapper)
        self.error_intelligence.connect_locator(self.locator)
        self.error_intelligence.connect_dependency_graph(self.dependency_graph)
        self.error_intelligence.connect_integration_checker(self.integration_checker)
    
         # Knowledge Base
        self.knowledge_base.connect_blueprint(self.blueprint)
        self.knowledge_base.connect_mapper(self.mapper)
        self.knowledge_base.connect_locator(self.locator)
        self.knowledge_base.connect_dependency_graph(self.dependency_graph)
        self.knowledge_base.connect_integration_checker(self.integration_checker)
        self.knowledge_base.connect_error_intelligence(self.error_intelligence)   

        # Change Planner
        self.change_planner.connect_blueprint(self.blueprint)
        self.change_planner.connect_mapper(self.mapper)
        self.change_planner.connect_locator(self.locator)
        self.change_planner.connect_dependency_graph(self.dependency_graph)
        self.change_planner.connect_integration_checker(self.integration_checker)
        self.change_planner.connect_error_intelligence(self.error_intelligence)
        self.change_planner.connect_knowledge_base(self.knowledge_base)
        self.change_planner.connect_auto_patch_engine(self.auto_patch_engine)
        self.change_planner.connect_project_memory(self.project_memory)
        self.change_planner.connect_live_monitor(self.live_monitor)

        # Auto Patch Engine
        self.auto_patch_engine.connect_blueprint(self.blueprint)
        self.auto_patch_engine.connect_mapper(self.mapper)
        self.auto_patch_engine.connect_locator(self.locator)
        self.auto_patch_engine.connect_dependency_graph(self.dependency_graph)
        self.auto_patch_engine.connect_integration_checker(self.integration_checker)
        self.auto_patch_engine.connect_error_intelligence(self.error_intelligence)
        self.auto_patch_engine.connect_knowledge_base(self.knowledge_base)
        self.auto_patch_engine.connect_change_planner(self.change_planner)
        
        # Project Memory
        self.project_memory.connect_blueprint(self.blueprint)
        self.project_memory.connect_mapper(self.mapper)
        self.project_memory.connect_locator(self.locator)
        self.project_memory.connect_dependency_graph(self.dependency_graph)
        self.project_memory.connect_integration_checker(self.integration_checker)
        self.project_memory.connect_error_intelligence(self.error_intelligence)
        self.project_memory.connect_knowledge_base(self.knowledge_base)
        self.project_memory.connect_change_planner(self.change_planner)
        self.project_memory.connect_auto_patch_engine(self.auto_patch_engine)
        self.project_memory.connect_live_monitor(self.live_monitor)
        self.project_memory.connect_workflow_engine(self.workflow_engine)
    
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
        return self.project_memory.record_change(file, action, description, metadata)

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

    def assistant_report(self):
        return self.ai_assistant.report()

    def assistant_ready(self):
        return self.ai_assistant.is_ready()

    def ask_ai(self, text):
        return self.ai_assistant.smart_execute(text)
