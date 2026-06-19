import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

print("🚀 CYBERSOC SWARM STARTED")

incident = "Multiple failed login attempts detected from Russia"

print("\n🚨 INCIDENT:", incident)

# Simulated Band-style pipeline (REAL AI should be Featherless later)
triage_result = f"SEVERITY: HIGH | TYPE: Brute Force Attack | INCIDENT: {incident}"
print("\n🟡 TRIAGE:", triage_result)

intel_result = "THREAT: Confirmed malicious IPs | RISK SCORE: 9.2/10"
print("\n🟣 THREAT INTEL:", intel_result)

response_result = "ACTION: Block IPs + Lock accounts + Enable MFA"
print("\n🔴 RESPONSE:", response_result)

print("\n✅ SWARM COMPLETE (Band used for orchestration layer only)")