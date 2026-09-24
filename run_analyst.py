import json
from pathlib import Path

from analyst_agent import run_analyst
from file_io import read_text, write_json

BRIEF_FILE = "brief.txt"
ARTIFACTS_DIR = "artifacts"
REQUIREMENTS_FILE = "requirements.json"


def main():
    brief_text = read_text(BRIEF_FILE)

    requirements = run_analyst(brief_text)

    if requirements is None:
        print("No valid requirements were produced. Nothing was saved.")
        return

    print(json.dumps(requirements, indent=2))

    output_file = Path(ARTIFACTS_DIR) / REQUIREMENTS_FILE
    write_json(requirements, output_file)
    print(f"\nRequirements saved to {output_file}")


if __name__ == "__main__":
    main()
