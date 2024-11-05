from csv import writer
from typing import Any

from numpy import full, linspace, zeros
from numpy.linalg import solve

from Config import Config


class Engine:
    """provides a facade for operating the thermal solver"""

    def __init__(self, config: Config, d_time: float):
        """
        Solver constructor
        :param config: Config object
        :param d_time: float time step [s]
        """

        self.__num_points: int = 50
        """[] number of points in simulation domain"""

        self.__current_time: float = 0.0
        """[s] current simulation time"""

        self.__delta_r = config.get_fuel_thickness() / (self.__num_points - 1)
        """[m] radial step"""

        self.__pos = linspace(0.0, config.get_fuel_thickness(), self.__num_points)
        """[m] radial location of all points in mesh"""

        # write position
        with open("./out/position.csv", "a", newline="", encoding="utf-8") as file:
            csv_writer = writer(file)
            csv_writer.writerow(self.__pos)

        self.__alpha = full(self.__num_points, 1e-6)  # todo fill me in properly
        """[] thermal diffusivity of mesh"""

        self.__cond = full(self.__num_points, 10.0)  # todo fill me in properly
        """[] thermal conductivity of mesh"""

        self.__temperature = full(self.__num_points, config.get_bulk_material_temp())
        """[K] temperature of all points in mesh"""

        self.__volume_source = zeros(self.__num_points)
        """[] volumetric sources"""

        self.__volume_source = full(self.__num_points, config.get_core_heat_generation())
        """[W/m^3] volumetric core heat source""" # todo determine me

        self.__A = zeros((self.__num_points, self.__num_points))
        """[] A matrix in linear system"""

        self.__b = zeros(self.__num_points)
        """[] B vector in linear system"""

        self.__temp_clad = config.get_bulk_material_temp()
        """[K] reference temperature of cladding"""

        self.__h_clad = 100.0  # todo fill me in correctly
        """[] heat transfer coefficient from fuel to clad"""

        self.__c1 = (1 / d_time + self.__alpha / self.__delta_r ** 2)
        """[] array geometric constants for all points in the simulation domain"""

        self.__c2 = (1 / d_time - self.__alpha / self.__delta_r ** 2)
        """[] array geometric constants for all points in the simulation domain"""

        self.__c3 = (self.__alpha / (2.0 * self.__delta_r**2) + self.__alpha / (4.0 * self.__pos * self.__delta_r))
        """[] array geometric constants for all points in the simulation domain"""

        self.__c4 = (self.__alpha / (2.0 * self.__delta_r**2) - self.__alpha / (4.0 * self.__pos * self.__delta_r))
        """[] array geometric constants for all points in the simulation domain"""

        self.__c5 = (self.__alpha / self.__cond)
        """[] array geometric constants for all points in the simulation domain"""

        self.__c6 = (2.0 * self.__delta_r * self.__h_clad / self.__cond)
        """[] array geometric constants for all points in the simulation domain"""

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

        # reassemble system with updated properties
        self.__assemble_system(d_time)

        # add source to b
        self.__b += self.__volume_source * self.__c5

        # update temperature
        self.__temperature = solve(self.__A, self.__b)

    def log(self) -> None:
        """
        logs temperature to disk
        :return: None
        """

        # log temperature
        with open("./out/temperature.csv", "a", newline="", encoding="utf-8") as file:
            csv_writer = writer(file)
            csv_writer.writerow(self.__temperature)

        # log time
        with open("./out/time.csv", "a", newline="", encoding="utf-8") as file:
            csv_writer = writer(file)
            csv_writer.writerow([self.__current_time])

    def __assemble_system(self, d_time: float) -> None:
        """reassembles matrices based on new material properties"""

        # left boundary conditions (reflective)
        self.__A[0, 0] = (1 / d_time + self.__alpha[0] / self.__delta_r ** 2)
        self.__A[0, 1] = -(self.__alpha[0] / self.__delta_r ** 2)
        self.__b[0] = (1 / d_time - self.__alpha[0] / self.__delta_r ** 2) * self.__temperature[0] + (self.__alpha[0] / self.__delta_r ** 2) * self.__temperature[1]

        # right boundary conditions (convective robbin BC)
        self.__A[-1,-1] = (self.__c1[-1] + self.__c3[-1] * self.__c6[-1])
        self.__A[-1,-2] = -(self.__c4[-1] + self.__c3[-1])
        self.__b[-1] = ((self.__c2[-1] - self.__c3[-1] * self.__c6[-1]) * self.__temperature[-1]
                        + (self.__c4[-1] + self.__c3[-1]) * self.__temperature[-2]
                        + 2.0 * self.__c3[-1] * self.__c6[-1] * self.__temp_clad)

        # interior nodes
        for i in range(1, self.__num_points - 1):

            # A matrix
            self.__A[i, i] = self.__c1[i]
            self.__A[i, i + 1] = -self.__c3[i]
            self.__A[i, i - 1] = -self.__c4[i]

            # B matrix
            self.__b[i] = (
                self.__c2[i] * self.__temperature[i]
                + self.__c3[i] * self.__temperature[i + 1]
                + self.__c4[i]* self.__temperature[i - 1]
            )
