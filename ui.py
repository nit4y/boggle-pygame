# Web pages we used: https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter

import tkinter as tk
from tkinter import CENTER, TOP, BOTH, NW
from tkinter.constants import LEFT, W
from tkinter.font import BOLD
import consts


def default():
    pass

class UserInterface(object):
    def __init__(self) -> None:
        # Initilization
        root = tk.Tk()
        self._main_window = root
        root.title("Boggle")
        root.iconbitmap('assets/icon.ico')

        # Initiate main menu frame
        bg = tk.PhotoImage(file="assets/resized.png")
        self._create_main_menu(bg)

        # Initiate play frame
        self.game_screen_display()
        self._about_rules_screen()

        self._show_main_menu_frame()
        self._center(root)
        root.mainloop()


    def run(self) -> None:
        self._main_window.mainloop()
    

    def exit(self) -> None :
        self._main_window.destroy()


    def _show_main_menu_frame(self):
        self._show_frame(self._main_menu_frame)


    def _show_game_frame(self):
        self._show_frame(self._game_display_frame)
    

    def _show_rules_frame(self):
        self._show_frame(self._about_rules_frame)
        

    def _create_buttons(self, parent, buttons):
        for _, b in buttons.items():
            button = tk.Button(parent, background = consts.PRIMARY, text = b["text"], font=(consts.MAIN_FONT, 18), command = b["command"])
            button.place(relx = b["relx"], rely = b["rely"], anchor = CENTER, width = b.get("width", 100), height = b.get("height", 50))
    

    def _show_frame(self, frame):
        frame.tkraise()
    

    def _create_main_menu(self, image):
        frame = tk.Frame(self._main_window)
        self._main_menu_frame = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self._main_menu_canvas = tk.Canvas(frame, height=600, width=600, bd=0, highlightthickness=1)
        self._main_menu_canvas.create_image(0, 0, image=image, anchor=NW, tags="IMG")
        self._main_menu_canvas.pack(side=TOP, fill=BOTH, expand=True)
        self._create_buttons(self._main_menu_canvas, self._get_menu_buttons())


    def game_screen_display(self):
        root = self._main_window
        game_display_frame = tk.Frame(root, bg=consts.REGULAR_COLOR,
                               highlightbackground=consts.REGULAR_COLOR,
                               highlightthickness=5, width=600, height=600)

        self.side_display_maker(game_display_frame)
        self.current_word_display(game_display_frame)

        self.four_by_four_maker(game_display_frame)
        game_display_frame.grid(row=0, column=0, sticky="nsew")
        self._game_display_frame = game_display_frame


    def side_display_maker(self, frame):
        root = self._main_window
        frame_for_side_bar = tk.Frame(frame, bg=consts.REGULAR_COLOR,
                               highlightbackground="black",
                               highlightthickness=5)
        frame_score = tk.Frame(frame_for_side_bar, bg=consts.REGULAR_COLOR,
                               highlightbackground=consts.REGULAR_COLOR,
                               highlightthickness=5)

        score_title = tk.Label(frame_score, text = "SCORE:", font = (consts.MAIN_FONT, 30))
        score_title.pack()

        score_actual = tk.Label(frame_score, text = "9999", font = (consts.MAIN_FONT, 30))
        score_actual.pack()
        frame_score.pack()
        button = tk.Button(frame, background = consts.SECONDARY, text = "Go Back", font=(consts.MAIN_FONT, 18), command = self._show_main_menu_frame)
        button.pack()
        

        ######################
        frame_time = tk.Frame(frame_for_side_bar, bg=consts.REGULAR_COLOR,
                            highlightbackground=consts.REGULAR_COLOR,
                            highlightthickness=5)
        time_title = tk.Label(frame_time, text="TIME:",
                                    font=(consts.MAIN_FONT, 30))
        time_title.pack()
        time_actual = tk.Label(frame_time, text="9999",
                                     font=(consts.MAIN_FONT, 30))
        time_actual.pack()
        frame_time.pack()
        #####################
        frame_found_words = tk.Frame(frame_for_side_bar, bg=consts.REGULAR_COLOR,
                           highlightbackground=consts.REGULAR_COLOR,
                           highlightthickness=5)
        words_title = tk.Label(frame_found_words, text="WORDS:",
                                   font=(consts.MAIN_FONT, 30))
        words_title.pack()
        words_actual = tk.Label(frame_found_words, text="test",
                                    font=(consts.MAIN_FONT, 30))
        words_actual.pack()
        frame_found_words.pack()
        frame_for_side_bar.pack(side = tk.LEFT)


    def current_word_display(self,frame):
        root = self._main_window
        frame_display = tk.Frame(frame,  bg=consts.SECONDARY,
                               highlightbackground=consts.SECONDARY,
                               highlightthickness=5)
        label = tk.Label(frame_display, text = "test", font = (consts.MAIN_FONT, 50))
        label.pack()
        frame_display.pack(side = tk.TOP)


    def four_by_four_maker(self, frame) -> None:
        for i in range(4):
            frame_grid = tk.Frame(frame, bg="black",
                               highlightbackground=consts.SECONDARY,
                               highlightthickness=5)
            for j in range(4):
                b = tk.Button(frame_grid, text= str(i)+","+str(j), bg = consts.PRIMARY,font=(consts.MAIN_FONT, 30))
                b.pack()
            frame_grid.pack(side = tk.LEFT)


    def _about_rules_screen(self):
        root = self._main_window
        frame = tk.Frame(root, height=300, width=450)
        self._about_rules_frame = frame
        l1 = tk.Label(frame, text = "Rules", font = (consts.MAIN_FONT, 18, BOLD), justify=LEFT)
        l2 = tk.Label(frame, text = consts.RULES, font = (consts.MAIN_FONT, 14), wraplength=600, justify=LEFT)
        l3 = tk.Label(frame, text = "About", font = (consts.MAIN_FONT, 18, BOLD), justify=LEFT)
        l4 = tk.Label(frame, text = consts.ABOUT, font = (consts.MAIN_FONT, 14), wraplength=600, justify=LEFT)
        button = tk.Button(frame, background = consts.SECONDARY, text = "Go Back", font=(consts.MAIN_FONT, 18), command = self._show_main_menu_frame)
        button.place(relx = 0.1, rely = 0.9, anchor = CENTER, width = 100, height = 50)
        frame.grid(row=0, column=0, sticky="nsew")
        for l in [l1, l2, l3, l4]:
            l.pack(anchor=W, padx=30, pady=10)


    def _center(self, root):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        root.update_idletasks()
        width = root.winfo_width()
        frm_width = root.winfo_rootx() - root.winfo_x()
        win_width = width + 2 * frm_width
        height = root.winfo_height()
        titlebar_height = root.winfo_rooty() - root.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = root.winfo_screenwidth() // 2 - win_width // 2
        y = root.winfo_screenheight() // 2 - win_height // 2
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        root.deiconify()
    
    
    def _get_menu_buttons(self):
        return {
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
                "command": self._show_rules_frame,
                "relx" : 0.95,
                "rely": 0.95,
                "width": 50,
                "height": 30
            },
            
        }

if __name__ == "__main__":
    ui = UserInterface()
    #ui.run()
