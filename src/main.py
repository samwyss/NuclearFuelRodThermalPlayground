from src.Config import Config
from src.Model import Model


def main():
    """main driver function for ThermalPlayground"""

    # todo add gui logic here

    # when "run" button or something is clicked run this code
    fuel_thickness: float = 0.0
    cladding_thickness: float = 0.0
    bulk_material_temp: float = 0.0
    coolant_temp: float = 0.0
    core_heat_generation = 0.0
    num_saved_time_steps = 0
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
