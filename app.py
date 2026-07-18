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
        ("Project Blueprint", guardian.blueprint),
        ("Project Mapper", guardian.mapper),
        ("Code Locator", guardian.locator),
        ("Dependency Graph", guardian.dependency_graph),
        ("Integration Checker", guardian.integration_checker),
        ("Error Intelligence", guardian.error_intelligence),
        ("Knowledge Base", guardian.knowledge_base),
        ("Change Planner", guardian.change_planner),
        ("Auto Patch Engine", guardian.auto_patch_engine),
        ("Project Memory", guardian.project_memory),
        ("Live Monitor", guardian.live_monitor),
        ("Workflow Engine", guardian.workflow_engine),
        ("AI Assistant", guardian.ai_assistant),
        ("Import Analyzer", guardian.import_analyzer),
        ("Guardian Health", guardian.guardian_health),
        ("Project Advisor", guardian.advisor),
        ("Risk Analyzer", guardian.risk_analyzer),
        ("Impact Analyzer", guardian.impact_analyzer),
        ("Change Simulator", guardian.change_simulator),
        ("Rollback Manager", guardian.rollback_manager),
        ("Backup Manager", guardian.backup_manager),
        
    ]

    guardian_ready = True

    for name, module in modules:

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

    st.divider()
    st.header("📊 Guardian Summary")
    
    st.subheader("Backup Manager")
    st.json(guardian.backup_report())
    
    st.subheader("Rollback Manager")
    st.json(guardian.rollback_report())

    st.subheader("Impact Analyzer")
    st.json(guardian.impact_report())
    
    st.subheader("Risk Analyzer")
    st.json(guardian.risk_report())
    
    st.subheader("Project Advisor")
    st.json(guardian.advisor_report())

    st.subheader("Health Report")
    st.json(guardian.health_report())

    st.subheader("Dependency Report")
    st.json(guardian.dependency_report())

    st.subheader("Workflow Report")
    st.json(guardian.workflow_report())

    st.subheader("AI Assistant Report")
    
    st.json(guardian.assistant_report())
    
    st.subheader("Change Simulation")

    file_name = st.text_input("Target File")

    action = st.selectbox(
        "Action",
        ["modify", "create", "delete"]
    )

    if st.button("Simulate"):
        st.json(
            guardian.simulate_change(
                file_name,
                action
            )
        )

    st.subheader("Rollback Preview")

    rollback_file = st.text_input(
        "Rollback Target File",
        key="rollback_file"
    )

    if st.button("Preview Rollback"):
        st.json(
            guardian.rollback_preview(
                rollback_file
            )
        )

    if st.button("Execute Rollback"):
        st.json(
            guardian.rollback(
                rollback_file
            )
        )

except Exception as e:
    st.error("Guardian Core Failed")
    st.code(str(e))
    st.stop()
