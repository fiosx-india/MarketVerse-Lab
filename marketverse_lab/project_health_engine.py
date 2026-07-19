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
import traceback
import sys

# UI Setup matching your application's clean aesthetic
st.title("🚀 MarketVerse Lab")
st.success("Stage 1 : Foundation Ready")

st.markdown("---")
st.subheader("🛡️ Guardian Core - Advanced Line Error Inspector")

# File uploader targeting code or configuration files
uploaded_file = st.file_uploader("Upload File to Scan for Line Errors", type=["py", "json", "txt"])

if uploaded_file is not None:
    file_name = uploaded_file.name
    file_content = uploaded_file.read().decode("utf-8")
    
    # --- Case 1: Checking JSON Files ---
    if file_name.endswith('.json'):
        import json
        try:
            json.loads(file_content)
            st.success(f"✅ **Success:** `{file_name}` has zero syntax errors!")
        except json.JSONDecodeError as e:
            st.error("🚨 **SYNTAX ERROR DETECTED!**")
            st.warning(f"📁 **File:** `{file_name}`")
            st.info(f"📍 **Error Location:** Line number **{e.lineno}**, Column {e.colno}")
            st.code(f"Details: {e.msg}", language="text")

    # --- Case 2: Checking Python Files ---
    elif file_name.endswith('.py'):
        try:
            compile(file_content, file_name, 'exec')
            st.success(f"✅ **Success:** `{file_name}` has zero syntax errors!")
        except SyntaxError as e:
            st.error("🚨 **SYNTAX ERROR DETECTED!**")
            st.warning(f"📁 **File:** `{file_name}`")
            st.info(f"📍 **Error Location:** Line number **{e.lineno}**")
            if e.text:
                st.code(f"Broken Code Line:\n{e.text.strip()}", language="python")
            st.code(f"Details: {e.msg}", language="text")
            
    # --- Case 3: Generic Text or Rule matching ---
    else:
        # Custom rule checking line-by-line (Example: Flagging any line containing "ERROR_TRIGGER")
        error_lines = []
        lines = file_content.splitlines()
        
        for idx, line in enumerate(lines, start=1):
            if "ERROR_TRIGGER" in line:  # Replace this string with whatever condition makes a line wrong
                error_lines.append(idx)
                
        if error_lines:
            st.error("🚨 **ERRORS FOUND IN FILE CONTENT!**")
            st.warning(f"📁 **File:** `{file_name}`")
            st.info(f"📍 **Failed Line Numbers:** {error_lines}")
        else:
            st.success(f"✅ **Success:** `{file_name}` looks perfectly fine line-by-line.")
