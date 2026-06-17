import yaml
from pathlib import Path


class ObjectiveMapper:

    def __init__(self, yaml_path=None):

        if yaml_path is None:
            yaml_path = Path(__file__).parent / "objectives.yaml"

        self.yaml_path = yaml_path
        self.objectives = self._load()

    def _load(self):

        with open(self.yaml_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        return data.get("objectives", {})

    def get_objective(self, objective_name):

        return self.objectives.get(objective_name)

    def get_dimensions(self, objective_name):

        objective = self.get_objective(objective_name)

        if not objective:
            return []

        return objective.get("dimensions", [])

    def get_agents(self, objective_name):

        objective = self.get_objective(objective_name)

        if not objective:
            return []

        return objective.get("agents", [])

    def list_objectives(self):

        return list(self.objectives.keys())