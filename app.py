import streamlit as st
import json

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

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📁 Files", "--")
    col2.metric("📂 Folders", "--")
    col3.metric("❤️ Health", "--")
    col4.metric("⚠ Errors", "0")

    st.divider()

    st.subheader("📋 System Status")

    st.json({
        "Guardian": "🟢 Ready",
        "Scanner": "🟢 Ready",
        "Reports": "🟢 Ready",
        "AI": "🟢 Ready"
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

Guardian Name   : {report.get('name', 'Guardian Core')}
Version         : {report.get('version', '1.0.0')}

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

# ==========================================
# PROJECT SCAN SETTINGS
# ==========================================

import streamlit as st

st.subheader("⚙️ Project Scan Settings")

col1, col2 = st.columns(2)

with col1:

    scan_enabled = st.toggle(
        "Project Scan",
        value=True
    )

    auto_scan = st.toggle(
        "Auto Scan",
        value=True
    )

    auto_clear = st.toggle(
        "Auto Clear Reports",
        value=False
    )

    auto_backup = st.toggle(
        "Auto Backup",
        value=False
    )

    live_monitor = st.toggle(
        "Live Monitor",
        value=True
    )

with col2:

    report_limit = st.selectbox(
        "Report Line Limit",
        [100, 500, 1000, 1500, 5000],
        index=3
    )

    download_limit = st.selectbox(
        "Download Line Limit",
        [100, 500, 1000, 1500, 5000],
        index=3
    )

    copy_limit = st.selectbox(
        "Copy Line Limit",
        [100, 500, 1000, 1500],
        index=2
    )

    keep_reports = st.selectbox(
        "Keep Last Reports",
        [1, 5, 10, 20],
        index=1
    )

    clear_time = st.selectbox(
        "Auto Delete Reports",
        [
            "Never",
            "1 Hour",
            "6 Hours",
            "24 Hours"
        ],
        index=1
    )

st.divider()

c1, c2, c3 = st.columns(3)

with c1:

    if st.button("🧹 Clear Reports"):
        st.success("Reports Cleared")

with c2:

    if st.button("🗑 Clear Backup"):
        st.success("Backups Cleared")

with c3:

    if st.button("📋 Clear Logs"):
        st.success("Logs Cleared")
