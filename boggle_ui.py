# Web pages we used: https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter

import tkinter as tk
from tkinter import CENTER, TOP, BOTH, NW
from tkinter.constants import LEFT, RIGHT, W
from tkinter.font import BOLD
import consts
from boggle_game import BoggleGame

class BoggleUserInterface(object):
    def __init__(self, game: BoggleGame) -> None:

        # Initilization
        root = tk.Tk()
        self.game = game
        self.game.set_root(root)
        self._set_game_variables()
        self._main_window = root
        root.title("Boggle")
        root.iconbitmap('assets/icon.ico')

        # Loading assets
        self._load_assets()
        

        # Creating screens
        self._create_main_menu(self.icons["menu-bg"])

        # Initiate play frame
        
        self._about_rules_screen()
        self._show_main_menu_frame()
        self._center(root)


    def run(self) -> None:
        self._main_window.mainloop()
    

    def exit(self) -> None :
        self._main_window.destroy()


    def _show_main_menu_frame(self):
        self.game.stop_timer()
        self._show_frame(self._main_menu_frame)


    def _show_game_frame(self):
        self.game.restart()
        self._set_game_variables()
        self.game.start_timer()
        self.game.countdown()
        self._game_screen_display()
        self._show_frame(self._game_display_frame)
    

    def _show_rules_frame(self):
        self._show_frame(self._about_rules_frame)


    def _load_assets(self):
        self.icons = {
            "backspace": tk.PhotoImage(file="assets/backspace_resized.png"),
            "menu-bg": tk.PhotoImage(file="assets/resized.png")
        }
        

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
        self._main_menu_canvas.pack(side=TOP, fill=BOTH, expand=False)
        self._create_buttons(self._main_menu_canvas, self._get_menu_buttons())


    def _game_screen_display(self):
        root = self._main_window
        game_display_frame = tk.Frame(root, bg=consts.REGULAR_COLOR,
                               highlightbackground=consts.REGULAR_COLOR,
                               highlightthickness=5, width=600, height=600)

        self._side_display_maker(game_display_frame)
        self._current_word_display(game_display_frame)

        self._four_by_four_maker(game_display_frame)
        game_display_frame.grid(row=0, column=0, columnspan=20, sticky="nsew")
        self._game_display_frame = game_display_frame



    def _create_score_frame(self, parent):
        frame_score = tk.Frame(parent, bg=consts.REGULAR_COLOR,
                               highlightbackground=consts.REGULAR_COLOR,
                               highlightthickness=5)
        score_title = tk.Label(frame_score, text = "SCORE:", font = (consts.MAIN_FONT, 30))
        score_title.grid(row=0, column=0)
        score_actual = tk.Label(frame_score, textvariable = self.game.score, font = (consts.MAIN_FONT, 30))
        score_actual.grid(row=1, column=0)
        frame_score.grid(row=0,column=0)


    def _create_time_frame(self, parent): 
        frame_time = tk.Frame(parent, bg=consts.REGULAR_COLOR,
                            highlightbackground=consts.REGULAR_COLOR,
                            highlightthickness=5)
        time_title = tk.Label(frame_time, text="TIME:", font=(consts.MAIN_FONT, 30))
        time_title.grid(row=0,column=0)
        time_actual = tk.Label(frame_time, textvariable = self.game.time_string ,font=(consts.MAIN_FONT, 30))
        time_actual.grid(row=1,column=0)
        frame_time.grid(row=1, column=0)
    

    def _create_words_frame(self, parent):
        frame_found_words = tk.Frame(parent, bg=consts.REGULAR_COLOR,
                           highlightbackground=consts.REGULAR_COLOR,
                           highlightthickness=5)
        words_title = tk.Label(frame_found_words, text="WORDS:",
                                   font=(consts.MAIN_FONT, 30))
        words_title.grid(row=0, column=0)
        words_actual = tk.Label(frame_found_words, textvariable = self.game.discovered_str, font=(consts.MAIN_FONT, 14))
        words_actual.grid(row=1, column=0)
        frame_found_words.grid(row=2, column=0)


    def _side_display_maker(self, parent):
        frame_for_side_bar = tk.Frame(parent, bg=consts.REGULAR_COLOR,
                               highlightbackground="black",
                               highlightthickness=5)
        button = tk.Button(parent, background = consts.SECONDARY, text = "Quit", font=(consts.MAIN_FONT, 18), command = self._show_main_menu_frame)
        button.grid(row=5,column=0)
        self._create_score_frame(parent = frame_for_side_bar)
        self._create_time_frame(parent = frame_for_side_bar)
        self._create_words_frame(parent = frame_for_side_bar)
        frame_for_side_bar.grid(row=1, column=0, rowspan=4)


    def _current_word_display(self, frame):
        frame_display = tk.Frame(frame,  bg=consts.SECONDARY,
                               highlightbackground=consts.SECONDARY,
                               highlightthickness=5)
        label = tk.Label(frame_display, textvariable=self.game.current_word, font = (consts.MAIN_FONT, 50))
        label.grid(row=0, column=0, sticky='ew')
        button = tk.Button(frame_display, font = (consts.MAIN_FONT, 50), image=self.icons["backspace"], width = 40, height = 40, command=self.game.delete_last_letter)
        button.grid(row=0, column=1, sticky='w')
        frame_display.grid(row=0, column=0, columnspan=10, sticky='ew')


    def _four_by_four_maker(self, frame) -> None:
        board = self.game.board
        frame_grid = tk.Frame(frame, bg="black",
                               highlightbackground=consts.SECONDARY,
                               highlightthickness=5)
        for i in range(4):
            for j in range(4):
                b = tk.Button(frame_grid, text= board[i][j], bg = consts.PRIMARY,font=(consts.MAIN_FONT, 30), command= lambda letter = board[i][j], loc = (i,j): self.game.player_choosing(letter, loc))
                b.grid(row=i, column=j)
        frame_grid.grid(row=2, column=1)


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
    

    def _set_game_variables(self):
        self.game.set_current_word(tk.StringVar())
        self.game.set_discovered_str(tk.StringVar())
        self.game.set_timer(tk.StringVar())
        self.game.set_score(tk.IntVar())
    

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
