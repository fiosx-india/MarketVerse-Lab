import streamlit as st
import json
import json
import os
import time
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

    guardian._last_scan = None
        report = guardian.scan_project(".")
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
    st.divider()
    st.subheader("💾 Auto Report Storage")

    auto_save = st.checkbox(
        "Enable Automatic Report Saving",
        value=True
    )

    interval = st.selectbox(
        "Save Interval",
        [
            "5 Minutes",
            "15 Minutes",
            "30 Minutes",
            "1 Hour"
        ],
        index=3
    )

    report_folder = st.text_input(
        "Report Folder",
        value="reports"
    )

    if auto_save:
        os.makedirs(report_folder, exist_ok=True)
        st.success(f"✅ Auto Save Enabled ({interval})")
        report_file = os.path.join(report_folder, "latest_report.json")

        if "report" in locals():
            with open(report_file, "w", encoding="utf-8") as f:
                json.dump(report, f, indent=4, ensure_ascii=False, default=str)

    if st.button("💾 Save Settings"):
        settings = {
            "auto_save": auto_save,
            "interval": interval,
            "report_folder": report_folder
        }

        with open("settings.json", "w") as f:
            json.dump(settings, f, indent=4)

        st.success("Settings Saved Successfully")
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
    report = guardian.app_report()

    st.success("✅ Guardian Core Connected")
    score = report.get("score", {})

    st.metric(
        "Guardian Score",
        f"{score.get('score', 0)}%"
    )

    st.write(
        "Signal:",
        score.get("signal", "UNKNOWN")
    )

    # ---------------- Basic Information ----------------

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🛡️ Guardian",
            report["guardian"]["name"]
        )

    with col2:
        st.metric(
            "📦 Version",
            report["guardian"]["version"]
        )

    st.divider()

    # ---------------- Health Metrics ----------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "❤️ Health",
            f"{report['guardian']['health']}%"
        )

    with col2:
        st.metric(
    "🧩 Ready Modules",
    f"{report['guardian']['ready_modules']}/{report['guardian']['total_modules']}"
        )

    with col3:
        st.metric(
            "📡 Status",
            report["guardian"]["status"]
        )

    st.divider()

    # ---------------- Recommendation ----------------

    st.subheader("🤖 AI Recommendation")
    st.json(report["recommendation"])

    st.divider()

    # ---------------- Module Status ----------------

    st.subheader("📋 Module Status")

    module_table = []

    for module, state in report["guardian"]["modules"].items():

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

Guardian Name   : {report["guardian"]["name"]}
Version         : {report["guardian"]["version"]}

Status          : {report["guardian"]["status"]}
Health          : {report["guardian"]["health"]}%

Ready Modules   : {report["guardian"]["ready_modules"]}
Total Modules   : {report["guardian"]["total_modules"]}

Recommendation  : {report["guardian"]["recommendation"]}

Last Scan       : {report["generated_at"]}

==============================
MODULE STATUS
==============================

"""

    for module, state in report["guardian"]["modules"].items():

        ready = (
            state.get("ready", False)
            if isinstance(state, dict)
            else bool(state)
        )

        report_text += (
            f"{module:<30}"
            f"{'✅ Ready' if ready else '❌ Waiting'}\n"
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
    st.code(str(e))

if st.button("📄 Generate Guardian Report", key="guardian_report_btn"):

    if "guardian" not in locals():
        st.error("Guardian Core is not initialized.")
        st.stop()

    try:

        report = guardian.app_report()

        report_text = json.dumps(
            report,
            indent=4,
            ensure_ascii=False
        )

        st.success("✅ Guardian Report Generated Successfully")

        # ==========================================
        # Report Preview
        # ==========================================

        st.subheader("📄 Report Preview")

        st.text_area(
            "Guardian Diagnostic Report",
            report_text,
            height=500
        )

        # ==========================================
        # Expandable JSON View
        # ==========================================

        with st.expander("🔍 Open Full Report", expanded=False):
            st.json(report)

        # ==========================================
        # Guardian Validation
        # ==========================================

        if "validation" in report:

            st.subheader("🛡 Guardian Validation")
            st.json(report["validation"])

        # ==========================================
        # Guardian Score
        # ==========================================

        if "score" in report:

            st.subheader("📊 Guardian Score")

            score = report["score"]

            st.metric(
                "Guardian Score",
                score["score"]
            )

            st.success(
                f"Signal : {score['signal']}"
            )

        # ==========================================
        # Download Buttons
        # ==========================================

        st.download_button(
            label="⬇ Download Guardian Report (.json)",
            data=report_text,
            file_name="guardian_report.json",
            mime="application/json",
            key="guardian_download_json"
        )

        st.download_button(
            label="⬇ Download Guardian Report (.txt)",
            data=report_text,
            file_name="guardian_report.txt",
            mime="text/plain",
            key="guardian_download_txt"
        )

    except Exception as e:

        st.error("❌ Failed to Generate Guardian Report")
        st.code(str(e))
        
