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
# SCORE REPORT (SAFE MODE)
# ============================

st.divider()
st.subheader("📊 Score Report")

try:
    from score import get_score_report

    report = get_score_report()

    st.metric("⭐ Health Score", f"{report['health_score']}%")
    st.metric("📁 Total Files", report["total_files"])
    st.metric("📂 Total Folders", report["total_folders"])

    st.dataframe(report["scan_report"])

    if len(report["errors"]) > 0:
        st.error("🚨 Errors Found")
        st.dataframe(report["errors"])

    if len(report["warnings"]) > 0:
        st.warning("⚠ Warnings")
        st.dataframe(report["warnings"])

    st.success("✅ Score System Connected")

except Exception as e:
    st.warning("⚠ Score System Offline")
    st.code(str(e))

# ==========================================================
# GUARDIAN CORE DASHBOARD
# ==========================================================

st.subheader("🛡️ Guardian Core")

try:
    from guardian.guardian_core import GuardianCore

    guardian = GuardianCore()
    report = guardian.dashboard_report()

    st.success("✅ Guardian Core Connected")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "❤️ Health",
            f"{report['health']}%"
        )

    with col2:
        st.metric(
            "🧩 Ready Modules",
            report["ready_modules"]
        )

    with col3:
        st.metric(
            "📦 Total Modules",
            report["total_modules"]
        )

    st.divider()

    st.subheader("📋 Guardian Core Report")
    st.json(report)

    st.divider()

    st.subheader("📄 Guardian Report")

    report_text = f"""
========== GUARDIAN CORE REPORT ==========

Status           : {report['status']}
Health           : {report['health']}%
Ready Modules    : {report['ready_modules']}
Total Modules    : {report['total_modules']}
Recommendation   : {report['recommendation']}
Last Scan        : {report['last_scan']}

Modules
-----------------------------------------
{report['modules']}
"""

    st.download_button(
        "📥 Download Guardian Report",
        report_text,
        file_name="guardian_core_report.txt",
        mime="text/plain"
    )

except ModuleNotFoundError as e:
    st.warning("🟡 Guardian Core Waiting")
    st.code(str(e))

except AttributeError:
    st.warning("🟡 dashboard_report() method not found")

except Exception as e:
    st.error("🔴 Guardian Core Error")
    st.code(str(e))
