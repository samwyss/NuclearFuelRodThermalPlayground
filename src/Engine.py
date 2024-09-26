from typing import Any

from Config import Config


class Engine:
    """provides a facade for operating the thermal solver"""

    def __init__(self, config: Config):
        """Solver constructor"""
        pass

    def __repr__(self) -> dict[str, Any]:
        """changes how Solver is represented, useful for debugging"""
        return self.__dict__

    def update(self):
        """updates the model to the next timestep"""
        pass
