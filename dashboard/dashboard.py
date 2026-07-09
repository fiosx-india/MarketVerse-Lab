import streamlit as st
from scanner import ProjectScanner

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="MarketVerse Lab",
    page_icon="🧠",
    layout="wide"
)

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("🧠 MarketVerse Lab")
st.caption("AI Development Control Center")

st.divider()

# ==========================================================
# SAFE PROJECT SCANNER
# ==========================================================

try:
    scanner = ProjectScanner()
    scan = scanner.scan()

except Exception as e:

    scan = {
        "total_files": 0,
        "python_files": 0,
        "empty_files": [],
        "syntax_errors": [],
        "scan_time": "Scanner Offline"
    }

    st.warning(f"⚠ Scanner Offline : {e}")

# ==========================================================
# TOP DASHBOARD
# ==========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📁 Total Files", scan["total_files"])

with col2:
    st.metric("🐍 Python Files", scan["python_files"])

with col3:
    st.metric("📭 Empty Files", len(scan["empty_files"]))

with col4:
    st.metric("❌ Syntax Errors", len(scan["syntax_errors"]))

st.divider()

# ==========================================================
# LIVE PROJECT STATUS
# ==========================================================

st.subheader("📋 Live Project Status")

status = {
    "Guardian Core": "🟢 Ready",
    "Blueprint": "🟢 Ready",
    "Mapper": "🟢 Ready",
    "Dependency Graph": "🟡 Waiting",
    "AI Assistant": "🟢 Ready",
    "Live Monitor": "🟡 Waiting"
}

st.json(status)

st.divider()

# ==========================================================
# LIVE ERRORS
# ==========================================================

st.subheader("🚨 Live Errors")

if len(scan["syntax_errors"]) == 0:
    st.success("No syntax errors detected.")
else:
    st.error(scan["syntax_errors"])

st.divider()

# ==========================================================
# AI RECOMMENDATION
# ==========================================================

st.subheader("🤖 AI Recommendation")

if len(scan["syntax_errors"]) == 0:
    st.success("Project is ready for module integration.")
else:
    st.warning("Fix syntax errors before integrating new modules.")

st.divider()

# ==========================================================
# PROJECT REPORT
# ==========================================================

st.subheader("📄 Project Report")

report = {
    "Total Files": scan["total_files"],
    "Python Files": scan["python_files"],
    "Empty Files": len(scan["empty_files"]),
    "Syntax Errors": len(scan["syntax_errors"]),
    "Last Scan": scan["scan_time"]
}

st.json(report)

# ==========================================================
# PROJECT REPORT
# ==========================================================

st.subheader("📄 Project Report")

report = {
    "Total Files": scan["total_files"],
    "Python Files": scan["python_files"],
    "Empty Files": len(scan["empty_files"]),
    "Syntax Errors": len(scan["syntax_errors"]),
    "Health Score": (
        "100%"
        if len(scan["syntax_errors"]) == 0
        else f"{max(0, 100 - len(scan['syntax_errors']) * 10)}%"
    ),
    "Last Scan": scan["scan_time"]
}

st.json(report)

st.divider()

# ==========================================================
# FULL PROJECT SUMMARY
# ==========================================================

st.subheader("📊 Full Project Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📁 Total Files", scan["total_files"])

with col2:
    st.metric("🐍 Python Files", scan["python_files"])

with col3:
    health = (
        "100%"
        if len(scan["syntax_errors"]) == 0
        else f"{max(0,100-len(scan['syntax_errors'])*10)}%"
    )
    st.metric("❤️ Project Health", health)

st.divider()

# ==========================================================
# EMPTY FILE REPORT
# ==========================================================

st.subheader("📭 Empty Files")

if scan["empty_files"]:
    st.write(scan["empty_files"])
else:
    st.success("No empty files detected.")

st.divider()

# ==========================================================
# SYNTAX ERROR REPORT
# ==========================================================

st.subheader("🚨 Syntax Error Report")

if scan["syntax_errors"]:
    st.error(scan["syntax_errors"])
else:
    st.success("No syntax errors detected.")

st.divider()

# ==========================================================
# AI SUGGESTIONS
# ==========================================================

st.subheader("🤖 AI Suggestions")

if len(scan["syntax_errors"]) == 0:
    st.success("Project is healthy. Safe to integrate new modules.")
else:
    st.warning("Fix syntax errors before adding new modules.")

if scan["empty_files"]:
    st.info("Some empty files are available. Complete or remove them.")

st.divider()

# ==========================================================
# LIVE PROJECT SCANNER
# ==========================================================

st.subheader("📂 Live Project Scanner")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Files", scan["total_files"])
c2.metric("Python", scan["python_files"])
c3.metric("Empty", len(scan["empty_files"]))
c4.metric("Last Scan", scan["scan_time"])

st.divider()

# ==========================================================
# EXPORT REPORT
# ==========================================================

st.subheader("📥 Export Report")

report_text = f"""
MARKETVERSE LAB REPORT

Total Files      : {scan['total_files']}
Python Files     : {scan['python_files']}
Empty Files      : {len(scan['empty_files'])}
Syntax Errors    : {len(scan['syntax_errors'])}
Last Scan        : {scan['scan_time']}
"""

st.download_button(
    "📄 Download Report",
    report_text,
    file_name="marketverse_report.txt",
    mime="text/plain"
)
