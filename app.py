import streamlit as st

st.set_page_config(
    page_title="MarketVerse Lab",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 MarketVerse Lab")
st.caption("Guardian Development Platform")

st.sidebar.title("🛡 Guardian")

menu = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Home",
        "🤖 Guardian",
        "📂 Project Scanner",
        "📄 Reports",
        "🧪 Testing",
        "📜 Logs",
        "⚙ Settings"
    ]
)

st.divider()

# ---------------- HOME ----------------

if menu == "🏠 Home":

    st.success("MarketVerse Lab Running Successfully")

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("📁 Files","--")
    col2.metric("📂 Folders","--")
    col3.metric("❤️ Health","--")
    col4.metric("⚠ Errors","0")

    st.divider()

    st.subheader("📋 System Status")

    st.json({
        "Guardian":"🟢 Ready",
        "Scanner":"🟢 Ready",
        "Reports":"🟢 Ready",
        "AI":"🟢 Ready"
    })

# ---------------- GUARDIAN ----------------

elif menu == "🤖 Guardian":

    st.header("Guardian")
    st.info("Guardian Engine Ready")

# ---------------- PROJECT SCANNER ----------------

elif menu == "📂 Project Scanner":

    st.header("Project Scanner")

    if st.button("🔍 Scan Project"):
        st.info("Scanner Module will run here.")

# ---------------- REPORT ----------------

elif menu == "📄 Reports":

    st.header("Project Report")

    if st.button("Generate Report"):
        st.info("Report Generator Module")

    if st.button("Download Report"):
        st.success("Report Ready")

# ---------------- TEST ----------------

elif menu == "🧪 Testing":

    st.header("Testing")
    st.info("Testing Environment")

# ---------------- LOGS ----------------

elif menu == "📜 Logs":

    st.header("Logs")
    st.info("System Logs")

# ---------------- SETTINGS ----------------

elif menu == "⚙ Settings":

    st.header("Settings")
    st.info("Configuration")

# ============================
# SCORE REPORT
# ============================

st.divider()
st.subheader("📊 Score Report")

st.info("Score Report is integrated into Guardian Core.")

st.success("✅ Score System Ready")
# ==========================================================
# GUARDIAN CORE DASHBOARD
# ==========================================================

st.divider()
st.subheader("🛡️ Guardian Core")

try:
    from marketverse_lab.guardian_core import GuardianCore

    guardian = GuardianCore()
    report = guardian.dashboard_report()

    st.success("✅ Guardian Core Connected")

    # ---------------- Basic Information ----------------

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🛡️ Guardian",
            report.get("name", "Guardian Core")
        )

    with col2:
        st.metric(
            "📦 Version",
            report.get("version", "1.0.0")
        )

    st.divider()

    # ---------------- Health Metrics ----------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "❤️ Health",
            f"{report['health']}%"
        )

    with col2:
        st.metric(
            "🧩 Ready Modules",
            f"{report['ready_modules']}/{report['total_modules']}"
        )

    with col3:
        st.metric(
            "📡 Status",
            report["status"]
        )

    st.divider()

    # ---------------- Recommendation ----------------

    st.subheader("🤖 AI Recommendation")
    st.info(report["recommendation"])

    st.divider()

    # ---------------- Module Status ----------------

    st.subheader("📋 Module Status")

    module_table = []

    for module, state in report["modules"].items():

        module_table.append({
            "Module": module,
            "Status": "✅ Ready" if state else "❌ Waiting"
        })

    st.table(module_table)

    st.divider()

    # ---------------- Project Scan ----------------

    if "scan_report" in report:

        st.subheader("📂 Project Scan")

        st.json(report["scan_report"])

    # ---------------- AI Recommendation Report ----------------

    if "ai_recommendation" in report:

        st.subheader("🧠 AI Analysis")

        st.json(report["ai_recommendation"])

    st.divider()

    # ---------------- Full Guardian Report ----------------

    report_text = f"""
==============================
     GUARDIAN CORE REPORT
==============================

Guardian Name   : {report.get('name','Guardian Core')}
Version         : {report.get('version','1.0.0')}

Status          : {report['status']}
Health          : {report['health']}%

Ready Modules   : {report['ready_modules']}
Total Modules   : {report['total_modules']}

Recommendation  : {report['recommendation']}

Last Scan       : {report['last_scan']}

==============================
MODULE STATUS
==============================

"""

    for module, state in report["modules"].items():

        report_text += (
            f"{module:<30}"
            f"{'✅ Ready' if state else '❌ Waiting'}\n"
        )

    report_text += "\n==============================\n"
    report_text += "Generated by Guardian Core\n"
    report_text += "MarketVerse Lab\n"

    st.subheader("📄 Guardian Report")

    st.text_area(
        "Guardian Core Report",
        report_text,
        height=350
    )

    st.code(
        report_text,
        language="text"
    )

    st.download_button(
        label="📥 Download Guardian Report",
        data=report_text,
        file_name="guardian_core_report.txt",
        mime="text/plain"
    )

except ModuleNotFoundError as e:

    st.warning("🟡 Guardian Core Module Not Found")
    st.code(str(e))

except AttributeError as e:

    st.warning("🟡 dashboard_report() not available")
    st.code(str(e))

except Exception as e:

    st.error("🔴 Guardian Core Error")
    
# ======================================================
# Guardian Diagnostic Report
# ======================================================

import json
from datetime import datetime

def export_diagnostic_report(self, output_file="guardian_report.json"):

    dashboard = self.dashboard_report()
    diagnostics = self.diagnostics()
    health = self.health_report()
    scan = self.scan_project()

    report = {
        "generated_at": datetime.now().isoformat(),

        "guardian": {
            "name": dashboard.get("name"),
            "version": dashboard.get("version"),
            "status": dashboard.get("status"),
            "health": dashboard.get("health")
        },

        "summary": {
            "ready_modules": dashboard.get("ready_modules"),
            "pending_modules": dashboard.get("pending_modules"),
            "total_modules": dashboard.get("total_modules"),
            "recommendation": dashboard.get("recommendation")
        },

        "diagnostics": diagnostics,

        "scan_report": scan,

        "issues": self.error_intelligence.report(),

        "dependencies": self.dependency_graph.report(),

        "integration": self.integration_checker.report(),

        "memory": self.project_memory.report(),

        "knowledge": self.knowledge_base.report(),

        "planner": self.change_planner.report()
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(
            report,
            f,
            indent=4,
            ensure_ascii=False
        )

    return output_file

st.divider()
st.subheader("📋 Guardian Diagnostic Report")

if st.button("📄 Generate Guardian Report"):

    report_file = guardian.export_diagnostic_report()

    with open(report_file, "r", encoding="utf-8") as f:
        report_text = f.read()

    st.success("✅ Report Generated Successfully")

    # Screen-ல் முழு Report
    st.code(report_text, language="json")

    # Download Button
    st.download_button(
        label="⬇ Download Guardian Report",
        data=report_text,
        file_name="guardian_report.json",
        mime="application/json"
    )
