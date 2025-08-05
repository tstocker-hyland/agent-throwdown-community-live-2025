import requests

payload = {
    "name": "DocumentHelper",
    "description": "Document assistant",
    "agentType": "rag",
    "notes": "Initial version - shows all configuration options",
    "config": {
        "filter_value": {},
        "limit": 25,
        "llm_model_id": "amazon.nova-micro-v1:0",
        "system_prompt": "Context information is below.\n---------------------\n{context_str}\n---------------------\nGiven the context information and not prior knowledge, answer the query.\nQuery: {query_str}\nAnswer:",
        "inference_config": {
            "temperature": 0.7,
            "max_tokens": 4000
        }
    }
}

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': f'Bearer <value>' # Fill this in manually
}

response = requests.post("https://api.agents.ai.dev.experience.hyland.com/agent-platform/v1/agents", json=payload, headers=headers)
print(response.status_code)
print(response.text)