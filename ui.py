import tkinter as tk
from tkinter import CENTER, TOP, BOTH, NW
from consts import PRIMARY, SECONDARY, REGULAR_COLOR, MAIN_FONT 


def default():
    pass

class UserInterface(object):
    def __init__(self) -> None:
        root = tk.Tk()
        self._main_window = root
        root.title("Boggle")
        root.iconbitmap('assets/icon.ico')
        frame = tk.Frame(root)
        self._main_frame = frame
        frame.grid(row=0, column=0, sticky="nsew")
        
        bg = tk.PhotoImage(file="assets/resized.png")
        self._main_menu_canvas = tk.Canvas(frame, height=600, width=600, bd=0, highlightthickness=1)
        self._main_menu_canvas.create_image(0, 0, image=bg, anchor=NW, tags="IMG")
        self._main_menu_canvas.pack(side=TOP, fill=BOTH, expand=True)

        self.game_screen_display()
        
        self._positioning()
        self._create_buttons(self._main_menu_canvas,{
            1: {
                "text": "Start",
                "command": self._show_game_frame,
                "relx" : 0.5,
                "rely": 0.5
            },
            2: {
                "text": "Exit",
                "command": self.exit,
                "relx" : 0.5,
                "rely": 0.6
            },
            3: {
                "text": "?",
                "command": default,
                "relx" : 0.95,
                "rely": 0.95,
                "width": 50,
                "height": 30
            },
            
        })
        
        self._show_frame(self._main_frame)
        root.mainloop()


    def run(self) -> None:
        self._main_window.mainloop()
    
    def exit(self) -> None :
        self._main_window.destroy()

    def _show_game_frame(self):
        self._show_frame(self._game_display_frame)
        
    def _create_buttons(self, parent, buttons):
        for _, b in buttons.items():
            button = tk.Button(parent, background = PRIMARY, text = b["text"], font=(MAIN_FONT, 18), command = b["command"])
            button.place(relx = b["relx"], rely = b["rely"], anchor = CENTER, width = b.get("width", 100), height = b.get("height", 50))
    
    def _show_frame(self, frame):
        frame.tkraise()
        
    def game_screen_display(self):
        root = self._main_window
        game_display_frame = tk.Frame(root, bg=REGULAR_COLOR,
                               highlightbackground=REGULAR_COLOR,
                               highlightthickness=5, width=600, height=600)
        self.side_display_maker(game_display_frame)
        self.current_word_display(game_display_frame)

        self.four_by_four_maker(game_display_frame)
        game_display_frame.grid(row=0, column=0, sticky="nsew")
        self._game_display_frame = game_display_frame

    def side_display_maker(self, frame):
        root = self._main_window
        frame_for_side_bar = tk.Frame(frame, bg=REGULAR_COLOR,
                               highlightbackground="black",
                               highlightthickness=5)
        frame_score = tk.Frame(frame_for_side_bar, bg=REGULAR_COLOR,
                               highlightbackground=REGULAR_COLOR,
                               highlightthickness=5)
        score_title = tk.Label(frame_score, text = "SCORE:", font = (MAIN_FONT, 30))
        score_title.pack()
        score_actual = tk.Label(frame_score, text = "9999", font = (MAIN_FONT, 30))
        score_actual.pack()
        frame_score.pack()
        ######################
        frame_time = tk.Frame(frame_for_side_bar, bg=REGULAR_COLOR,
                            highlightbackground=REGULAR_COLOR,
                            highlightthickness=5)
        time_title = tk.Label(frame_time, text="TIME:",
                                    font=(MAIN_FONT, 30))
        time_title.pack()
        time_actual = tk.Label(frame_time, text="9999",
                                     font=(MAIN_FONT, 30))
        time_actual.pack()
        frame_time.pack()
        #####################
        frame_found_words = tk.Frame(frame_for_side_bar, bg=REGULAR_COLOR,
                           highlightbackground=REGULAR_COLOR,
                           highlightthickness=5)
        words_title = tk.Label(frame_found_words, text="WORDS:",
                                   font=(MAIN_FONT, 30))
        words_title.pack()
        words_actual = tk.Label(frame_found_words, text="test",
                                    font=(MAIN_FONT, 30))
        words_actual.pack()
        frame_found_words.pack()
        frame_for_side_bar.pack(side = tk.LEFT)


    def current_word_display(self,frame):
        root = self._main_window
        frame_display = tk.Frame(frame,  bg="wheat",
                               highlightbackground="wheat",
                               highlightthickness=5)
        label = tk.Label(frame_display, text = "test", font = (MAIN_FONT, 50))
        label.pack()
        frame_display.pack(side = tk.TOP)


    def four_by_four_maker(self, frame) -> None:
        for i in range(4):
            frame_grid = tk.Frame(frame, bg="black",
                               highlightbackground="wheat",
                               highlightthickness=5)
            for j in range(4):
                b = tk.Button(frame_grid, text= str(i)+","+str(j), bg = "orange",font=(MAIN_FONT, 30))
                b.pack()
            frame_grid.pack(side = tk.LEFT)


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
