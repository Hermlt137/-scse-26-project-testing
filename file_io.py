import json
from pathlib import Path


def read_text(filename):
    return Path(filename).read_text(encoding="utf-8")


def write_text(text, filename):
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def read_json(filename):
    return json.loads(read_text(filename))


def write_json(data, filename):
    write_text(json.dumps(data, indent=2), filename)
