from marketverse_lab import GuardianCore

guardian = GuardianCore()

print("=" * 50)
print("Guardian Created :", guardian is not None)
print("Guardian Ready   :", guardian.is_ready())
print("=" * 50)

print(guardian.report())
