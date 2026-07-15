import streamlit as st

st.set_page_config(
    page_title="MarketVerse Lab",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 MarketVerse Lab")
st.success("Stage 1 : Foundation Ready")

st.divider()

st.header("📘 Project Blueprint")

try:
    from marketverse_lab.project_blueprint import ProjectBlueprint

    blueprint = ProjectBlueprint()
    blueprint.build(".")

    st.success("✅ Project Blueprint Loaded")

    if hasattr(blueprint, "report"):
        st.json(blueprint.report())
    else:
        st.write(blueprint)

except Exception as e:
    st.error("❌ Project Blueprint Failed")
    st.code(str(e))
