
import streamlit as st

st.set_page_config(
    page_title="MarketVerse Lab",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 MarketVerse Lab")
st.success("Stage 1 : Foundation Ready")

# ==========================================
# Guardian Core Gate
# ==========================================

st.divider()
st.header("🛡 Guardian Core")

try:
    from marketverse_lab.guardian_core import GuardianCore

    guardian = GuardianCore()

    modules = [
        ("Guardian Constitution", guardian.constitution),
        ("Health Engine", guardian.health_engine),
        ("File Registry", guardian.file_registry),
        ("Cleanup Engine", guardian.cleanup_engine),
        ("Change Report", guardian.change_report),
    ]

    guardian_ready = True

    for name, module in modules:

        if hasattr(module, "scan"):
            module.scan()

        report = {}

        if hasattr(module, "report"):
            report = module.report()

        if hasattr(module, "is_ready"):
            ready = module.is_ready()
        else:
            ready = True

        if ready:
            st.success(f"✅ {name}")
        else:
            guardian_ready = False
            st.error(f"❌ {name}")

        with st.expander(f"{name} Report"):
            st.json(report)

    if guardian_ready:
        st.success("🛡 Guardian PASS")
    else:
        st.error("🛑 Guardian FAILED")
        st.stop()

except Exception as e:
    st.error("Guardian Core Failed")
    st.code(str(e))
    st.stop()
