import streamlit as st
import json
import traceback

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="MarketVerse Lab",
    page_icon="🚀",
    layout="wide"
)

# ==========================================================
# TITLE
# ==========================================================

st.title("🚀 MarketVerse Lab")
st.caption("Guardian Development Platform")

# ==========================================================
# LOAD GUARDIAN (ONLY ONCE)
# ==========================================================

if "guardian" not in st.session_state:

    try:
        from marketverse_lab.guardian_core import GuardianCore

        st.session_state.guardian = GuardianCore()

    except Exception as e:

        st.session_state.guardian = None
        st.session_state.guardian_error = str(e)

guardian = st.session_state.get("guardian")

# ==========================================================
# LOAD REPORT (ONLY WHEN GUARDIAN EXISTS)
# ==========================================================

report = {}

if guardian is not None:

    try:
        report = guardian.app_report()

    except Exception:

        report = {}

# ==========================================================
# SIDEBAR
# ==========================================================

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

# ==========================================================
# HOME
# ==========================================================

if menu == "🏠 Home":

    st.header("🏠 Dashboard")

    if guardian is None:

        st.error("Guardian Core could not be loaded.")

        if "guardian_error" in st.session_state:
            st.code(st.session_state.guardian_error)

        st.stop()

    scan = report.get("scan", {})
    health = report.get("health", {})
    summary = report.get("summary", {})

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📁 Files",
        scan.get("files", 0)
    )

    col2.metric(
        "📂 Folders",
        scan.get("folders", 0)
    )

    col3.metric(
        "❤️ Health",
        f"{health.get('health_percent',0)}%"
    )

    col4.metric(
        "⚠ Issues",
        summary.get("total_issues",0)
    )

    st.divider()

    st.subheader("System Status")

    st.success("🟢 Guardian Online")

    st.json({

        "Guardian":"Ready",

        "Scanner":"Ready",

        "Reports":"Ready",

        "AI":"Ready"

    })
# ==========================================================
# GUARDIAN
# ==========================================================

elif menu == "🤖 Guardian":

    st.header("🛡 Guardian Core")

    if guardian is None:

        st.error("Guardian Core Not Loaded")
        st.stop()

    try:

        dashboard = guardian.dashboard_report()

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "❤️ Health",
            f"{dashboard['health']}%"
        )

        col2.metric(
            "🧩 Modules",
            f"{dashboard['ready_modules']}/{dashboard['total_modules']}"
        )

        col3.metric(
            "📡 Status",
            dashboard["status"]
        )

        st.divider()

        st.subheader("🤖 AI Recommendation")

        st.info(
            dashboard["recommendation"]
        )

        st.divider()

        st.subheader("📋 Module Status")

        module_table = []

        for module, state in dashboard["modules"].items():

            module_table.append({

                "Module": module,

                "Status":
                "✅ Ready"
                if state
                else
                "❌ Waiting"

            })

        st.table(module_table)

    except Exception as e:

        st.error("Guardian Dashboard Failed")

        st.code(str(e))

# ==========================================================
# PROJECT SCANNER
# ==========================================================

elif menu == "📂 Project Scanner":

    st.header("📂 Project Scanner")

    if guardian is None:

        st.error("Guardian Core Not Loaded")
        st.stop()

    st.subheader("⚙ Scan Settings")

    auto_scan = st.toggle(
        "Auto Scan",
        value=True
    )

    live_monitor = st.toggle(
        "Live Monitor",
        value=True
    )

    report_limit = st.selectbox(

        "Report Limit",

        [100, 500, 1000, 5000],

        index=2

    )

    st.divider()

    if st.button(
        "🔍 Scan Project",
        use_container_width=True
    ):

        try:

            report = guardian.app_report()

            score = report["score"]

            st.success(
                "✅ Scan Completed"
            )

            c1, c2, c3, c4 = st.columns(4)

            c1.metric(
                "Guardian Score",
                score["score"]
            )

            c2.metric(
                "Signal",
                score["signal"]
            )

            c3.metric(
                "Health",
                f"{score['health_percent']}%"
            )

            c4.metric(
                "Modules",
                f"{score['ready_modules']}/{score['total_modules']}"
            )

            st.divider()

            st.subheader("📊 Validation")

            st.json(
                report["validation"]
            )

        except Exception as e:

            st.error("Project Scan Failed")

            st.code(str(e))

# ==========================================================
# REPORTS
# ==========================================================

elif menu == "📄 Reports":

    st.header("📄 Guardian Reports")

    if guardian is None:

        st.error("Guardian Core Not Loaded")
        st.stop()

    try:

        report = guardian.app_report()

        st.success("✅ Report Generated")

        # ------------------------------------------
        # Health Summary
        # ------------------------------------------

        health = report["health"]

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Health",
            f"{health['health_percent']}%"
        )

        col2.metric(
            "Ready Modules",
            health["ready_modules"]
        )

        col3.metric(
            "Total Modules",
            health["total_modules"]
        )

        st.divider()

        # ------------------------------------------
        # Scan Summary
        # ------------------------------------------

        st.subheader("📂 Project Summary")

        st.json(report["scan"])

        st.divider()

        # ------------------------------------------
        # Diagnostics
        # ------------------------------------------

        st.subheader("🛡 Diagnostics")

        st.json(report["diagnostics"])

        st.divider()

        # ------------------------------------------
        # Guardian Validation
        # ------------------------------------------

        st.subheader("✅ Validation")

        st.json(report["validation"])

        st.divider()

        # ------------------------------------------
        # Guardian Score
        # ------------------------------------------

        score = report["score"]

        st.subheader("📊 Guardian Score")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Score",
            score["score"]
        )

        c2.metric(
            "Signal",
            score["signal"]
        )

        c3.metric(
            "Structure Errors",
            score["structure_errors"]
        )

        st.divider()

        # ------------------------------------------
        # AI Recommendation
        # ------------------------------------------

        st.subheader("🤖 AI Recommendation")

        st.json(
            report["recommendation"]
        )

        st.divider()

        # ------------------------------------------
        # Complete JSON Report
        # ------------------------------------------

        with st.expander(
            "📄 Full Guardian Report",
            expanded=False
        ):

            st.json(report)

    except Exception as e:

        st.error("Report Generation Failed")

        st.code(str(e))

# ==========================================================
# TESTING
# ==========================================================

elif menu == "🧪 Testing":

    st.header("🧪 Testing")

    if guardian is None:
        st.error("Guardian Core Not Loaded")
        st.stop()

    if st.button("▶ Run Diagnostics", use_container_width=True):

        try:

            diagnostics = guardian.diagnostics()

            st.success("Diagnostics Completed")

            st.json(diagnostics)

        except Exception as e:

            st.error("Diagnostics Failed")

            st.code(str(e))


# ==========================================================
# LOGS
# ==========================================================

elif menu == "📜 Logs":

    st.header("📜 Guardian Logs")

    if guardian is None:
        st.error("Guardian Core Not Loaded")
        st.stop()

    report = guardian.app_report()

    if report["issues"]:

        st.warning(
            f"{len(report['issues'])} Issue(s) Found"
        )

        st.json(report["issues"])

    else:

        st.success("✅ No Errors Found")


# ==========================================================
# SETTINGS
# ==========================================================

elif menu == "⚙ Settings":

    st.header("⚙ Guardian Settings")

    st.checkbox(
        "Enable Auto Scan",
        value=True
    )

    st.checkbox(
        "Enable Live Monitor",
        value=True
    )

    st.checkbox(
        "Enable AI Recommendation",
        value=True
    )

    st.checkbox(
        "Enable Auto Backup",
        value=False
    )

    st.selectbox(
        "Report Limit",
        [100, 500, 1000, 5000],
        index=2
    )

    st.success("Settings Saved")


# ==========================================================
# DOWNLOAD REPORT
# ==========================================================

st.divider()

st.subheader("📥 Export Guardian Report")

if guardian is not None:

    try:

        report = guardian.app_report()

        report_json = json.dumps(
            report,
            indent=4,
            ensure_ascii=False
        )

        st.download_button(

            label="⬇ Download JSON",

            data=report_json,

            file_name="guardian_report.json",

            mime="application/json"

        )

        st.download_button(

            label="⬇ Download TXT",

            data=report_json,

            file_name="guardian_report.txt",

            mime="text/plain"

        )

    except Exception as e:

        st.error("Export Failed")

        st.code(str(e))


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "🚀 MarketVerse Lab | Guardian Development Platform | Version 1.0.0"
          )
