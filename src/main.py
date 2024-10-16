from src.Config import Config
from src.Model import Model


def main():
    """main driver function for ThermalPlayground"""

    # todo add gui logic here

    # when "run" button or something is clicked run this code
    fuel_thickness: float = 0.0  # todo this is temporary
    cladding_thickness: float = 0.0  # todo this is temporary
    bulk_material_temp: float = 0.0  # todo this is temporary
    coolant_temp: float = 0.0  # todo this is temporary
    core_heat_generation: float = 0.0  # todo this is temporary
    num_saved_time_steps: int = 0  # todo this is temporary
    end_time: float = 0.0  # todo this is temporary
    config = Config(
        fuel_thickness,
        cladding_thickness,
        bulk_material_temp,
        coolant_temp,
        core_heat_generation,
        num_saved_time_steps,
    )

    # construct model
    model: Model = Model(config)

    # run model
    model.run()

    # todo post processing


# runs main
if __name__ == "__main__":
    main()
