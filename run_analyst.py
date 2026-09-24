import json
from pathlib import Path

from analyst_agent import run_analyst

BRIEF_FILE = "brief.txt"
ARTIFACTS_DIR = "artifacts"
REQUIREMENTS_FILE = "requirements.json"


def read_brief(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def save_requirements(requirements, filename):
    output_path = Path(filename)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(requirements, file, indent=2)


def main():
    brief_text = read_brief(BRIEF_FILE)

    requirements = run_analyst(brief_text)

    if requirements is None:
        print("No valid requirements were produced. Nothing was saved.")
        return

    print(json.dumps(requirements, indent=2))

    output_file = Path(ARTIFACTS_DIR) / REQUIREMENTS_FILE
    save_requirements(requirements, output_file)
    print(f"\nRequirements saved to {output_file}")


if __name__ == "__main__":
    main()
