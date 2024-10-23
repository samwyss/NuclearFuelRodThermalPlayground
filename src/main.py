from src.Config import Config
from src.Model import Model

from os import mkdir, path
from shutil import rmtree


def main():
    """main driver function for ThermalPlayground"""

    # remove old files
    if path.exists("./out"):
        print("removing old output files")
        rmtree("./out")

    # make new folder for output files
    mkdir("./out")



    # todo add gui logic here

    # when "run" button or something is clicked run this code ----------------------------------------------------------
    fuel_thickness: float = (
        0.0  # todo this is temporary and needs to be attached to GUI
    )
    """[m] thickness of fuel"""

    cladding_thickness: float = (
        0.0  # todo this is temporary and needs to be attached to GUI
    )
    """[m] thickness of cladding"""

    bulk_material_temp: float = (
        300.0  # todo this is temporary and needs to be attached to GUI
    )
    """[K] initial bulk material temperature"""

    coolant_temp: float = 300.0  # todo this is temporary and needs to be attached to GUI
    """[K] temperature of coolant as T_infty"""

    core_heat_generation: float = (
        0.0  # todo this is temporary and needs to be attached to GUI
    )
    """[W/m^3] volumetric heat generation rate of core"""

    num_saved_time_steps: int = (
        10  # todo this is temporary and needs to be attached to GUI
    )
    """[] number of saved time steps"""

    end_time: float = 5.0  # todo this is temporary and needs to be attached to GUI
    """[s] end time of simulation"""

    config = Config(
        fuel_thickness,
        cladding_thickness,
        bulk_material_temp,
        coolant_temp,
        core_heat_generation,
        num_saved_time_steps,
        end_time,
    )

    # construct model
    model: Model = Model(config)

    # run model here
    model.run()
    # ------------------------------------------------------------------------------------------------------------------

    # when post processing button is clicked run this code -------------------------------------------------------------
    # todo post processing
    # ------------------------------------------------------------------------------------------------------------------


# runs main
if __name__ == "__main__":
    main()
