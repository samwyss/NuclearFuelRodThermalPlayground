from src.Config import Config
from src.Engine import Engine


class Model:
    """
    Model class, acts as a Facade class to manage simulation
    """

    def __init__(self, config: Config):
        """
        Model constructor
        :param config: model configuration
        """

        # construct model
        self.__engine: Engine = Engine(config)

        # todo create sensor observer class

    def run(self) -> None:
        """
        runs model
        :return: None
        """

        # number of time steps to run
        num_time_steps = 0  # todo calculate me

        # main time loop
        for t_step in range(num_time_steps):
            # update temperature
            self.__engine.update()

            # conditionally log data
            # todo conditionally call log on sensor observer class
