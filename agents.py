from llm import call_llm

def run_triage(vulnerable_code):
    prompt = f"Analyze this code for security flaws:\n\n{vulnerable_code}"
    return call_llm(prompt, agent_role="TriageAgent")

def run_engineer(triage_report, original_code):
    prompt = f"Using this report:\n{triage_report}\n\nSecure this original code:\n{original_code}"
    return call_llm(prompt, agent_role="SecurityEngineer")

def run_reviewer(patched_code):
    prompt = f"Audit this code patch for security compliance:\n\n{patched_code}"
    return call_llm(prompt, agent_role="ReviewerAgent")