import json
from ollama_client import create_openai_client

def extract_criteria_via_llm(prompt):
    client = create_openai_client()
    try:
        llm_response = client.chat.completions.create(
            model="llama3.1",
            messages=[
                {"role": "system", "content": """
                You are a JSON extraction assistant. Your task is to extract house selection criteria from the given prompt and return it ONLY as a JSON object. Do not include any other text in your response.
                Use the following format:

                {
                    "cost": <number or null>,
                    "New_Build": <boolean>,
                    "Walk_score": <number or null>,
                    "overall_score": <number or null>,
                    "state": "<string or null>",
                    "distance": <number or null>,
                    "place_distance_is_from": "<string or null>"
                }

                If a value is not specified, use null for numbers/strings and false for booleans.
                """},
                {"role": "user", "content": prompt}
            ]
        )
        llm_response_content = llm_response.choices[0].message.content
        print(f"llm_response_content: {llm_response_content}")

        criteria = json.loads(llm_response_content)

        # Ensure all expected keys are present
        expected_keys = ["cost", "New_Build", "Walk_score", "overall_score", "state", "distance", "place_distance_is_from"]
        for key in expected_keys:
            if key not in criteria:
                criteria[key] = None if key != "New_Build" else False

        return criteria
    except Exception as e:
        print(f"Error in extract_criteria_via_llm: {e}")
        return create_default_criteria()

def create_default_criteria():
    return {
        "cost": None,
        "New_Build": False,
        "Walk_score": None,
        "overall_score": None,
        "state": None,
        "distance": None,
        "place_distance_is_from": None
    }