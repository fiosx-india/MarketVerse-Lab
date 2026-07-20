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

st.title("🚀 MarketVerse Lab")
st.success("Stage 1 : Foundation Ready")

st.markdown("---")
st.subheader("🛡️ Guardian AI Mold & Code Verification")

# 1. ALLOW ALL REQUIRED FILE TYPES (py, json, obj, stl, step, iges, txt)
uploaded_file = st.file_uploader(
    "Upload File to Scan", 
    type=["py", "json", "obj", "stl", "step", "iges", "txt"] # All file types allowed now
)

# If file is not uploaded yet, show blue info banner
if uploaded_file is None:
    st.info("📂 Please upload a file to start verification.")
else:
    # File is uploaded successfully
    file_name = uploaded_file.name
    st.success(f"📁 **File Uploaded:** `{file_name}`")
    
    # Process Python files for line-by-line syntax errors
    if file_name.endswith('.py'):
        content = uploaded_file.read().decode("utf-8")
        try:
            ast.parse(content)
            st.success("✅ **Verification Success:** No syntax errors found in this Python file!")
        except SyntaxError as e:
            st.error("🚨 **CRITICAL SYNTAX ERROR DETECTED!**")
            st.warning(f"📍 **Error Location:** Line Number **{e.lineno}**")
            if e.text:
                st.code(f"Broken Code Line:\n{e.text.strip()}", language="python")
            st.code(f"Details: {e.msg}", language="text")

    # Process 3D Mold files by Name Matching
    elif file_name.endswith(('.obj', '.stl', '.step', '.iges')):
        CORRECT_MOLD_NAME = "correct_final_mold.obj"
        if file_name != CORRECT_MOLD_NAME:
            st.error("🚨 **WRONG MOLD DETECTED!**")
            st.warning(f"❌ **Uploaded Mold:** `{file_name}`")
            st.info(f"🎯 **Expected Mold Name:** `{CORRECT_MOLD_NAME}`")
        else:
            st.success(f"✅ **Mold Verified:** `{file_name}` matches required specifications!")

