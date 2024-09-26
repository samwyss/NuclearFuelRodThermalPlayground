from src.Config import Config
from src.Engine import Engine
from src.Mesh import Mesh


class Model:
    """
    Model class, acts as a Facade class to manage simulation
    """

    def __init__(self, config: Config):
        """
        Model constructor
        """

        # construct mesh
        self.__mesh: Mesh = Mesh(config)

        # construct model
        self.__engine: Engine = Engine(config)

    def run(self) -> None:
        self.__engine.run(self.__mesh)
