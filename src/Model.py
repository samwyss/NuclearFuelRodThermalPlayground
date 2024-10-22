from src.Config import Config
from src.Engine import Engine

from numpy import floor


class Model:
    """
    Model class, acts as a Facade class to manage simulation
    """

    def __init__(self, config: Config):
        """
        Model constructor
        :param config: model configuration
        """

        self.__d_time: float = 1e-3
        """[s] fixed simulation time step"""

        self.__num_time_steps: int = int(floor(config.get_end_time() / self.__d_time))
        """[] number of timesteps in the simulation"""

        # number of steps between snapshots
        if config.get_num_saved_time_steps() < self.__num_time_steps:
            # case where the number of saved timesteps is less than the total number of timesteps
            self.__num_steps_between_logs: int = floor(
                self.__num_time_steps / config.get_num_saved_time_steps()
            )
            """number of steps between snapshots"""
        else:
            # case where the user requested to save more timesteps than there are available
            self.__num_steps_between_logs: int = 1
            """number of steps between snapshots"""

        # construct model
        self.__engine: Engine = Engine(config, self.__d_time)

    def run(self) -> None:
        """
        runs model
        :return: None
        """

        # main time loop
        for t_step in range(self.__num_time_steps):
            # update temperature
            self.__engine.update(self.__d_time)

            # conditionally log data
            if 0 == t_step % self.__num_steps_between_logs:
                self.__engine.log()
                print(f"logged step {t_step} of {self.__num_time_steps}")

    def get_d_time(self) -> float:
        """
        time step getter
        :return: time step
        """
        return self.__d_time
