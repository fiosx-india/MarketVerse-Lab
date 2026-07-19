from marketverse_lab import GuardianCore

guardian = GuardianCore()

print("Guardian Created :", guardian is not None)
print("Guardian Ready   :", guardian.is_ready())
print("Diagnostics      :", guardian.diagnostics())
