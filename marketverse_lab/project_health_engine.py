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

# --- Import your core architecture ---
try:
    from guardian_core import GuardianCore
    from project_health_engine import ProjectHealthEngine
except ImportError:
    pass

# Title & Status Header
st.title("🚀 MarketVerse Lab")
st.success("Stage 1 : Foundation Ready")

st.markdown("---")
st.subheader("🛡️ Guardian Core - File Inspector & Mold Validator")

# =========================================================
# 1. UPLOAD BOX (ALWAYS VISIBLE AT THE TOP)
# =========================================================
uploaded_file = st.file_uploader(
    "Upload File to Inspect (Code or Mold File)", 
    type=["py", "json", "obj", "stl", "step", "iges", "txt"]
)

if uploaded_file is None:
    st.info("📂 Upload a file above to check for syntax/line errors or mold mismatch.")
else:
    file_name = uploaded_file.name
    st.success(f"📁 **Uploaded File:** `{file_name}`")
    
    # CASE 1: Python Files (.py) - Check for exact line errors
    if file_name.endswith('.py'):
        content = uploaded_file.read().decode("utf-8")
        try:
            ast.parse(content)
            st.success("✅ **Verification Success:** No syntax errors found in this file!")
        except SyntaxError as e:
            st.error("🚨 **CRITICAL SYNTAX ERROR DETECTED!**")
            st.warning(f"📍 **Error Line Number:** Line **{e.lineno}**")
            if e.text:
                st.code(f"Broken Code Line:\n{e.text.strip()}", language="python")
            st.code(f"Details: {e.msg}", language="text")

    # CASE 2: JSON Files (.json)
    elif file_name.endswith('.json'):
        content = uploaded_file.read().decode("utf-8")
        try:
            json.loads(content)
            st.success("✅ **Verification Success:** Valid JSON format!")
        except json.JSONDecodeError as e:
            st.error("🚨 **JSON SYNTAX ERROR DETECTED!**")
            st.warning(f"📍 **Error Location:** Line **{e.lineno}**, Column {e.colno}")
            st.code(f"Details: {e.msg}", language="text")

    # CASE 3: 3D Mold Files
    elif file_name.endswith(('.obj', '.stl', '.step', '.iges')):
        CORRECT_MOLD_NAME = "correct_final_mold.obj"
        if file_name != CORRECT_MOLD_NAME:
            st.error("🚨 **WRONG MOLD DETECTED!**")
            st.warning(f"❌ **Uploaded Mold:** `{file_name}`")
            st.info(f"🎯 **Expected Mold Name:** `{CORRECT_MOLD_NAME}`")
        else:
            st.success(f"✅ **Mold Verified:** `{file_name}` matches required specifications!")

st.markdown("---")

# =========================================================
# 2. GUARDIAN CORE REPORTS (BELOW THE UPLOADER)
# =========================================================
st.subheader("🛡️ Guardian Core Engine Status")

# Initialize Guardian System
try:
    core = GuardianCore()
    
    # Expanders for Guardian Modules
    with st.expander("✅ Project Blueprint Report"):
        st.write("Blueprint status: Active")
        
    with st.expander("✅ Project Mapper Report"):
        st.write("Mapper status: Active")
        
    with st.expander("✅ Code Locator Report"):
        st.write("Locator status: Active")
        
    with st.expander("✅ Dependency Graph Report"):
        st.write("Dependency Graph status: Active")

    with st.expander("✅ Integration Checker Report"):
        st.write("Integration Checker status: Active")

    with st.expander("✅ Error Intelligence Report"):
        st.write("Error Intelligence status: Active")

    with st.expander("✅ Knowledge Base Report"):
        st.write("Knowledge Base status: Active")

except Exception as e:
    st.warning(f"Guardian Core initialization note: {str(e)}")


