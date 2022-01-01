import tkinter as tki
from typing import Callable, Dict, List, Any

BUTTON_HOVER_COLOR = 'gray'
REGULAR_COLOR = 'lightgray'
BUTTON_ACTIVE_COLOR = 'slateblue'

BUTTON_STYLE = {"font": ("Courier", 30),
                "borderwidth": 1,
                "relief": tki.RAISED,
                "bg": REGULAR_COLOR,
                "activebackground": BUTTON_ACTIVE_COLOR}


class CalculatorGUI:
    _buttons: Dict[str, tki.Button] = {}

    def __init__(self) -> None:
        root = tki.Tk()
        root.title("My Calculator")
        root.resizable(False, False)
        self._main_window = root

        self._outer_frame = tki.Frame(root, bg=REGULAR_COLOR,
                                      highlightbackground=REGULAR_COLOR,
                                      highlightthickness=5)
        self._outer_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)

        self._display_label = tki.Label(self._outer_frame, font=("Courier", 30),
                                        bg=REGULAR_COLOR, width=23, relief="ridge")
        self._display_label.pack(side=tki.TOP, fill=tki.BOTH)

        self._lower_frame = tki.Frame(self._outer_frame)
        self._lower_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)

        self._create_buttons_in_lower_frame()
        self._main_window.bind("<Key>", self._key_pressed)

    def run(self) -> None:
        self._main_window.mainloop()

    def set_display(self, display_text: str) -> None:
        self._display_label["text"] = display_text

    def set_button_command(self, button_name: str, cmd: Callable[[], None]) -> None:
        self._buttons[button_name].configure(command=cmd)

    def get_button_chars(self) -> List[str]:
        return list(self._buttons.keys())

    def _create_buttons_in_lower_frame(self) -> None:
        for i in range(4):
            tki.Grid.columnconfigure(self._lower_frame, i, weight=1)  # type: ignore

        for i in range(5):
            tki.Grid.rowconfigure(self._lower_frame, i, weight=1)  # type: ignore

        self._make_button("C", 0, 0)
        self._make_button("/", 0, 1)
        self._make_button("*", 0, 2)
        self._make_button("-", 0, 3)
        self._make_button("7", 1, 0)
        self._make_button("8", 1, 1)
        self._make_button("9", 1, 2)
        self._make_button("+", 1, 3, rowspan=2)
        self._make_button("4", 2, 0)
        self._make_button("5", 2, 1)
        self._make_button("6", 2, 2)
        self._make_button("1", 3, 0)
        self._make_button("2", 3, 1)
        self._make_button("3", 3, 2)
        self._make_button("=", 3, 3, rowspan=2)
        self._make_button("0", 4, 0, columnspan=2)
        self._make_button(".", 4, 2)

    def _make_button(self, button_char: str, row: int, col: int,
                     rowspan: int = 1, columnspan: int = 1) -> tki.Button:
        button = tki.Button(self._lower_frame, text=button_char, **BUTTON_STYLE)
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky=tki.NSEW)
        self._buttons[button_char] = button

        def _on_enter(event: Any) -> None:
            button['background'] = BUTTON_HOVER_COLOR

        def _on_leave(event: Any) -> None:
            button['background'] = REGULAR_COLOR

        button.bind("<Enter>", _on_enter)
        button.bind("<Leave>", _on_leave)
        return button

    def _key_pressed(self, event: Any) -> None:
        """the callback method for when a key is pressed.
        It'll simulate a button press on the right button."""
        if event.char in self._buttons:
            self._simulate_button_press(event.char)
        elif event.keysym == "Return":
            self._simulate_button_press("=")

    def _simulate_button_press(self, button_char: str) -> None:
        """make a button light up as if it is pressed,
        and then return to normal"""
        button = self._buttons[button_char]
        button["bg"] = BUTTON_ACTIVE_COLOR

        def return_button_to_normal() -> None:
            # find which widget the mouse is pointing at:
            x, y = self._main_window.winfo_pointerxy()
            widget_under_mouse = self._main_window.winfo_containing(x, y)
            # change color accordingly:
            if widget_under_mouse is button:
                button["bg"] = BUTTON_HOVER_COLOR
            else:
                button["bg"] = REGULAR_COLOR

        button.invoke()  # type: ignore
        button.after(100, func=return_button_to_normal)


if __name__ == "__main__":
    cg = CalculatorGUI()
    cg.set_display("TEST MODE")
    cg.run()
