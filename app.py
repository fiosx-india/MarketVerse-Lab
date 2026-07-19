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
        ("Version Manager", guardian.version_manager),
        ("Recovery Manager", guardian.recovery_manager),
        ("Snapshot Manager", guardian.snapshot_manager),
        ("Session Manager", guardian.session_manager),
        ("State Manager", guardian.state_manager),
        ("Audit Manager", guardian.audit_manager),
        ("Diagnostics Manager", guardian.diagnostics_manager),
        ("Notification Manager", guardian.notification_manager),
        ("Policy Manager", guardian.policy_manager),
        ("Orchestrator", guardian.orchestrator),
        ("Task Scheduler", guardian.task_scheduler),
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
    

    st.subheader("Policy Manager")
    st.json(guardian.policy_report())
    
    st.subheader("Orchestrator")
    st.json(
    guardian.orchestrator_report()
    )

    st.subheader("Task Scheduler")
    st.json(
    guardian.task_scheduler_report()
    )

    st.subheader("Notification Manager")
    st.json(guardian.notification_report())
    
    st.subheader("Diagnostics Manager")
    st.json(guardian.diagnostics_report())

    st.subheader("Audit Manager")
    st.json(guardian.audit_report())

    st.subheader("State Manager")
    st.json(guardian.state_report())
    
    st.subheader("Session Manager")
    st.json(guardian.session_report())
    
    st.subheader("Snapshot Manager")
    st.json(guardian.snapshot_report())
    
    st.subheader("Recovery Manager")
    st.json(guardian.recovery_report())
    
    st.subheader("Version Manager")
    st.json(guardian.version_report())
    
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

    st.subheader("Backup Manager")

    backup_file = st.text_input(
        "Backup Target File",
         key="backup_file"
    )

    if st.button("Create Backup"):
        st.json(
            guardian.backup(
                backup_file
            )
        )

    st.subheader("Recovery Manager")

    reason = st.text_input(
        "Recovery Reason",
        key="recovery_reason"
    )

    if st.button("Recover Project"):
        st.json(
            guardian.recover(reason)
        )

    st.subheader("Session Manager")

    session_name = st.text_input(
        "Session Name",
        key="session_name"
    )

    if st.button("Create Session"):
        st.json(
            guardian.create_session(session_name)
        )

    if st.button("Load Session"):
        st.json(
            guardian.load_session(session_name)
        )

    st.subheader("State Manager")

    state = st.selectbox(
        "Project State",
        [
            "IDLE",
            "RUNNING",
            "RECOVERING",
            "FAILED",
            "COMPLETED"
        ]
    )

    if st.button("Update State"):
        st.json(
            guardian.set_state(state)
        )
    st.subheader("Audit Manager")

    audit_action = st.text_input(
        "Audit Action"
    )

    audit_details = st.text_input(
        "Audit Details"
    )

    if st.button("Create Audit Log"):
        st.json(
            guardian.audit(
                audit_action,
            audit_details
            )
        )

    st.subheader("Diagnostics Manager")

    if st.button("Run Diagnostics"):
        st.json(
            guardian.diagnostics()
        )

    st.subheader("Diagnostics Report")
    st.json(
        guardian.diagnostics_report()
    )

    st.subheader("Notification Manager")

    title = st.text_input("Notification Title")

    message = st.text_input("Notification Message")

    level = st.selectbox(
        "Level",
        [
            "INFO",
            "SUCCESS",
            "WARNING",
            "ERROR"
        ]
    )

    if st.button("Send Notification"):
        st.json(
            guardian.notify(
                title,
                message,
                level
            )
        )

    st.subheader("Notification History")
    st.json(
        guardian.notification_history()
    )


    st.subheader("Task Scheduler")

task_name = st.text_input(
    "Task Name",
    key="task_name"
)

if st.button("Add Task"):
    st.json(
        guardian.add_task(task_name)
    )

if st.button("Run Next Task"):
    st.json(
        guardian.run_next_task()
    )

st.subheader("Pending Tasks")
st.json(
    guardian.pending_tasks()
)
    # ==========================================
    # Policy Manager
    # ==========================================

    st.subheader("Policy Manager")

    policy_name = st.text_input(
        "Policy Name",
        key="policy_name"
    )

    policy_value = st.text_input(
        "Policy Value",
        key="policy_value"
    )

    if st.button("Save Policy"):
        st.json(
            guardian.add_policy(
                policy_name,
                policy_value
            )
        )

    st.subheader("Policy History")
    st.json(
        guardian.policy_history()
    )

    remove_name = st.text_input(
        "Remove Policy",
        key="remove_policy"
    )

    if st.button("Delete Policy"):
        st.json(
            guardian.remove_policy(remove_name)
        )
        
except Exception as e:
    st.error("Guardian Core Failed")
    st.code(str(e))
    st.stop()
