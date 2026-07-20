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
        ("Event Bus", guardian.event_bus),
        ("Plugin Manager", guardian.plugin_manager),
        ("Config Manager", guardian.config_manager),
        ("Resource Manager", guardian.resource_manager),
        ("Cache Manager", guardian.cache_manager),
        ("Security Manager", guardian.security_manager),
        ("Metrics Manager", guardian.metrics_manager),
        ("Logger Manager", guardian.logger_manager),
        ("Command Center", guardian.command_center),
        ("Automation Engine", guardian.automation_engine),
        ("Rule Engine", guardian.rule_engine),
        ("Report Generator", guardian.report_generator),
        ("Project Health Engine", guardian.project_health_engine),
        ("Project Inspector", guardian.project_inspector),
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
    
    st.subheader("Project Inspector")
    st.json(
    guardian.project_inspector_report()
    )

    st.subheader("Event Bus")
    st.json(guardian.event_bus_report())

    st.subheader("Plugin Manager")
    st.json(guardian.plugin_manager_report())

    st.subheader("Config Manager")
    st.json(guardian.config_manager_report())

    st.subheader("Resource Manager")
    st.json(guardian.resource_manager_report())

    st.subheader("Cache Manager")
    st.json(guardian.cache_manager_report())

    st.subheader("Security Manager")
    st.json(guardian.security_manager_report())

    st.subheader("Metrics Manager")
    st.json(guardian.metrics_manager_report())

    st.subheader("Logger Manager")
    st.json(guardian.logger_manager_report())

    st.subheader("Command Center")
    st.json(guardian.command_center_report())

    st.subheader("Automation Engine")
    st.json(guardian.automation_engine_report())

    st.subheader("Rule Engine")
    st.json(guardian.rule_engine_report())

    st.subheader("Report Generator")
    st.json(guardian.report_generator_report())
    
    st.subheader("Project Health Engine")
    st.json(
    guardian.project_health_report()
    )
    
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

    # ==========================================
    # Event Bus
    # ==========================================

    st.subheader("Event Bus")

    event_name = st.text_input(
        "Event Name",
        key="event_name"
    )

    event_data = st.text_input(
        "Event Data",
        key="event_data"
    )

    if st.button("Publish Event"):
        st.json(
            guardian.publish_event(
                event_name,
                event_data
            )
        )

    st.subheader("Event History")
    st.json(
        guardian.event_history()
    )

    # ==========================================
    # Plugin Manager
    # ==========================================

    st.subheader("Plugin Manager")

    plugin_name = st.text_input(
        "Plugin Name",
        key="plugin_name"
    )

    if st.button("Load Plugin"):
        st.json(
            guardian.load_plugin(plugin_name)
        )

    st.subheader("Plugins")
    st.json(
        guardian.plugin_list()
    )

    # ==========================================
    # Config Manager
    # ==========================================

    st.subheader("Config Manager")

    config_key = st.text_input(
        "Config Key",
        key="config_key"
    )

    config_value = st.text_input(
        "Config Value",
        key="config_value"
    )

    if st.button("Save Config"):
        st.json(
            guardian.set_config(
                config_key,
                config_value
            )
        )

    # ==========================================
    # Resource Manager
    # ==========================================

    st.subheader("Resource Manager")

    resource_name = st.text_input(
        "Resource Name",
        key="resource_name"
    )

    resource_value = st.text_input(
        "Resource Value",
        key="resource_value"
    )

    if st.button("Allocate Resource"):
        st.json(
            guardian.allocate_resource(
                resource_name,
                resource_value
            )
        )

    st.subheader("Resource Status")
    st.json(
        guardian.resource_status()
    )

    # ==========================================
    # Cache Manager
    # ==========================================

    st.subheader("Cache Manager")

    cache_key = st.text_input(
        "Cache Key",
        key="cache_key"
    )

    cache_value = st.text_input(
        "Cache Value",
        key="cache_value"
    )

    if st.button("Save Cache"):
        st.json(
            guardian.cache_set(
                cache_key,
                cache_value
            )
        )

    # ==========================================
    # Security Manager
    # ==========================================

    st.subheader("Security Manager")

    if st.button("Run Security Scan"):
        st.json(
            guardian.security_scan()
        )

    # ==========================================
    # Metrics Manager
    # ==========================================

    st.subheader("Metrics Manager")

    if st.button("Show Metrics"):
        st.json(
            guardian.metrics()
        )

    # ==========================================
    # Logger Manager
    # ==========================================

    st.subheader("Logger Manager")

    log_level = st.selectbox(
        "Log Level",
        ["INFO", "WARNING", "ERROR"],
        key="log_level"
    )

    log_message = st.text_input(
        "Log Message",
        key="log_message"
    )

    if st.button("Write Log"):
        st.json(
            guardian.log(
                log_level,
                log_message
            )
        )

    # ==========================================
    # Command Center
    # ==========================================

    st.subheader("Command Center")

    command = st.text_input(
        "Command",
        key="command"
    )

    if st.button("Execute Command"):
        st.json(
            guardian.execute_command(command)
        )

    # ==========================================
    # Automation Engine
    # ==========================================

    st.subheader("Automation Engine")

    automation_name = st.text_input(
        "Automation Name",
        key="automation_name"
    )

    if st.button("Run Automation"):
        st.json(
            guardian.run_automation(
                automation_name
            )
        )

    # ==========================================
    # Rule Engine
    # ==========================================

    st.subheader("Rule Engine")

    if st.button("Evaluate Rules"):
        st.json(
            guardian.evaluate_rules()
        )

    # ==========================================
    # Report Generator
    # ==========================================

    st.subheader("Report Generator")

    if st.button("Generate Report"):
        st.json(
            guardian.generate_report()
        )

    # ==========================================
    # Project Health Engine
    # ==========================================

    st.divider()

    st.header("🩺 Project Health Engine")

    health_root = st.text_input(
        "Health Scan Root",
        value=".",
        key="health_root"
    )

    if st.button("Run Project Health Scan"):

        guardian.project_health_scan(health_root)

        st.subheader("Health Report")
        st.json(
            guardian.project_health_report()
        )

        st.subheader("Statistics")
        st.json(
            guardian.project_health_statistics()
        )

        st.subheader("Diagnostics")
        st.json(
            guardian.project_health_diagnostics()
        )

    # ==========================================
    # Project Scanner
    # ==========================================

    st.divider()

    st.header("🔍 Project Scanner")

    project_root = st.text_input(
        "Project Root",
        value="."
    )

    if st.button("Scan Project"):
        st.json(
            guardian.scan_project(project_root)
        )

    st.divider()

    st.header("🔎 Project Inspector")

    inspect_root = st.text_input(
        "Inspection Root",
        value=".",
        key="inspect_root"
    )

    if st.button("Run Project Inspection"):

        st.json(
            guardian.inspect_project(inspect_root)
        )

        st.subheader("Inspection Report")

        st.json(
            guardian.project_inspector_report()
        )


except Exception as e:
    st.error("Guardian Core Failed")
    st.code(str(e))
    st.stop()
