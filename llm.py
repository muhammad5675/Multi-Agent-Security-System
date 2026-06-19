import os
import requests
from dotenv import load_dotenv

load_dotenv()

FEATHERLESS_API_KEY = os.getenv("FEATHERLESS_API_KEY")
BASE_URL = os.getenv("FEATHERLESS_BASE_URL")

def call_llm(prompt, agent_role):
    system_prompts = {
        "TriageAgent": "You are Sentinel Triage Agent. Identify vulnerability type, severity, and target line. Format with [ANALYSIS START] and [ANALYSIS END].",
        "SecurityEngineer": "You are Security Engineer Agent. Rewrite the vulnerable code safely. Format with [PATCH START] and [PATCH END].",
        "ReviewerAgent": "You are Patch Reviewer Agent. Verify the patch code. Format with [REVIEW START], STATUS: APPROVED or REJECTED, and [REVIEW END]."
    }
    
    headers = {
        "Authorization": f"Bearer {FEATHERLESS_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "meta-llama/Llama-3-70b-Instruct",
        "messages": [
            {"role": "system", "content": system_prompts.get(agent_role, "You are a helpful security assistant.")},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.1
    }
    
    try:
        response = requests.post(f"{BASE_URL}/chat/completions", headers=headers, json=payload)
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error executing {agent_role}: {str(e)}"