from typing import Callable
from calculator_model import CalculatorModel
from calculator_gui import CalculatorGUI


class CalculatorController:
    def __init__(self) -> None:
        self._gui = CalculatorGUI()
        self._model = CalculatorModel()

        for button_text in self._gui.get_button_chars():
            action = self.create_button_action(button_text)
            self._gui.set_button_command(button_text, action)
        self._gui.set_display("0")

    def create_button_action(self, button_text: str) -> Callable[[], None]:
        def fun() -> None:
            self._model.type_in(button_text)
            self._gui.set_display(self._model.get_display())

        return fun

    def run(self) -> None:
        self._gui.run()


if __name__ == "__main__":
    CalculatorController().run()

