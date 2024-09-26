from typing import Any

from Config import Config


class Engine:
    """provides a facade for operating the thermal solver"""

    def __init__(self, config: Config):
        """Solver constructor"""

        # todo set up material properties

        # todo set up mesh stuff

        pass

    def __repr__(self) -> dict[str, Any]:
        """changes how Solver is represented, useful for debugging"""
        return self.__dict__

    def update(self) -> None:
        """updates the model to the next timestep"""

        # todo update material properties

        # todo update temperature
