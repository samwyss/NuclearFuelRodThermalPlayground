from typing import Any
from numpy import full, linspace, zeros
from csv import writer

from Config import Config


class Engine:
    """provides a facade for operating the thermal solver"""

    def __init__(self, config: Config):
        """
        Solver constructor
        :param config: Config object
        """

        self.__num_points = (
            30  # todo need to determine this, maybe 10 elements for each region?
        )
        """[] number of points in simulation domain"""

        self.__current_time: float = 0.0
        """[s] current simulation time"""

        self.__pos = linspace(0.0, 1.0, self.__num_points)  # todo fill me in properly
        """[m] radial location of all points in mesh"""

        self.__alpha = full(self.__num_points, 1.0)  # todo fill me in properly
        """[] thermal diffusivity of mesh"""

        self.__cond = full(self.__num_points, 1.0)  # todo fill me in properly
        """[] thermal conductivity of mesh"""

        self.__temperature = full(self.__num_points, config.get_bulk_material_temp())
        """[K] temperature of all points in mesh"""

        self.__volume_source = full(self.__num_points, 0.0)  # todo fill me in properly
        """[] volumetric sources"""

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
        """
        changes how the object is represented, useful for debugging
        :return:
        """
        return self.__dict__

    def update(self, time_step: float) -> None:
        """
        updates model to the next timestep
        :return: None
        """

        # todo update current time
        self.__current_time += time_step

        # todo update material properties

        # todo matrix assembly

        # todo update temperature

    def log(self) -> None:
        """
        logs temperature to disk
        :return: None
        """

        # log temperature
        with open("./temperature.csv", "a", newline="", encoding="utf-8") as file:
            csv_writer = writer(file)
            csv_writer.writerow(self.__temperature)

        # log time
        with open("./time.csv", "a", newline="", encoding="utf-8") as file:
            csv_writer = writer(file)
            csv_writer.writerow([self.__current_time])
