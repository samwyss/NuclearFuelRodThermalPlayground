import numpy as np

class Materials:
    """
    This Class serves to return material parameters as a function of temperature.

    Specifically that of the fuel in this system, it could further be extended by creating multiple materials which contain correlations to update their properties
    """
    
    def __init__(self, temperature):
        """Material Constructor"""

        # initialize thermal diffusivity
        self.thermal_diffusivity = np.zeros(temperature.shape[0])
        """[m^2 / s] Thermal Diffusivity"""

        # initialize thermal conductivity
        self.thermal_conductivity = np.zeros(temperature.shape[0])
        """[W / m K] Thermal Conductivity"""

        # initialize heat_transfer coefficient
        self.heat_transfer_coefficient = 0
        """[W / m^2 K] Heat Transfer Coefficient"""

        # properly initialize all material properties
        self.update(temperature)


    def update(self, temperature):
        """
        update all material properties given the current temperature
        :param temperature: current numpy array of temperatures
        :return: None
        """

        # update thermal diffusivity
        self.__update_thermal_diffusivity(temperature)

        # update thermal conductivity
        self.__update_thermal_conductivity(temperature)

        # update heat transfer coefficient
        self.__update_heat_transfer_coefficient(temperature[-1])

    def __update_thermal_diffusivity(self, temperature):
        """
        update thermal diffusivity given the current temperature
        :param temperature: current numpy array of temperatures
        :return: None
        """

        self.thermal_diffusivity = (1/(8e-4*temperature+0.0686))*1e-6

    def __update_thermal_conductivity(self, temperature):
        """
        update thermal conductivity given the current temperature
        :param temperature: current numpy array of temperatures
        :return: None
        """

        self.thermal_conductivity = (1/(6.8e-2+(1.7e-4*temperature)+(3.2e-8*(temperature**2))))+0.128*temperature*(2.718**(-(1.16/(8.6e-5*temperature))))

    def __update_heat_transfer_coefficient(self, temperature):
        """
        update heat transfer coefficient given the current temperature
        :param temperature: fuel pin surface temperature
        :return: None
        """

        #fuel to Zircaloy interface
        self.heat_transfer_coefficient = 5364-1.716*(temperature-273)
