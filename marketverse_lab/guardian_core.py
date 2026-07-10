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

    def __init__(self):

        # Core Modules
        self.blueprint = ProjectBlueprint()
        self.mapper = ProjectMapper()
        self.locator = CodeLocator()
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
        
        self._connect_modules()

    # ----------------------------------------
    # Connect Everything
    # ----------------------------------------

    def _connect_modules(self):

        modules = [

            self.integration_checker,
            self.error_intelligence,
            self.knowledge_base,
            self.change_planner,
            self.auto_patch_engine,
            self.project_memory,
            self.live_monitor,
            self.workflow_engine,
            self.ai_assistant
            
        ]

        for module in modules:
            try:
                # Connect common modules
                module.connect_blueprint(self.blueprint)
                module.connect_mapper(self.mapper)
                module.connect_locator(self.locator)
                module.connect_dependency_graph(
                    self.dependency_graph
                )

            except Exception as e:
                print(
                    f"[Guardian] Connection failed: "
                    f"{module.__class__.__name__} -> {e}"
                )
                continue

        self.ai_assistant.connect_guardian(self)

        self.ai_assistant.connect_change_planner(
            self.change_planner
        )

        self.ai_assistant.connect_auto_patch_engine(
            self.auto_patch_engine
        )

        self.ai_assistant.connect_project_memory(
            self.project_memory
        )

        self.ai_assistant.connect_live_monitor(
            self.live_monitor
        )

        self.ai_assistant.connect_integration_checker(
            self.integration_checker
        )

        self.ai_assistant.connect_error_intelligence(
            self.error_intelligence
        )

        self.ai_assistant.connect_knowledge_base(
            self.knowledge_base
        )

        self.integration_checker.connect_mapper(
            self.mapper
        )

        self.error_intelligence.connect_integration_checker(
            self.integration_checker
        )

        self.knowledge_base.connect_integration_checker(
            self.integration_checker
        )

        self.knowledge_base.connect_error_intelligence(
            self.error_intelligence
        )

        self.change_planner.connect_integration_checker(
            self.integration_checker
        )

        self.change_planner.connect_error_intelligence(
            self.error_intelligence
        )

        self.change_planner.connect_knowledge_base(
            self.knowledge_base
        )

        self.auto_patch_engine.connect_integration_checker(
            self.integration_checker
        )

        self.auto_patch_engine.connect_error_intelligence(
            self.error_intelligence
        )

        self.auto_patch_engine.connect_knowledge_base(
            self.knowledge_base
        )

        self.auto_patch_engine.connect_change_planner(
            self.change_planner
        )

        self.project_memory.connect_integration_checker(
            self.integration_checker
        )

        self.project_memory.connect_error_intelligence(
            self.error_intelligence
        )

        self.project_memory.connect_knowledge_base(
            self.knowledge_base
        )

        self.project_memory.connect_change_planner(
            self.change_planner
        )
                 
        self.project_memory.connect_auto_patch_engine(
            self.auto_patch_engine
        )

        # ----------------------------------------
        # Live Monitor Connections
        # ----------------------------------------

        self.live_monitor.connect_guardian(self)

        self.live_monitor.connect_integration_checker(
            self.integration_checker
        )

        self.live_monitor.connect_error_intelligence(
            self.error_intelligence
        )

        self.live_monitor.connect_knowledge_base(
            self.knowledge_base
        )

        self.live_monitor.connect_change_planner(
            self.change_planner
        )

        self.live_monitor.connect_auto_patch_engine(
            self.auto_patch_engine
        )

        self.live_monitor.connect_project_memory(
            self.project_memory
        )

        # ----------------------------------------
        # Workflow Engine Connections
        # ----------------------------------------

        self.workflow_engine.connect_guardian(self)

        self.workflow_engine.connect_ai_assistant(
            self.ai_assistant
        )

        self.workflow_engine.connect_change_planner(
            self.change_planner
        )

        self.workflow_engine.connect_auto_patch_engine(
            self.auto_patch_engine
        )

        self.workflow_engine.connect_project_memory(
            self.project_memory
        )

        self.workflow_engine.connect_live_monitor(
            self.live_monitor
        )

    # ----------------------------------------
    # Scan Project
    # ----------------------------------------

    def scan_project(
        self,
        root="."
    ):


        report = {}

        report["blueprint"] = self.blueprint.report()

        report["mapping"] = self.mapper.report()

        report["dependencies"] = (
            self.dependency_graph.report()
        )

        report["integration"] = (
            self.integration_checker.report()
        )

        report["errors"] = (
            self.error_intelligence.report()
        )

        report["knowledge"] = (
            self.knowledge_base.report()
        )

        report["memory"] = (
            self.project_memory.report()
        )

        return report
    # ----------------------------------------
    # Dashboard Report
    # ----------------------------------------

    def dashboard_report(self):

        return {
            "name": "Guardian Core",
            "version": "1.0.0",
            "health": 100,
            "status": "Ready"
        }
    # ----------------------------------------
    # Plan Change
    # ----------------------------------------

    def plan_change(
        self,
        target_file,
        action
    ):

        return self.change_planner.generate_plan(
            target_file,
            action
        )

    # ----------------------------------------
    # Apply Patch
    # ----------------------------------------

    def apply_patch(
        self,
        file,
        line,
        code
    ):

        backup = self.auto_patch_engine.backup_file(
            file
        )

        if not backup.success:

            return backup

        result = self.auto_patch_engine.insert_code(
            file=file,
            line=line,
            code=code
        )

        self.project_memory.record_change(
            file=file,
            action="PATCH",
            description=result.message
        )

        return result
    # ----------------------------------------
    # Auto Scan
    # ----------------------------------------

    def auto_scan(self):

        return {
            "scan": self.scan_project(),
            "diagnostics": self.diagnostics()
        }

    # ----------------------------------------
    # Diagnostics
    # ----------------------------------------

    def diagnostics(self):

        return {
            "blueprint": self.blueprint.is_ready(),
            "mapper": self.mapper.is_ready(),
            "locator": self.locator.is_ready(),
            "dependency_graph": self.dependency_graph.is_ready(),
            "integration_checker": self.integration_checker.is_ready(),
            "error_intelligence": self.error_intelligence.is_ready(),
            "knowledge_base": self.knowledge_base.is_ready(),
            "change_planner": self.change_planner.is_ready(),
            "auto_patch_engine": self.auto_patch_engine.is_ready(),
            "project_memory": self.project_memory.is_ready(),
           "live_monitor": self.live_monitor.is_ready(),
            "workflow_engine": self.workflow_engine.is_ready(),
            "ai_assistant": self.ai_assistant.is_ready(),
        }

    # ----------------------------------------
    # Health Report
    # ----------------------------------------

    def health_report(self):

        diagnostics = self.diagnostics()

        ready = sum(
            1
            for value in diagnostics.values()
            if value
        )

        total = len(diagnostics)

        return {
            "ready_modules": ready,
            "total_modules": total,
            "health_percent": round(
                (ready / total) * 100,
                2
            )
        }

    # ----------------------------------------
    # AI Recommendation
    # ----------------------------------------

    def ai_recommendation(self):

        return {
            "project_health": self.health_report(),
            "planner": self.change_planner.report(),
            "errors": self.error_intelligence.report()
        }

    # ----------------------------------------
    # Ready Check
    # ----------------------------------------

    def is_ready(self):

        return all(
            self.diagnostics().values()
        )

    # ----------------------------------------
    # String Representation
    # ----------------------------------------

    def __str__(self):

        health = self.health_report()

        return (
            f"GuardianCore("
            f"{health['health_percent']}% Ready)"
        )

    __repr__ = __str__

# ----------------------------------------
# Dashboard Report
# ----------------------------------------

def dashboard_report(self):

    diagnostics = self.diagnostics()
    health = self.health_report()
    scan = self.scan_project()
    ai = self.ai_recommendation()

    ready_modules = [
        name for name, state in diagnostics.items()
        if state
    ]

    pending_modules = [
        name for name, state in diagnostics.items()
        if not state
    ]

    total_modules = health["total_modules"]
    ready_count = health["ready_modules"]
    pending_count = total_modules - ready_count

    return {

        # =================================================
        # Guardian Information
        # =================================================

        "name": "Guardian Core",
        "version": "1.0.0",

        "status": (
            "🟢 Online"
            if self.is_ready()
            else
            "🟡 Initializing"
        ),

        # =================================================
        # Health
        # =================================================

        "health": health["health_percent"],

        "health_report": health,

        "ready_modules": ready_count,

        "pending_modules": pending_count,

        "total_modules": total_modules,

        # =================================================
        # Module Details
        # =================================================

        "modules": diagnostics,

        "ready_list": ready_modules,

        "pending_list": pending_modules,

        # =================================================
        # Project Scan
        # =================================================

        "scan_report": scan,

        "last_scan": "Live",

        # =================================================
        # AI Report
        # =================================================

        "ai_recommendation": ai,

        "recommendation": (
            "System Ready"
            if self.is_ready()
            else
            "Integration Pending"
        ),

        # =================================================
        # Dashboard Counters
        # =================================================

        "statistics": {

            "health_percent": health["health_percent"],

            "ready_modules": ready_count,

            "pending_modules": pending_count,

            "total_modules": total_modules,

            "ready_percent": round(
                (ready_count / total_modules) * 100,
                2
            ) if total_modules else 0
        },

        # =================================================
        # Live Status
        # =================================================

        "live": {

            "guardian": True,

            "scanner": True,

            "blueprint": self.blueprint.is_ready(),

            "mapper": self.mapper.is_ready(),

            "locator": self.locator.is_ready(),

            "dependency_graph": self.dependency_graph.is_ready(),

            "integration_checker":
                self.integration_checker.is_ready(),

            "error_intelligence":
                self.error_intelligence.is_ready(),

            "knowledge_base":
                self.knowledge_base.is_ready(),

            "change_planner":
                self.change_planner.is_ready(),

            "auto_patch_engine":
                self.auto_patch_engine.is_ready(),

            "project_memory":
                self.project_memory.is_ready(),

            "live_monitor":
                self.live_monitor.is_ready(),

            "workflow_engine":
                self.workflow_engine.is_ready(),

            "ai_assistant":
                self.ai_assistant.is_ready()

        },

        # =================================================
        # Dashboard Summary
        # =================================================

        "summary": {

            "online": self.is_ready(),

            "healthy": health["health_percent"] >= 80,

            "warnings": pending_count,

            "errors": 0

        }

    }

 # ======================================================
 # Send Complete Report to App
 # ======================================================
     def app_report(self):
        """
        Generate one complete report for the Streamlit App.
        """

        from datetime import datetime
        import traceback

        report = {
            "generated_at": datetime.now().isoformat(),
            "guardian": {},
            "health": {},
            "diagnostics": {},
            "scan": {},
            "recommendation": {},
            "modules": {},
            "issues": [],
            "summary": {}
        }

        # Guardian Dashboard
        try:
            report["guardian"] = self.dashboard_report()
        except Exception as e:
            report["issues"].append({
                "module": "GuardianCore",
                "error": type(e).__name__,
                "message": str(e),
                "traceback": traceback.format_exc()
            })

        # Health
        try:
            report["health"] = self.health_report()
        except Exception as e:
            report["issues"].append({
                "module": "Health",
                "error": type(e).__name__,
                "message": str(e)
            })

        # Diagnostics
        try:
            report["diagnostics"] = self.diagnostics()
        except Exception as e:
            report["issues"].append({
                "module": "Diagnostics",
                "error": type(e).__name__,
                "message": str(e)
            })

        # Project Scan
        try:
            report["scan"] = self.scan_project()
        except Exception as e:
            report["issues"].append({
                "module": "ProjectScanner",
                "error": type(e).__name__,
                "message": str(e)
            })

        # AI Recommendation
        try:
            report["recommendation"] = self.ai_recommendation()
        except Exception as e:
            report["issues"].append({
                "module": "AIRecommendation",
                "error": type(e).__name__,
                "message": str(e)
            })

    # Automatically collect every module report
    for name, obj in self.__dict__.items():

        try:

            if hasattr(obj, "report"):
                report["modules"][name] = obj.report()

            elif hasattr(obj, "diagnostics"):
                report["modules"][name] = obj.diagnostics()

            elif hasattr(obj, "health_report"):
                report["modules"][name] = obj.health_report()

            elif hasattr(obj, "is_ready"):
                report["modules"][name] = {
                    "ready": obj.is_ready()
                }

        except Exception as e:

            report["issues"].append({
                "module": name,
                "error": type(e).__name__,
                "message": str(e)
            })

    # ==========================================
    # App Status
    # ==========================================

    report["app"] = {
        "display": True,
        "download": True,
        "preview": True,
        "generated": True,
        "generated_at": report["generated_at"]
    }

    # ==========================================
    # Summary
    # ==========================================

    report["summary"] = {
        "guardian_ready": self.is_ready(),
        "health_percent": report["health"].get("health_percent", 0),
        "total_modules": len(report["modules"]),
        "total_issues": len(report["issues"]),
        "generated_at": report["generated_at"],
        "status": "READY" if self.is_ready() else "WARNING"
    }

    return report
