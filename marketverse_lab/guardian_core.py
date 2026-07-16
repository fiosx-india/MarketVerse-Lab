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
from .guardian.constitution import GuardianConstitution
from .guardian.health import HealthEngine
from .guardian.cleanup import CleanupEngine
from .guardian.registry import FileRegistry
from .guardian.change_report import ChangeReport

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
        self._initialized = False
        self._last_scan = None
        # Guardian Foundation
        self.constitution = GuardianConstitution()
        self.health_engine = HealthEngine()
        self.cleanup_engine = CleanupEngine()
        self.file_registry = FileRegistry()
        self.change_report = ChangeReport()
        # Connect all modules
        self._connect_modules()
        
        modules = [
            ("project_mapper", "Project Mapper"),
            ("code_locator", "Code Locator"),
            ("dependency_graph", "Dependency Graph"),
            ("integration_checker", "Integration Checker"),
            ("error_intelligence", "Error Intelligence"),
            ("knowledge_base", "Knowledge Base"),
            ("change_planner", "Change Planner"),
            ("auto_patch_engine", "Auto Patch Engine"),
            ("project_memory", "Project Memory"),
            ("live_monitor", "Live Monitor"),
            ("workflow_engine", "Workflow Engine"),
            ("ai_assistant", "AI Assistant"),
        ]

        for name, description in modules:
            self.blueprint.register_module(name, description)
            self.blueprint.enable_module(name)
       
        # Build Blueprint
        from pathlib import Path

        project_root = Path(__file__).resolve().parent.parent
        self.blueprint.build(project_root)
        print(self.blueprint.is_ready())
        print(self.blueprint.module_status())
        print(self.blueprint.summary())
        print(self.blueprint.validate())
        print(self.blueprint.integrity_check())

        # Scan Project
        self.mapper.build(".")
        
        # Connect Blueprint
        self.blueprint.connect("project_mapper", self.mapper)
        self.blueprint.connect("code_locator", self.locator)
        self.blueprint.connect("dependency_graph", self.dependency_graph)
        self.blueprint.connect("integration_checker", self.integration_checker)
        self.blueprint.connect("error_intelligence", self.error_intelligence)
        self.blueprint.connect("knowledge_base", self.knowledge_base)
        self.blueprint.connect("change_planner", self.change_planner)
        self.blueprint.connect("auto_patch_engine", self.auto_patch_engine)
        self.blueprint.connect("project_memory", self.project_memory)
        self.blueprint.connect("live_monitor", self.live_monitor)
        self.blueprint.connect("workflow_engine", self.workflow_engine)
        self.blueprint.connect("ai_assistant", self.ai_assistant)
        
        # Connect Locator
        self.locator.connect_blueprint(self.blueprint)
        self.locator.connect_mapper(self.mapper)

        # Build Dependency Graph
        self.dependency_graph.connect_blueprint(self.blueprint)
        self.dependency_graph.connect_mapper(self.mapper)
        self.dependency_graph.build()

        # Scan Monitor
        self.live_monitor.scan_folder(".")

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
            self.ai_assistant,
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

        # ----------------------------------------
        # AI Assistant Connections
        # ----------------------------------------

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

        # ----------------------------------------
        # Integration Checker Connections
        # ----------------------------------------

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

        # ----------------------------------------
        # Change Planner Connections
        # ----------------------------------------

        self.change_planner.connect_integration_checker(
            self.integration_checker
        )

        self.change_planner.connect_error_intelligence(
            self.error_intelligence
        )

        self.change_planner.connect_knowledge_base(
            self.knowledge_base
        )

        # ----------------------------------------
        # Auto Patch Engine Connections
        # ----------------------------------------

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

        # ----------------------------------------
        # Project Memory Connections
        # ----------------------------------------

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

        self.workflow_engine.connect_integration_checker(
        self.integration_checker
        )

        self.workflow_engine.connect_error_intelligence(
        self.error_intelligence
        )

        self.workflow_engine.connect_knowledge_base(
        self.knowledge_base
        )
        
        # ----------------------------------------
        # Scan Project
        # ----------------------------------------

    def scan_project(
        self,
        root="."
    ):

        self.mapper.build(root)
        self.live_monitor.scan_folder(root)

        report = {}

        report["errors"] = (
            self.error_intelligence.report()
            if self.error_intelligence is not None
            else {"status": "ErrorIntelligence not connected."}
        )

        report["blueprint"] = (
            self.blueprint.report()
            if self.blueprint is not None
            else {"status": "ProjectBlueprint not connected."}
        )
        report["mapping"] = (
            self.mapper.report()
            if self.mapper is not None
            else {
                "summary": {
                    "files": 0,
                    "folders": 0,
                    "python_files": 0,
                },
                "status": "ProjectMapper not connected.",
            }
        )

        summary = report["mapping"].get("summary", {})

        report["mapping"]["summary"] = {
            "files": summary.get("files", 0),
            "folders": summary.get("folders", 0),
            "python_files": summary.get("python_files", 0),
        }

        report["dependencies"] = (
            self.dependency_graph.report()
            if self.dependency_graph is not None
            else {"status": "DependencyGraph not connected."}
        )

        report["integration"] = (
            self.integration_checker.report()
            if self.integration_checker is not None
            else {"status": "IntegrationChecker not connected."}
        )

        report["knowledge"] = (
            self.knowledge_base.report()
            if self.knowledge_base is not None
            else {"status": "KnowledgeBase not connected."}
        )

        report["memory"] = (
            self.project_memory.report()
            if self.project_memory is not None
            else {"status": "ProjectMemory not connected."}
        )

        return report
    
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

        backup = self.auto_patch_engine.backup_file(file)

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
            ) if total_modules else 0,
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
            scan = self.scan_project()

            report["scan"] = {
                "files": scan.get("mapping", {}).get("summary", {}).get("files", 0),
                 "folders": scan.get("mapping", {}).get("summary", {}).get("folders", 0),
                "python_files": scan.get("mapping", {}).get("summary", {}).get("python_files", 0),
                "health": "OK"
            }

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

        # ==========================================
        # Automatically collect every module report
        # ==========================================

        report["modules"] = {}

        for name, obj in self.__dict__.items():
            try:
                report["modules"][name] = {
                    "ready": (
                        obj.is_ready()
                        if hasattr(obj, "is_ready")
                        else False
                    ),
                    "type": obj.__class__.__name__
                }

            except Exception:
                report["modules"][name] = {
                    "ready": False,
                    "type": "Unknown"
                }

        # ==========================================
        # Guardian Validation & Score
        # ==========================================

        report["validation"] = self.guardian_validation()
        report["score"] = self.guardian_score()

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
        self._last_scan = report
        
        # ==========================================
        # Summary
        # ==========================================

        report["summary"] = {
            "guardian_ready": self.is_ready(),
            "health_percent": report["health"].get(
                "health_percent", 0
            ),
            "total_modules": len(report["modules"]),
            "total_issues": len(report["issues"]),
            "generated_at": report["generated_at"],
            "status": (
                "READY"
                if self.is_ready()
                else "WARNING"
            )
        }

        return report

    # =====================================================
    # Guardian Structural Validation
    # =====================================================

    def structure_report(self):

        report = {
            "placement": [],
            "wrong_files": [],
            "wrong_position": [],
            "summary": {
                "green": 0,
                "red": 0
            }
        }

        expected = {

            "guardian_core.py": [
                "__init__",
                "_connect_modules",
                "scan_project",
                "dashboard_report",
                "plan_change",
                "apply_patch",
                "auto_scan",
                "diagnostics",
                "health_report",
                "ai_recommendation",
                "is_ready",
                "app_report"
            ]

        }

        # ----------------------------------------
        # Check Placement
        # ----------------------------------------

        for file, functions in expected.items():

            current = self.mapper.function_list(file)

            for index, func in enumerate(functions):

                if func not in current:

                    report["placement"].append({
                        "status": "RED",
                        "function": func,
                        "reason": "Missing"
                    })

                    report["summary"]["red"] += 1

                    continue

                if current.index(func) == index:

                    report["placement"].append({
                        "status": "GREEN",
                        "function": func
                    })

                    report["summary"]["green"] += 1

                else:

                    report["placement"].append({
                        "status": "RED",
                        "function": func,
                        "reason": "Wrong Position"
                    })

                    report["summary"]["red"] += 1

        # ----------------------------------------
        # Wrong File Detection
        # ----------------------------------------

        wrong = self.mapper.find_wrong_files()

        for item in wrong:

            report["wrong_files"].append(item)

        return report

    # =====================================================
    # Guardian Validation
    # =====================================================

    def guardian_validation(self):

        return {

            "structure": self.structure_report(),

            "diagnostics": self.diagnostics(),

            "health": self.health_report(),

            "ready": self.is_ready(),

            "status": (
                "GREEN"
                if self.is_ready()
                else "RED"
            )
        }

    # =====================================================
    # Guardian Score
    # =====================================================

    def guardian_score(self):

        validation = self.guardian_validation()

        score = validation["health"]["health_percent"]

        if validation["structure"]["summary"]["red"] > 0:
            score -= validation["structure"]["summary"]["red"] * 2

        if score < 0:
            score = 0

        return {

    "score": round(score, 2),

    "signal": (
        "🟢 GREEN"
        if score >= 90
        else "🟡 YELLOW"
        if score >= 70
        else "🔴 RED"
    ),

    "health_percent": validation["health"]["health_percent"],

    "ready_modules": validation["health"]["ready_modules"],

    "total_modules": validation["health"]["total_modules"],

    "structure_errors": validation["structure"]["summary"]["red"],

    "validation": validation

}

