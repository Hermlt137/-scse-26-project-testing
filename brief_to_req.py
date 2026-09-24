from file_io import read_text, write_text
from llm import ask_qwen

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


def build_prompt(brief_text):
    system_prompt = SYSTEM_PROMPT
    user_prompt = f"""Brief:
{brief_text}

Write the software requirements for this brief."""
    return system_prompt, user_prompt


def main():
    brief_text = read_text(BRIEF_FILE)

    system_prompt, user_prompt = build_prompt(brief_text)
    requirements_text = ask_qwen(system_prompt, user_prompt)

    print(requirements_text)

    write_text(requirements_text, OUTPUT_FILE)
    print(f"\nRequirements saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
