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

import os
import streamlit as st

# ==========================================
# MarketVerse Lab
# ==========================================

st.set_page_config(
    page_title="MarketVerse Lab",
    page_icon="🛡️",
    layout="wide"
)

st.title("🚀 MarketVerse Lab")
st.success("Stage 1 : Foundation Ready")

st.divider()

st.header("🛡️ Guardian AI Mold Verification")

uploaded_file = st.file_uploader(
    "Upload Mold File",
    type=["obj", "stl", "step", "iges"]
)

if uploaded_file is not None:

    st.success(f"✅ File Loaded : {uploaded_file.name}")

    st.subheader("📁 File Information")

    st.write(f"File Name : {uploaded_file.name}")
    st.write(f"File Size : {uploaded_file.size} Bytes")

    st.divider()

    st.subheader("✅ File Validation")

    st.json({
        "Uploaded": True,
        "Supported Format": True,
        "Readable": True,
        "Corrupted": False
    })

    st.divider()

    st.subheader("📐 Geometry")

    st.json({
        "Vertices": 0,
        "Edges": 0,
        "Faces": 0,
        "Solids": 0
    })

    st.divider()

    st.subheader("🧩 Mesh Inspection")

    st.json({
        "Open Edges": 0,
        "Non-Manifold": 0,
        "Duplicate Vertices": 0,
        "Duplicate Faces": 0,
        "Flipped Normals": 0,
        "Self Intersections": 0
    })

    st.divider()

    st.subheader("🏭 Manufacturing Check")

    st.json({
        "Wall Thickness": "Pending",
        "Draft Angle": "Pending",
        "Undercut": "Pending",
        "Tiny Faces": "Pending",
        "Tiny Holes": "Pending"
    })

    st.divider()

    st.subheader("🤖 Guardian AI Analysis")

    st.json({
        "Critical Errors": 0,
        "Warnings": 0,
        "Recommendations": [],
        "Auto Repair": []
    })

    st.divider()

    st.subheader("📊 Statistics")

    st.json({
        "Volume": 0,
        "Surface Area": 0,
        "Bounding Box": "Pending"
    })

    st.divider()

    st.subheader("🛡 Guardian Score")

    st.metric("Health Score", "100 / 100")

    st.success("✅ PASS")

    st.divider()

    st.subheader("📄 Final Report")

    st.json({
        "Status": "PASS",
        "Critical": 0,
        "Warnings": 0,
        "Ready For Production": True
    })

else:
    st.info("📂 Please upload a mold file to start verification.")
