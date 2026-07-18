"""
MarketVerse Lab
guardian_test.py

Purpose:
Integration test for GuardianCore.
"""

from marketverse_lab.guardian_core import GuardianCore


def run_tests():

    print("=" * 60)
    print("MarketVerse Guardian Integration Test")
    print("=" * 60)

    guardian = GuardianCore(project_root=".")

    print("\nGuardian Ready")
    print(guardian.is_ready())

    print("\nBlueprint Report")
    print(guardian.report())

    print("\nHealth Report")
    print(guardian.health_report())

    print("\nImport Analyzer")
    print(guardian.import_report())

    print("\nDependency Graph")
    print(guardian.dependency_report())

    print("\nIntegration Checker")
    print(guardian.integration_report())

    print("\nKnowledge Base")
    print(guardian.knowledge_report())

    print("\nChange Planner")
    print(guardian.change_report())

    print("\nPatch Engine")
    print(guardian.patch_report())

    print("\nProject Memory")
    print(guardian.memory_report())

    print("\nLive Monitor")
    print(guardian.monitor_report())

    print("\nWorkflow Engine")
    print(guardian.workflow_report())

    print("\nAI Assistant")
    print(guardian.assistant_report())
    
    print("\nGuardian Health")
    print(guardian.guardian_health_report())

    print("\nAll Tests Completed")
    print("=" * 60)
    
    print("\nProject Advisor")
    print(guardian.advisor_report())
    
    print("\nRisk Analyzer")
    print(guardian.risk_report())
    
    print("\nImpact Analyzer")
    print(guardian.impact_report())
    
    print("\nChange Simulator")
    print(guardian.simulator_report())
    
    print("\nRollback Manager")
    print(guardian.rollback_report())
    
if __name__ == "__main__":
    run_tests()
