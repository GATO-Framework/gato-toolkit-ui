import json
import pathlib

import yaml

import gato.entity


DATA_DIR = pathlib.Path(__file__).parent.parent / "data"


def save_scenario(scenario: gato.entity.Scenario):
    key = f"scenario_{scenario.id}"
    path = pathlib.Path(f"scenarios/{key}.yml")
    with open(DATA_DIR / path, "w") as file:
        yaml.safe_dump(json.loads(scenario.json()), file)


def load_scenario(key) -> gato.entity.Scenario:
    path = pathlib.Path(f"scenarios/{key}.yml")
    with open(DATA_DIR / path) as file:
        return gato.entity.Scenario(**yaml.safe_load(file))


def save_action(scenario: gato.entity.Scenario, action: gato.entity.Action):
    key = f"action_{scenario.id}"
    path = pathlib.Path(f"actions/{key}.yml")
    with open(DATA_DIR / path, "w") as file:
        yaml.safe_dump(json.loads(action.json()), file)