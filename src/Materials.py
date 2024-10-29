import numpy as np

class Materials:
    '''
    This Class serves to return material parameters as a function of temperature.
    Water, Zircaloy, and fuel are initialized at the bottom.

    Input variables:
    itemp: float, interface temperature as a single value in Kelvin
    temp: ndarray, temperature in Kelvin as an array of radial position

    output variables:
    heattransfercoefficient: units of W/m2K.
    "Zircaloy" is the HTC between fuel and cladding
    "Water" is the HTC between cladding and water
    thermaldiffusivity: units of m2/s
    thermalconductivity: units of w/mK

    '''
    
    def __init__(self,thermaldiffusivity,thermalconductivity,heattransfercoefficient):
        self.thermaldiffusivity = thermaldiffusivity
        self.thermalconductivity = thermalconductivity
        self.heattransfercoefficient = heattransfercoefficient

    def get_materials_update(self, temps):
        if self == fuel:
            self.thermaldiffusivity = (1/(8e-4*(temps)+0.0686))
            self.thermalconductivity = (1/((6.8e-2)+(1.7e-4*temps)+(3.2e-8*(temps**2))))+0.128*temps*(2.718**(-(1.16/(8.6e-5*temps))))
        elif self == Zircaloy:
            self.thermaldiffusivity = 2.4e-7*(temps-273.15)+7e-6
            self.thermalconductivity = 0.0088*(temps)+12.24
        else:
            if any(temps>643):
                self.thermaldiffusivity = abs(1e-9*(temps)-8e-7)
                xval = np.array([639, 655, 667, 670, 675,685,705,734,758,786,814,1200])
                yval = np.array([0.466,0.442,0.406,0.351,0.302,0.247,0.197,0.163,0.148,0.1418,0.1418,0.1418])
                interp = np.interp(temps,xval,yval)
                self.thermalconductivity = interp
            else:
                self.thermaldiffusivity = 3e-2 * (temps - 273.15) + 1.3417
                self.thermalconductivity = -1e-5 * (temps ** 2) + 0.0081 * temps - 0.861


    def get_heattransfercoefficient(self, itemp):
        #Where itemp is the interface temperture in K
        if (self == Zircaloy):
            #fuel to Zircaloy interface
            self.heattransfercoefficient = 5364-1.716*(itemp-273)
        else:
            #Zircaloy to water interface
            if (itemp<643):
                self.heattransfercoefficient = 45000
            elif (643<itemp<773):
                self.heattransfercoefficient = 8-(32e-3*(itemp-648))
            else:
                self.heattransfercoefficient = 6-(2e-2*(itemp-773))


fuel = Materials(3.177,8.3,0)
Zircaloy = Materials(1.2e-5, 14.8, 5329)
Water = Materials(1.4, 0.65,45000)



