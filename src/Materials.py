import numpy as np

class Materials:
    '''
    This Class serves to return material parameters as a function of temperature.

    Input variables:
    itemp: float, interface temperature as a single value in Kelvin
    temp: ndarray, temperature in Kelvin as an array of radial position

    output variables:
    heattransfercoefficient: units of W/m2K, between fuel and Zircaloy
    thermaldiffusivity: units of m2/s
    thermalconductivity: units of w/mK

    '''
    
    def __init__(self, temps, size):
        self.thermaldiffusivity = np.zeros(size)
        self.get_thermaldiffusivity(temps)
        self.thermalconductivity = np.zeros(size)
        self.get_thermalconductivity(temps)
        self.heattransfercoefficient = ()
        self.get_heattransfercoefficient(temps[-1])

    def get_thermaldiffusivity(self, temps):
            self.thermaldiffusivity = (1/(8e-4*(temps)+0.0686))

    def get_thermalconductivity(self, temps):
            self.thermalconductivity = (1/((6.8e-2)+(1.7e-4*temps)+(3.2e-8*(temps**2))))+0.128*temps*(2.718**(-(1.16/(8.6e-5*temps))))

    def get_heattransfercoefficient(self, itemp):
        #Where itemp is the interface temperture in K
            #fuel to Zircaloy interface
            self.heattransfercoefficient = 5364-1.716*(itemp-273)
