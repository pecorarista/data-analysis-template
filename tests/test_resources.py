from pathlib import Path

import jsonlines
from jsonschema import validate


def test_resource_jsonlines() -> None:
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "id": {
                "type": "integer"
            },
            "name": {
                "type": "string"
            }
        },
        "required": [
            "id",
            "name"
        ]
    }

    with Path('resources/example.jsonl').open(mode='r') as r:
        reader = jsonlines.Reader(r)
        for obj in reader:
            validate(obj, schema=schema)
