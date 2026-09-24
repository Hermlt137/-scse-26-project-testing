from pathlib import Path

from ollama import chat

MODEL = "qwen3:8b"

BRIEF_FILE = "brief.txt"
OUTPUT_FILE = "robot_requirements.txt"

SYSTEM_PROMPT = """You are a requirements engineer. Your job is to read a customer brief written in natural language and produce clear, explicit software requirements for the software to be built.

Rules:
- Use ONLY the information given in the brief.
- Write each requirement as a separate numbered statement.
- Use clear, testable language (must, must never, should).
- Do not invent features that are not in the brief.
- Do not write code.
- Return only the requirements text, with no extra commentary."""


def read_brief(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def build_prompt(brief_text):
    system_prompt = SYSTEM_PROMPT
    user_prompt = f"""Brief:
{brief_text}

Write the software requirements for this brief."""
    return system_prompt, user_prompt


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


def save_output(text, filename):
    Path(filename).write_text(text, encoding="utf-8")


def main():
    brief_text = read_brief(BRIEF_FILE)

    system_prompt, user_prompt = build_prompt(brief_text)
    requirements_text = ask_qwen(system_prompt, user_prompt)

    print(requirements_text)

    save_output(requirements_text, OUTPUT_FILE)
    print(f"\nRequirements saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
