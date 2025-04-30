from random import randint
from typing import Dict


class Calculator:
    __operations_sym_dict: Dict[int, str] = {1: "+", 2: "-", 3: "*"}
    __operations_name_dict: Dict[int, str] = {1: "add", 2: "sub", 3: "mult"}

    def __init__(self, difficulty: int) -> None:
        self.__difficulty: int = difficulty
        self.__value1: float = self._calculate_new_value()
        self.__value2: float = self._calculate_new_value()
        self.__operation: int = self._get_new_operation()
        self.__result: float = self._calculate_result()

    def __str__(self) -> str:
        return (
            f"Value 1: {self.value1}\n"
            + f"Value 2: {self.value2}\n"
            + f"Difficulty: {self.difficulty}\n"
            + f"Operation: {self.operation_symbol} ({self.operation_text})\n"
        )

    def __repr__(self) -> str:
        return (
            f"Calculator class <object> - value1:{self.value1} "
            + f"value2: {self.value2} "
            + f"difficulty:{self.difficulty} "
            + f"operation: {self.operation}"
        )

    @property
    def difficulty(self) -> int:
        return self.__difficulty

    @property
    def value1(self) -> float:
        return self.__value1

    @property
    def value2(self) -> float:
        return self.__value2

    @property
    def operation(self) -> int:
        return self.__operation

    @property
    def operation_symbol(self) -> str:
        return self.__operations_sym_dict[self.operation]

    @property
    def operation_text(self) -> str:
        return self.__operations_name_dict[self.operation]

    @property
    def result(self) -> float:
        return self.__result

    @difficulty.setter
    def difficulty(self, difficulty: int) -> None:
        self.__difficulty = difficulty
        self._generate_new_operation()

    def _generate_new_operation(self) -> None:
        self.__value1 = self._calculate_new_value()
        self.__value2 = self._calculate_new_value()
        self.__operation = self._get_new_operation()
        self.__result = self._calculate_result()

    def _calculate_new_value(self) -> float:
        return randint(0, pow(self.difficulty, 2))

    def _calculate_result(self) -> float:
        if self.operation == 1:
            return self.value1 + self.value2  # Addition
        elif self.operation == 2:
            return self.value1 - self.value2  # Subtraction
        elif self.operation == 3:
            return self.value1 * self.value2  # Multiplication
        else:
            return 0.0

    def _get_new_operation(self) -> int:
        return randint(1, len(self.__operations_sym_dict))
