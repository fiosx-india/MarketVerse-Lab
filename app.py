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

    mapper = ProjectMapper()

    # Fast Scan (Stage 1)
    mapper.scan(".")
    mapper.map_folders()
    mapper.map_files()

    st.success("✅ Project Mapper Loaded")

    if hasattr(mapper, "report"):
        st.json(mapper.report())
    else:
        st.write(mapper)

except Exception as e:
    st.error("❌ Project Mapper Failed")
    st.exception(e)
