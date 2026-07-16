import streamlit as st

st.set_page_config(
    page_title="MarketVerse Lab",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 MarketVerse Lab")
st.success("Stage 1 : Foundation Ready")

# ======================================================
# Project Mapper
# ======================================================

import time
import platform

st.divider()
st.header("🗂️ Project Mapper")

mapper = None
locator = None

try:
    from marketverse_lab.project_mapper import ProjectMapper
    from marketverse_lab.code_locator import CodeLocator

    mapper = ProjectMapper()
    mapper.build(".")

    locator = CodeLocator()
    locator.connect_mapper(mapper)

except Exception as e:
    st.error("❌ Project Mapper Initialization Failed")
    st.code(str(e))

# ======================================================
# Performance Monitor
# ======================================================

st.divider()
st.header("⚡ Performance Monitor")

if st.button("⚡ Open Performance Monitor"):

    start = time.perf_counter()

    with st.spinner("Checking Performance..."):
        time.sleep(0.2)

    load_time = time.perf_counter() - start

    st.success("✅ Performance Monitor Ready")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("⚡ Load Time", f"{load_time:.3f} sec")
        st.metric("🖥 Platform", platform.system())

    with col2:
        st.metric("🐍 Python", platform.python_version())
        st.metric("💻 Machine", platform.machine())

    with st.expander("📋 Performance Report"):
        st.json({
            "status": "Healthy",
            "load_time": round(load_time, 3),
            "platform": platform.system(),
            "python": platform.python_version(),
            "machine": platform.machine()
        })

    if mapper is not None:

        if st.button("🔍 Scan Project"):

            with st.spinner("Scanning Project..."):
                mapper.scan(".")
                mapper.map_folders()
                mapper.map_files()

            st.success("✅ Project Scan Complete")

            report = mapper.report()

            summary = report["summary"]
            validation = report["diagnostics"]["validation"]

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("📁 Folders", summary["folders"])

            with col2:
                st.metric("📄 Files", summary["files"])

            with col3:
                st.metric("🐍 Python Files", summary["python_files"])

            if validation["mapping_complete"]:
                st.success("✅ Project Ready")
            else:
                st.warning("⚠️ Project Not Ready")

            with st.expander("📋 Diagnostics"):
                st.json(report)

    else:
        st.error("❌ Project Mapper is not available.")

# ======================================================
# Code Locator
# ======================================================

st.divider()
st.header("📍 Code Locator")

if st.button("📍 Open Code Locator"):

    if locator is not None:
        st.success("✅ Button Working")
        st.write(locator)
        st.json(locator.diagnostics())
    else:
        st.error("❌ Code Locator is not available.")
