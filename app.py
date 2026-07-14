import streamlit as st
import json
import traceback

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

    try:
        from marketverse_lab.guardian_core import GuardianCore

        guardian = GuardianCore()
        report = guardian.app_report()

        scan = report["scan"]
        health = report["health"]

        col1.metric("📁 Files", scan["files"])
        col2.metric("📂 Folders", scan["folders"])
        col3.metric("❤️ Health", f'{health["health_percent"]}%')
        col4.metric("⚠ Errors", len(report["issues"]))

    except Exception:
        col1.metric("📁 Files", "0")
        col2.metric("📂 Folders", "0")
        col3.metric("❤️ Health", "0%")
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

if menu == "🛡 Guardian":

    st.header("Guardian")
    st.info("Guardian Engine Ready")

# ---------------- PROJECT SCANNER ----------------

if menu == "📂 Project Scanner":

    st.header("📂 Project Scanner")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "⚙️ Settings",
        "🔍 Scan",
        "📊 Report",
        "📜 Logs",
        "🤖 AI"
    ])

    with tab1:

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

            auto_refresh = st.toggle(
                "Auto Refresh After Expiry",
                value=True
            )

            force_scan = st.toggle(
                "Force Full Scan",
                value=False
            )

            live_monitor = st.toggle(
                "Live Monitor",
                value=True
            )

        with col2:

            report_expiry = st.selectbox(
                "Report Expiry",
                [
                    "1 Hour",
                    "2 Hours",
                    "6 Hours",
                    "12 Hours"
                ],
                index=3
            )

            scan_interval = st.selectbox(
                "Scan Interval",
                [
                    "Manual",
                    "1 Hour",
                    "2 Hours",
                    "6 Hours",
                    "12 Hours"
                ],
                index=0
            )

            keep_reports = st.selectbox(
                "Keep Reports",
                [
                    1,
                    5,
                    10,
                    20
                ],
                index=1
            )

            download_format = st.selectbox(
                "Download Format",
                [
                    "JSON",
                    "TXT",
                    "Both"
                ],
                index=2
            )

            report_view = st.selectbox(
                "Report View",
                [
                    "Summary",
                    "Detailed"
                ],
                index=0
            )

    st.divider()

    from marketverse_lab.guardian_core import GuardianCore

    guardian = GuardianCore()

    c1, c2, c3 = st.columns(3)

    with c1:

        if st.button("🗑 Clear Expired Reports", use_container_width=True):

            try:
                guardian.project_memory.reset()
                st.success("✅ Expired Reports Cleared")
            except Exception:
                st.error("❌ Failed to Clear Reports")
                st.code(traceback.format_exc())

    with c2:

        if st.button("♻ Reset Scanner Cache", use_container_width=True):

            try:

                if hasattr(guardian, "_last_scan"):
                    guardian._last_scan = None

                st.success("✅ Scanner Cache Reset")

            except Exception:
                st.error("❌ Failed to Reset Cache")
                st.code(traceback.format_exc())

    with c3:

        if st.button("🧹 Clear Logs", use_container_width=True):

            try:

                if hasattr(guardian.live_monitor, "reset"):
                    guardian.live_monitor.reset()

                st.success("✅ Logs Cleared")

            except Exception:
                st.error("❌ Failed to Clear Logs")
                st.code(traceback.format_exc())

    st.divider()

    if scan_enabled:

        if st.button("🔍 Scan Project", use_container_width=True):

            try:

                with st.spinner("🔍 Scanning Project..."):

                    report = guardian.app_report()

                st.success("✅ Project Scan Completed")

                score = report["score"]

                st.subheader("📊 Guardian Score")

                col1, col2, col3, col4 = st.columns(4)

                col1.metric("Guardian Score", score["score"])
                col2.metric("Signal", score["signal"])
                col3.metric("Health", f'{score["health_percent"]}%')
                col4.metric(
                    "Modules",
                    f'{score["ready_modules"]}/{score["total_modules"]}'
                )

                st.divider()

                if report_view == "Summary" and "summary" in report:

                    st.subheader("📋 Report Summary")
                    st.json(report["summary"])

                else:

                    st.subheader("📂 Guardian Report")
                    st.json(report)

            except Exception:

                st.error("❌ Project Scan Failed")
                st.code(traceback.format_exc())

    else:

        st.warning("⚠ Project Scan is Disabled.")

# ---------------- REPORT ----------------

if menu == "📄 Reports":

    st.header("Project Report")

    if st.button("📄 Generate Report"):
        st.info("Report Generator Module")

    if st.button("⬇️ Download Report"):
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

    # ---------------- Health Metrics ----------------

    col1, col2, col3 = st.columns(3)

    col1.metric("❤️ Health", f"{report.get('health', 0)}%")
    col2.metric(
        "🧩 Ready Modules",
        f"{report.get('ready_modules', 0)}/{report.get('total_modules', 0)}"
    )
    col3.metric("📡 Status", report.get("status", "Unknown"))

    st.divider()

    # ---------------- Recommendation ----------------

    st.subheader("🤖 AI Recommendation")
    st.info(report.get("recommendation", "No recommendation available."))

    st.divider()

    # ---------------- Module Status ----------------

    st.subheader("📋 Module Status")

    module_table = [
        {
            "Module": module,
            "Status": "✅ Ready" if state else "❌ Waiting"
        }
        for module, state in report.get("modules", {}).items()
    ]

    if module_table:
        st.table(module_table)
    else:
        st.info("No module information available.")

    st.divider()

    # ---------------- Project Summary ----------------

    st.subheader("📄 Guardian Summary")

    st.json({
        "Health": report.get("health", 0),
        "Status": report.get("status", "Unknown"),
        "Ready Modules": report.get("ready_modules", 0),
        "Total Modules": report.get("total_modules", 0),
        "Recommendation": report.get("recommendation", "")
    })

except ModuleNotFoundError as e:
    st.warning("🟡 Guardian Core Module Not Found")
    st.code(str(e))

except AttributeError as e:
    st.warning("🟡 dashboard_report() not available")
    st.code(str(e))

except Exception as e:
    st.error("🔴 Guardian Core Error")
    st.code(str(e))
