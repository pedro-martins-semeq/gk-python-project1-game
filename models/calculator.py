from random import randint


class Calculator:
    __operations_sym_dict = {1: "+", 2: "-", 3: "*"}
    __operations_name_dict = {1: "add", 2: "sub", 3: "mult"}

    def __init__(self, difficulty: int) -> None:
        self.__difficulty: int = difficulty
        self.__value1: float = self._generate_value()
        self.__value2: float = self._generate_value()
        self.__operation: int = randint(1, len(self.__operations_sym_dict))
        self.__result: float = self._generate_result()

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

    def _generate_value(self) -> float:
        return randint(0, pow(self.difficulty, 2))

    def _generate_result(self) -> float:
        if self.operation == 1:
            return self.value1 + self.value2
        elif self.operation == 2:
            return self.value1 - self.value2
        elif self.operation == 3:
            return self.value1 * self.value2
        else:
            return 0.0

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
