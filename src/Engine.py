from typing import Any

from Config import Config
from src.Mesh import Mesh


class Engine:
    """provides a facade for operating the thermal solver"""

    def __init__(self, config: Config):
        """Solver constructor"""
        pass

    def __repr__(self) -> dict[str, Any]:
        """changes how Solver is represented, useful for debugging"""
        return self.__dict__

    def run(self, mesh: Mesh):
        """runs the model"""
        pass
