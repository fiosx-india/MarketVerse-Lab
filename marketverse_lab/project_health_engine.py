"""
MarketVerse Lab
project_health_engine.py

Purpose:
Analyze overall project health and report
missing components, connections, and readiness.
"""

from pathlib import Path
import ast


class ProjectHealthEngine:

    def __init__(self):

        self.guardian = None
        self.report_data = {}

    # ----------------------------------------

    def connect_guardian(self, guardian):

        self.guardian = guardian

    # ----------------------------------------
    # Scan Project
    # ----------------------------------------

    def scan(self, root="."):

        root = Path(root)

        py_files = list(root.rglob("*.py"))

        files = []
        imports = []
        errors = []

        for file in py_files:

            files.append(str(file))

            try:

                tree = ast.parse(
                    file.read_text(encoding="utf-8")
                )

                for node in ast.walk(tree):

                    if isinstance(node, ast.Import):

                        for n in node.names:
                            imports.append(n.name)

                    elif isinstance(node, ast.ImportFrom):

                        imports.append(node.module)

            except Exception as e:

                errors.append({
                    "file": str(file),
                    "error": str(e)
                })

        self.report_data = {

            "files": files,
            "imports": sorted(
                list(
                    set(
                        i for i in imports if i
                    )
                )
            ),
            "errors": errors,
            "file_count": len(files),
            "error_count": len(errors)

        }

        return self.report_data

    # ----------------------------------------
    # Guardian Connections
    # ----------------------------------------

    def guardian_status(self):

        if self.guardian is None:

            return {
                "guardian": False
            }

        status = {}

        for name, value in vars(self.guardian).items():

            if name.startswith("_"):
                continue

            status[name] = value is not None

        return status

    # ----------------------------------------
    # Health Score
    # ----------------------------------------

    def health_score(self):

        score = 100

        score -= self.report_data.get(
            "error_count",
            0
        ) * 5

        score = max(score, 0)

        return score

    # ----------------------------------------
    # Full Report
    # ----------------------------------------

    def full_report(self):

        return {

            "files": self.report_data.get(
                "file_count",
                0
            ),

            "syntax_errors": self.report_data.get(
                "error_count",
                0
            ),

            "guardian": self.guardian_status(),

            "health_score": self.health_score(),

            "ready": self.is_ready()

        }

    # ----------------------------------------

    def report(self):

        return self.full_report()

    # ----------------------------------------

    def diagnostics(self):

        return {

            "guardian_connected":
                self.guardian is not None,

            "project_scanned":
                bool(self.report_data)

        }

    # ----------------------------------------

    def statistics(self):

        return {

            "files":
                self.report_data.get(
                    "file_count",
                    0
                ),

            "imports":
                len(
                    self.report_data.get(
                        "imports",
                        []
                    )
                ),

            "errors":
                self.report_data.get(
                    "error_count",
                    0
                )

        }

    # ----------------------------------------

    def reset(self):

        self.report_data.clear()

        return True

    # ----------------------------------------

    def is_ready(self):

        return self.guardian is not None

    # ----------------------------------------

    def __str__(self):

        return (
            f"ProjectHealthEngine("
            f"score={self.health_score()}%)"
        )

    __repr__ = __str__


import streamlit as st
import ast
import json
from pathlib import Path

# Mock classes to ensure safe standalone runtime execution if imports are local
try:
    from guardian_core import GuardianCore
    from project_health_engine import ProjectHealthEngine
except ImportError:
    # Fallback to local declarations if running directly inside the web runner script
    class ProjectHealthEngine:
        def __init__(self):
            self.guardian = None
            self.report_data = {}
        def connect_guardian(self, guardian):
            self.guardian = guardian
        def scan_file_content(self, name, content):
            imports = []
            errors = []
            try:
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for n in node.names: imports.append(n.name)
                    elif isinstance(node, ast.ImportFrom):
                        imports.append(node.module)
            except SyntaxError as e:
                errors.append({"file": name, "error": str(e), "line": e.lineno, "text": e.text})
            except Exception as e:
                errors.append({"file": name, "error": str(e), "line": "Unknown", "text": ""})
            
            self.report_data = {
                "files": [name], "imports": sorted(list(set(i for i in imports if i))),
                "errors": errors, "file_count": 1, "error_count": len(errors)
            }
            return self.report_data
        def guardian_status(self):
            if not self.guardian: return {"guardian": False}
            return {name: getattr(self.guardian, name) is not None for name in vars(self.guardian) if not name.startswith("_")}
        def health_score(self):
            return max(100 - (self.report_data.get("error_count", 0) * 5), 0)
        def full_report(self):
            return {
                "files": self.report_data.get("file_count", 0),
                "syntax_errors": self.report_data.get("error_count", 0),
                "guardian": self.guardian_status(),
                "health_score": self.health_score(),
                "ready": self.guardian is not None
            }

    class GuardianCore:
        def __init__(self):
            # Dynamic generation matching core properties seen in your schema
            modules = [
                "blueprint", "locator", "mapper", "dependency_graph", "integration_checker",
                "error_intelligence", "knowledge_base", "change_planner", "auto_patch_engine",
                "project_memory", "live_monitor", "workflow_engine", "ai_assistant", "import_analyzer",
                "guardian_health", "advisor", "risk_analyzer", "impact_analyzer", "change_simulator",
                "rollback_manager", "backup_manager", "version_manager", "recovery_manager",
                "snapshot_manager", "session_manager", "state_manager", "audit_manager",
                "diagnostics_manager", "notification_manager", "policy_manager", "orchestrator",
                "task_scheduler", "event_bus", "plugin_manager", "config_manager", "resource_manager",
                "cache_manager", "security_manager", "metrics_manager", "logger_manager",
                "command_center", "automation_engine", "rule_engine", "report_generator", "project_health_engine"
            ]
            for mod in modules:
                setattr(self, mod, True)

# Initialize Core System Engines
engine = ProjectHealthEngine()
core = GuardianCore()
engine.connect_guardian(core)

# UI Aesthetics Setup
st.title("🚀 MarketVerse Lab")
st.success("Stage 1 : Foundation Ready")
st.markdown("---")
st.subheader("🛡️ Guardian Core - Diagnostic System Scanner")

# Upload targeting system files
uploaded_file = st.file_uploader("Upload System Code File (e.g., guardian_core.py)", type=["py", "json"])

if uploaded_file is not None:
    file_name = uploaded_file.name
    file_content = uploaded_file.read().decode("utf-8")
    
    # Run parsing check via Abstract Syntax Tree (AST) engine rules
    if file_name.endswith('.py'):
        # Pass memory stream data to validation layers
        if hasattr(engine, 'scan_file_content'):
            scan_results = engine.scan_file_content(file_name, file_content)
        else:
            # Inline parsing if strict structural limitations apply to framework execution
            scan_results = {"errors": []}
            try:
                ast.parse(file_content)
            except SyntaxError as e:
                scan_results["errors"].append({"file": file_name, "error": str(e), "line": e.lineno, "text": e.text})
        
        # UI rendering decision loop based on parsing verification outcomes
        if scan_results.get("errors"):
            for err in scan_results["errors"]:
                st.error("🚨 **CRITICAL SYNTAX ERROR DETECTED!**")
                st.markdown(f"**Target Location:** File `{err['file']}` has failed verification.")
                st.info(f"📍 **Error Location:** Line number **{err.get('line')}**")
                
                if err.get('text'):
                    st.markdown("**Broken Code Segment:**")
                    st.code(f"{err['text'].strip()}", language="python")
                
                st.markdown("**Parser Error Log:**")
                st.code(f"{err['error']}", language="text")
        else:
            st.success(f"✅ **Verification Success:** `{file_name}` compiled cleanly with 0 compilation faults.")
            
    elif file_name.endswith('.json'):
        try:
            json.loads(file_content)
            st.success(f"✅ **Verification Success:** JSON layout parses cleanly.")
        except json.JSONDecodeError as e:
            st.error("🚨 **JSON LAYOUT EXCEPTION DETECTED!**")
            st.info(f"📍 **Error Location:** Line number **{e.lineno}**, Column {e.colno}")
            st.code(f"Details: {e.msg}", language="text")

    st.markdown("---")
    st.subheader("📊 Engine System Diagnostics")
    
    # Calculate live health metrics based on target scan matrix data profiles
    final_report = engine.full_report()
    st.json(final_report)

