from typing import Any

from numpy import full

from Config import Config


class Engine:
    """provides a facade for operating the thermal solver"""

    def __init__(self, config: Config):
        """Solver constructor"""

        # todo set up mesh stuff
        num_points = (
            30  # todo need to determine this, maybe 10 elements for each region?
        )

        # set up initial temperature
        self.__temperature = full(num_points, config.get_coolant_temp())

        # todo set up material properties

        pass

    def __repr__(self) -> dict[str, Any]:
        """changes how Solver is represented, useful for debugging"""
        return self.__dict__

    def update(self) -> None:
        """updates the model to the next timestep"""

        # todo update material properties

        # todo update temperature
