from typing import Any
from numpy import full, linspace, zeros, dot
from numpy.linalg import solve
from csv import writer

from Config import Config


class Engine:
    """provides a facade for operating the thermal solver"""

    def __init__(self, config: Config, d_time: float):
        """
        Solver constructor
        :param config: Config object
        """

        self.__num_points = (
            100  # todo need to determine this, maybe 10 elements for each region?
        )
        """[] number of points in simulation domain"""

        self.__current_time: float = 0.0
        """[s] current simulation time"""

        self.__delta_r = 1.0 / self.__num_points # todo this will likely need to be changed when material regions are added
        """[m] radial step"""

        self.__pos = linspace(self.__delta_r, 1.0, self.__num_points)  # todo fill me in properly
        """[m] radial location of all points in mesh"""

        self.__alpha = full(self.__num_points, 0.143)  # todo fill me in properly
        """[] thermal diffusivity of mesh"""

        self.__cond = full(self.__num_points, 0.5918)  # todo fill me in properly
        """[] thermal conductivity of mesh"""

        self.__temperature = full(self.__num_points, config.get_bulk_material_temp())
        """[K] temperature of all points in mesh"""

        self.__volume_source = full(self.__num_points, 0.0)  # todo fill me in properly
        """[] volumetric sources"""

        self.__A = zeros((self.__num_points, self.__num_points))
        """[] A matrix in linear system"""

        self.__b = zeros(self.__num_points)
        """[] B vector in linear system"""

        # left boundary conditions
        self.__A[0, 0] = 1.0
        self.__b[0] = 1.0
        self.__temperature[0] = 1.0

        # right boundary conditions
        self.__A[-1, -1] = 1.0

        # interior nodes
        for i in range(1, self.__num_points - 1):

            # A matrix
            self.__A[i, i + 1] = - (self.__alpha[i] / (2.0 * self.__delta_r ** 2) + self.__alpha[i] / (2.0 * self.__pos[i] * self.__delta_r))
            self.__A[i, i] = (1.0 / d_time + self.__alpha[i] / self.__delta_r ** 2)
            self.__A[i, i - 1] = - (self.__alpha[i] / (2.0 * self.__delta_r ** 2) - self.__alpha[i] / (2.0 * self.__pos[i] * self.__delta_r))

            # B matrix
            a = (self.__alpha[i] / (2.0 * self.__delta_r ** 2) - self.__alpha[i] / (2.0 * self.__pos[i] * self.__delta_r)) * self.__temperature[i - 1]
            self.__b[i] = (1.0 / d_time - self.__alpha[i] / self.__delta_r ** 2) * self.__temperature[i] + (self.__alpha[i] / (2.0 * self.__delta_r ** 2) + self.__alpha[i] / (2.0 * self.__pos[i] * self.__delta_r)) * self.__temperature[i + 1] + (self.__alpha[i] / (2.0 * self.__delta_r ** 2) - self.__alpha[i] / (2.0 * self.__pos[i] * self.__delta_r)) * self.__temperature[i - 1]

    def __repr__(self) -> dict[str, Any]:
        """
        changes how the object is represented, useful for debugging
        :return:
        """
        return self.__dict__

    def update(self, d_time: float) -> None:
        """
        updates model to the next timestep
        :return: None
        """

        # update current time
        self.__current_time += d_time

        # todo update material properties

        # todo matrix assembly

        # b vector assembly
        for i in range(1, self.__num_points - 1):
            self.__b[i] = (1.0 / d_time - self.__alpha[i] / self.__delta_r ** 2) * self.__temperature[i] + (self.__alpha[i] / (2.0 * self.__delta_r ** 2) + self.__alpha[i] / (2.0 * self.__pos[i] * self.__delta_r)) * self.__temperature[i + 1] + (self.__alpha[i] / (2.0 * self.__delta_r ** 2) - self.__alpha[i] / (2.0 * self.__pos[i] * self.__delta_r)) * self.__temperature[i - 1]

        # todo update temperature
        self.__temperature = solve(self.__A, self.__b)

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
