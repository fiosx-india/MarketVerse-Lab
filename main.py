# main.py - Entry point for MarketVerse Lab
from marketverse_lab.bootstrap import bootstrap_system

def start_lab():
    print("--- Starting MarketVerse Lab System ---")
    
    # 1. Initialize and connect all modules
    try:
        lab = bootstrap_system()
        print("System modules connected successfully.")
    except Exception as e:
        print(f"Error connecting system: {e}")
        return

    # 2. Perform system health check
    health = lab.guardian.health_report()
    print(f"System Health: {health['health_percent']}% ready.")
    
    # 3. Execute logic if system is ready
    if lab.guardian.is_ready():
        print("All modules are synchronized.")
        
        # Triggering a scan via AI Assistant
        response = lab.assistant.execute("scan")
        print("Scan result:", response)
    else:
        print("Warning: Some modules are not connected.")
        # Diagnostics to identify unconnected modules
        print("Diagnostics Report:", lab.guardian.diagnostics())

if __name__ == "__main__":
    start_lab()
# main.py - Primary Entry Point for MarketVerse Lab

from marketverse_lab.bootstrap import bootstrap_system

def start_system():
    print("--- Starting MarketVerse Lab System ---")
    
    # Initialize the system and connect all modules
    try:
        lab = bootstrap_system()
        print("System modules connected successfully.")
    except Exception as e:
        print(f"Error connecting system: {e}")
        return

    # Check overall system health
    health = lab.guardian.health_report()
    print(f"System Health: {health['health_percent']}% ready.")
    
    # Execute primary scan if system is ready
    if lab.guardian.is_ready():
        print("All modules are synchronized.")
        
        # Triggering a scan via AI Assistant
        response = lab.assistant.execute("scan")
        print("Scan result:", response)
    else:
        print("Warning: Some modules are not connected.")
        # Diagnostics to identify unconnected modules
        print("Diagnostics Report:", lab.guardian.diagnostics())

if __name__ == "__main__":
    start_system()
