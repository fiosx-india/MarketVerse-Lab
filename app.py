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

st.divider()
st.header("🗂️ Project Mapper")

try:
    from marketverse_lab.project_mapper import ProjectMapper
    from marketverse_lab.code_locator import CodeLocator

    mapper = ProjectMapper()

    locator = CodeLocator()
    locator.connect_mapper(mapper)

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

except Exception as e:
    st.error("❌ Project Mapper Failed")
    st.code(str(e))
