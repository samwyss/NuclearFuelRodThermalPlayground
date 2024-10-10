from typing import Any

from numpy import full, linspace, zeros

from Config import Config


class Engine:
    """provides a facade for operating the thermal solver"""

    def __init__(self, config: Config):
        """Solver constructor"""

        self.__num_points = (
            30  # todo need to determine this, maybe 10 elements for each region?
        )
        """[] number of points in simulation domain"""

        self.__pos = linspace(0.0, 1.0, self.__num_points) # todo fill me in properly
        """[m] radial location of all points in mesh"""

        self.__alpha = full(self.__num_points, 1.0) # todo fill me in properly
        """[] thermal diffusivity of mesh"""

        self.__cond = full(self.__num_points, 1.0) # todo fill me in properly
        """[] thermal conductivity of mesh"""

        self.__temperature = full(self.__num_points, config.get_coolant_temp())
        """[K] temperature of all points in mesh"""

        self.__volume_source = full(self.__num_points, 0.0) # todo fill me in properly

        self.__A = zeros((self.__num_points, self.__num_points))
        """[] A matrix in linear system AT^(n+1) = BT^(n)"""

        self.__B = zeros((self.__num_points, self.__num_points))
        """[] B matrix in linear system AT^(n+1) = BT^(n)"""

        # matrix assembly
        for i in range(1, self.__num_points - 1):
            # todo j - 1
            # todo j
            # todo j + 1
            pass

        # todo boundary conditions at r = 0 and r = 1



    def __repr__(self) -> dict[str, Any]:
        """changes how Solver is represented, useful for debugging"""
        return self.__dict__

    def update(self) -> None:
        """updates the model to the next timestep"""

        # todo update material properties

        # todo matrix assembly

        # todo update temperature
