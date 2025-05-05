from os import name as _os_name, system as _os_system
from models.calculator import Calculator


def clear() -> None:
    _os_system("cls" if _os_name == "nt" else "clear")


class Game:
    def __init__(self, calculator: Calculator):
        self.__calculator = calculator
        self.__score = 0
        self.__report = str(self)

    def __str__(self) -> str:
        return f"Calculator: \n{str(self.__calculator)}"

    @property
    def get_score(self) -> int:
        return self.__score

    def get_report(self) -> str:
        return self.__report

    def answer(self, answer: str) -> bool:
        if self._is_correct_answer(answer):
            self._score()
            self.__report = "CORRECT ANSWER\n" + self.__report
            return True
        else:
            self.__report = (
                "WRONG ANSWER "
                + f"(expected {self.__calculator.result}))\n"
                + self.__report
                + "GAME OVER\n"
            )
            self._game_over()
            return False

    def get_str_expression(self):
        return (
            f"{self.__calculator.value1} "
            + f"{self.__calculator.operation_symbol} "
            + f"{self.__calculator.value2} = "
        )

    def refresh_report(self) -> None:
        self.__report = str(self)

    def _score(self) -> None:
        self.__score += 1
        self.__calculator.difficulty += 1

    def _game_over(self) -> None:
        self.__calculator = Calculator(1)
        self.__score = 0

    def _is_correct_answer(self, answer: str) -> bool:
        return self.__calculator.result == float(answer)


def play():
    calculator: Calculator = Calculator(1)

    game: Game = Game(calculator)

    clear()

    while True:
        clear()
        game.refresh_report()

        print(f"Score: {game.get_score}")
        answer: str = input(game.get_str_expression())
        game.answer(answer)

        print(game.get_report())
        input("Press <enter> to continue...")


def main():
    play()


if __name__ == "__main__":
    main()
