import tkinter
from tkinter import *
#import mp3play
import sys

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
        self.game_screen_display()

        frame.pack(side=TOP, fill=BOTH, expand=True)
        bg = PhotoImage(file="assets/resized.png")
        self.display = Canvas(frame, height=600, width=600, bd=0, highlightthickness=1)
        self.display.create_image(0, 0, image=bg, anchor=NW, tags="IMG")

        self.display.pack(side=TOP, fill=BOTH, expand=True)
        
        self._positioning()
        root.mainloop()

    def game_screen_display(self):
        root = self._main_window
        game_display_frame = Frame(root, bg=REGULAR_COLOR,
                               highlightbackground=REGULAR_COLOR,
                               highlightthickness=5)
        self.side_display_maker(game_display_frame)
        self.current_word_display(game_display_frame)

        self.four_by_four_maker(game_display_frame)
        game_display_frame.pack()

    def side_display_maker(self, frame):
        root = self._main_window
        frame_for_side_bar = Frame(frame, bg=REGULAR_COLOR,
                               highlightbackground="black",
                               highlightthickness=5)
        frame_score = Frame(frame_for_side_bar, bg=REGULAR_COLOR,
                               highlightbackground=REGULAR_COLOR,
                               highlightthickness=5)
        score_title = tkinter.Label(frame_score, text = "SCORE:", font = ("Courier", 30))
        score_title.pack()
        score_actual = tkinter.Label(frame_score, text = "9999", font = ("Courier", 30))
        score_actual.pack()
        frame_score.pack()
        ######################
        frame_time = Frame(frame_for_side_bar, bg=REGULAR_COLOR,
                            highlightbackground=REGULAR_COLOR,
                            highlightthickness=5)
        time_title = tkinter.Label(frame_time, text="TIME:",
                                    font=("Courier", 30))
        time_title.pack()
        time_actual = tkinter.Label(frame_time, text="9999",
                                     font=("Courier", 30))
        time_actual.pack()
        frame_time.pack()
        #####################
        frame_found_words = Frame(frame_for_side_bar, bg=REGULAR_COLOR,
                           highlightbackground=REGULAR_COLOR,
                           highlightthickness=5)
        words_title = tkinter.Label(frame_found_words, text="WORDS:",
                                   font=("Courier", 30))
        words_title.pack()
        words_actual = tkinter.Label(frame_found_words, text="test",
                                    font=("Courier", 30))
        words_actual.pack()
        frame_found_words.pack()
        frame_for_side_bar.pack(side = tkinter.LEFT)


    def current_word_display(self,frame):
        root = self._main_window
        frame_display = Frame(frame,  bg="wheat",
                               highlightbackground="wheat",
                               highlightthickness=5)
        label = tkinter.Label(frame_display, text = "test", font = ("Courier", 50))
        label.pack()
        frame_display.pack(side = tkinter.TOP)

    def four_by_four_maker(self,frame) -> None:
        root = self._main_window
        #f = mp3play.load('boom.mp3'); play = lambda: f.play()
        for i in range(4):
            frame_grid = Frame(frame, bg="black",
                               highlightbackground="wheat",
                               highlightthickness=5)
            for j in range(4):
                b = tkinter.Button(frame_grid, text= str(i)+","+str(j), bg = "orange",font=("Courier", 30))#, command = play)
                b.pack()
            frame_grid.pack(side = tkinter.LEFT)

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
    print(sys.path)

    ui = UserInterface()

    #ui.run()
