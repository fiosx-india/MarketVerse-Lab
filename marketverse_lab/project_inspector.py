"""
MarketVerse Lab

Main Entry Point

Purpose:
Start the complete MarketVerse AI Foundation
and verify that every core module is connected.
"""

import traceback

from bootstrap import bootstrap_system


def print_status(result):

    print("\n" + "=" * 60)
    print("        MARKETVERSE LAB")
    print("=" * 60)

    print(f"System Status : {result['status']}")
    print(f"Guardian      : {result['guardian']}")
    print(f"Assistant     : {result['assistant']}")
    print(f"Workflow      : {result['workflow']}")
    print(f"Monitor       : {result['monitor']}")

    print("=" * 60)


def diagnostics(system):

    print("\nDiagnostics")
    print("-" * 60)

    modules = {
        "Blueprint": system.guardian.blueprint,
        "Mapper": system.guardian.mapper,
        "Locator": system.guardian.locator,
        "DependencyGraph": system.guardian.dependency_graph,
        "IntegrationChecker": system.guardian.integration_checker,
        "ErrorIntelligence": system.guardian.error_intelligence,
        "KnowledgeBase": system.guardian.knowledge_base,
        "ChangePlanner": system.guardian.change_planner,
        "AutoPatchEngine": system.guardian.auto_patch_engine,
        "ProjectMemory": system.guardian.project_memory,
        "LiveMonitor": system.guardian.live_monitor,
        "WorkflowEngine": system.guardian.workflow_engine,
        "AIAssistant": system.guardian.ai_assistant,
    }

    for name, obj in modules.items():

        if obj is None:
            print(f"[ERROR] {name:<22} NOT CONNECTED")
            continue

        ready = True

        if hasattr(obj, "is_ready"):
            try:
                ready = obj.is_ready()
            except Exception:
                ready = False

        print(f"[OK] {name:<22} Ready = {ready}")


def main():

    try:

        system = bootstrap_system()

        result = system.start()

        print_status(result)

        diagnostics(system)

        print("\nMarketVerse Foundation Started Successfully.")

    except Exception:

        print("\nSYSTEM START FAILED\n")

        traceback.print_exc()


if __name__ == "__main__":
    main()
