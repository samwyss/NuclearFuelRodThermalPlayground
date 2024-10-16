from typing import Any

from numpy import ndarray


class AbstractMaterial:
    """
    abstract material class

    used as an interface to update material properties
    """

    def __init__(self) -> None:
        self.__interpolation_table: ndarray[float]

    def get_updated_property(temps: ndarray[Any, Any]) -> ndarray[Any, Any]:
        """
        returns an array of material properties given an array of temperatures
        :param temps:
        :return:
        """
        pass
