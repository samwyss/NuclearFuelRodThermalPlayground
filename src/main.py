from src.Config import Config
from src.Model import Model


def main():
    """main driver function for ThermalPlayground"""

    # todo add gui logic here

    # when "run" button or something is clicked run this code ----------------------------------------------------------
    fuel_thickness: float = (
        0.0  # todo this is temporary and needs to be attached to GUI
    )
    cladding_thickness: float = (
        0.0  # todo this is temporary and needs to be attached to GUI
    )
    bulk_material_temp: float = (
        0.0  # todo this is temporary and needs to be attached to GUI
    )
    coolant_temp: float = 0.0  # todo this is temporary and needs to be attached to GUI
    core_heat_generation: float = (
        0.0  # todo this is temporary and needs to be attached to GUI
    )
    num_saved_time_steps: int = (
        0  # todo this is temporary and needs to be attached to GUI
    )
    end_time: float = 0.0  # todo this is temporary and needs to be attached to GUI
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

    # run model
    model.run()
    # ------------------------------------------------------------------------------------------------------------------

    # when post processing button is clicked run this code -------------------------------------------------------------
    # todo post processing
    # ------------------------------------------------------------------------------------------------------------------


# runs main
if __name__ == "__main__":
    main()
