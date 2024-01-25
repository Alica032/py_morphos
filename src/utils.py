import abc


class NumberConvertor(abc.ABC):
    @abc.abstractmethod
    def get_cases(self, number: int, gender: str) -> list:
        """cases"""

    @abc.abstractmethod
    def get_case(self, number: int, gender: str, case: str) -> str:
        """case"""
