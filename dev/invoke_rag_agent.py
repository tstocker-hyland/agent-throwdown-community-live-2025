import requests

payload = {
    "messages": [
        {
            "role": "user",
            "content": "What is the company's sick leave policy?"
        },
        {
            "role": "assistant",
            "content": "The company's sick leave policy allows employees to take a certain number of sick days per year. Please refer to the employee handbook for specific details and eligibility criteria."
        },
        {
            "role": "user",
            "content": "Tell me more about HR docs?"
        }
    ],
    "filterValue": {}
}

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': f'Bearer <value>' # Fill this in manually
}

agent_id = "<value>" # Fill this in manually
response = requests.post(f"https://api.agents.ai.dev.experience.hyland.com/agent-platform/v1/agents/{agent_id}/versions/latest/invoke", json=payload, headers=headers)
print(response.status_code)
print(response.text)