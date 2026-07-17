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


__init__()-
self.blueprint = ProjectBlueprint()

self.blueprint.build(project_root)


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


self.blueprint.enable_module("ProjectMapper")
self.blueprint.enable_module("CodeLocator")
self.blueprint.enable_module("DependencyGraph")
self.blueprint.enable_module("IntegrationChecker")
self.blueprint.enable_module("ErrorIntelligence")
self.blueprint.enable_module("KnowledgeBase")
self.blueprint.enable_module("ChangePlanner")
self.blueprint.enable_module("AutoPatchEngine")
self.blueprint.enable_module("ProjectMemory")
self.blueprint.enable_module("LiveMonitor")
self.blueprint.enable_module("WorkflowEngine")
self.blueprint.enable_module("AIAssistant")


self.blueprint.connect(
    "project_mapper",
    self.mapper
)

self.blueprint.connect(
    "code_locator",
    self.locator
)

self.blueprint.connect(
    "dependency_graph",
    self.dependency_graph
)

self.blueprint.connect(
    "integration_checker",
    self.integration_checker
)

self.blueprint.connect(
    "error_intelligence",
    self.error_intelligence
)

self.blueprint.connect(
    "knowledge_base",
    self.knowledge_base
)



self.blueprint.report()


self.blueprint.is_ready()
