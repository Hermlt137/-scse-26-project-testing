import json

from ollama import chat

MODEL = "qwen3:8b"


def ask_qwen(system_prompt, user_prompt):
    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        think=False,
    )
    return response.message.content


def clean_response(response_text):
    text = response_text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        lines = lines[1:]
        if lines and lines[-1].strip().startswith("```"):
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return text


def parse_json_response(response_text):
    try:
        return json.loads(clean_response(response_text))
    except json.JSONDecodeError:
        return None
