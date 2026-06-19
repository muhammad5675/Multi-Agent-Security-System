import yaml
import requests

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

agent = config["sentinel_triage"]
api_key = agent["api_key"]
agent_id = agent["agent_id"]

# REAL API test call
response = requests.get(
    "https://app.band.ai/api/v1/agent/me",
    headers={
        "X-API-Key": api_key
    }
)

print("Status Code:", response.status_code)
print("Response:")
print(response.text)