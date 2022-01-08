from tkinter import *

REGULAR_COLOR = 'lightgray'


def default():
    pass

class UserInterface(object):
    def __init__(self) -> None:
        root = Tk()
        self._main_window = root
        root.title = "Boggle"
        root.iconbitmap('assets/icon.ico')
        frame = Frame(root, bg=REGULAR_COLOR,
                                      highlightbackground=REGULAR_COLOR,
                                      highlightthickness=5)
        self._main_frame = frame
        frame.pack(side=TOP, fill=BOTH, expand=True)
        bg = PhotoImage(file="assets/resized.png")
        self.display = Canvas(frame, height=600, width=600, bd=0, highlightthickness=1)
        self.display.create_image(0, 0, image=bg, anchor=NW, tags="IMG")
        self.display.pack(side=TOP, fill=BOTH, expand=True)
        
        self._positioning()
        root.mainloop()


    def run(self) -> None:
        self._main_window.mainloop()
    
    def _create_buttons(self):
        buttons = {
            {
                "text": "Start",
                "command": default(),
            }
        }

        for b in buttons:
            button = Button(self._main_frame, text=b["text"])
            button.pack(side=TOP, fill=BOTH, expand=True)
            

    def _positioning(self):
        root = self._main_window
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()
        # Gets both half the screen width/height and window width/height
        positionRight = int(screen_width/4)
        positionDown = int(screen_height/4 - screen_height*0.22)
        # Positions the window in the center of the page.
        root.geometry("+{}+{}".format(positionRight, positionDown))


if __name__ == "__main__":
    ui = UserInterface()
    #ui.run()
