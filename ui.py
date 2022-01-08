import tkinter as tk


REGULAR_COLOR = 'lightgray'

class UserInterface(object):
    def __init__(self) -> None:
        root = tk.Tk()
        self._main_window = root
        root.title = "Boggle!"
        root.eval('tk::PlaceWindow . center')
        root.iconbitmap('assets/icon.ico')

        self._outer_frame = tk.Frame(root, bg=REGULAR_COLOR,
                                      highlightbackground=REGULAR_COLOR,
                                      highlightthickness=5)
        self._outer_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        bg = tk.PhotoImage(file="assets/menu.png")
        self.display = tk.Canvas(self._outer_frame, bd=0, highlightthickness=0)
        self.display.create_image(0, 0, image=bg, anchor=tk.NW, tags="IMG")
        self.display.grid(row=0, sticky=tk.W+tk.E+tk.N+tk.S)
        self.display.pack(fill=tk.BOTH, expand=1)
        root.mainloop()


    def run(self) -> None:
        self._main_window.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    #ui.run()
