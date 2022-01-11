# Web pages we used: https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter

import tkinter as tk
from tkinter import messagebox, CENTER, TOP, BOTH, NW
from tkinter.constants import LEFT, W
from tkinter.font import BOLD
from typing import Dict, Tuple
import consts
from boggle_game import BoggleGame
from pygame import mixer


def play_song(name: str) -> None:
    """
    plays a song via pygames mixer
    :param name: path to the song file
    :return: None
    """
    mixer.music.load(name)
    mixer.music.set_volume(consts.MUSIC_VOLUME)
    mixer.music.play()

class BoggleUserInterface(object):
    """
    A class representing the Boggle game User Interface
    """
    def __init__(self, game: BoggleGame) -> None:
        """
        initializes a BoggleUserInterface instance
        :param game: a BoggleGame instance to manage all dynamic variables and make calculations
        :return: None
        """
        # Initilization
        root = tk.Tk()
        root.attributes('-alpha', 0) # make it invisible until all ui builds
        
        self.game = game
        self.game.set_root(self)
        self._set_game_variables()
        self._main_window = root
        root.title(consts.APP_NAME)

        mixer.init()

        # Loading assets
        self._load_assets()
        
        # Creating screens
        self._create_main_menu(self._icons["menu-bg"])        
        self._about_rules_screen()
        self._show_main_menu_frame()
        self._center(root)
        root.resizable(False, False) 
        root.attributes('-alpha', 1.0)


    def run(self) -> None:
        """
        runs the application via tkinter's mainloop
        :return: None
        """
        self._main_window.mainloop()
    

    def exit(self) -> None :
        """
        exits the application, ends the main loop
        :return: None
        """
        self._main_window.destroy()


    def show_end_message(self) -> None:
        """
        shows the ending message pop up for the game
        :return: None
        """
        self.game.stop_timer()
        root = tk.Tk()
        self._center(root)
        frame = tk.Frame(root, width=300, height = 250)
        l1 = tk.Label(frame, text="SCORE: " + str(self.game.score.get()) + "\nWant to play another game?\n", wraplength=150)
        yb = tk.Button(frame, text = "Yes", font=(consts.MAIN_FONT, 14), command=lambda r = root: self._show_game_frame_and_destroy(r))
        nb = tk.Button(frame, text = "No", font=(consts.MAIN_FONT, 14), command=lambda r = root: self._show_main_menu_frame_and_destroy(r))
        l1.place(relx=0.1, rely=0.1)
        yb.place(relx=0.2, rely=0.6)
        nb.place(relx=0.6, rely=0.6)
        frame.pack(expand=True)


    def _show_main_menu_frame(self, play: bool = True) -> None:
        """
        brings the main menu frame to the front, shows it to the user and plays the menu theme song
        :return: None
        """
        if play:
            play_song('assets/menu-theme.mp3')
        self.game.stop_timer()
        self._show_frame(self._main_menu_frame)


    def _show_game_frame(self) -> None:
        """
        brings the game frame to the front, shows it to the user and plays the game theme song
        :return: None
        """
        play_song('assets/game-theme.mp3')
        self.game.restart()
        self._set_game_variables()
        self.game.start_timer()
        self.game.countdown()
        self._create_game_screen_display()
        self._game_display_frame.grid_columnconfigure(0, weight=2)
        self._game_display_frame.grid_columnconfigure(1, weight=1)
        self._game_display_frame.grid_rowconfigure(0, weight=2)
        self._game_display_frame.grid_rowconfigure(1, weight=1)
        self._show_frame(self._game_display_frame)
    

    def _show_rules_frame(self):
        """
        brings the rules frame to the front, shows it to the user
        :return: None
        """
        self._show_frame(self._about_rules_frame)


    def _show_frame(self, frame) -> None:
        """
        a generic method to bring any frame to the front, so the user can see it
        :param frame: the frame to bring to front
        :return: None
        """
        frame.tkraise()


    def _load_assets(self) -> None:
        """
        load assets to variables
        :return: None
        """
        self._main_window.iconbitmap('assets/icon.ico')
        self._icons = {
            "backspace": tk.PhotoImage(file="assets/backspace_resized.png"),
            "menu-bg": tk.PhotoImage(file="assets/resized.png")
        }
        

    def _create_buttons(self, parent: tk.Widget, buttons: Dict) -> None:
        """
        create buttons for the main menu
        :param parent: the root parent to assign buttons to
        :param buttons: a dictionary of buttons to create the buttons by, see _get_menu_buttons
        :return: None
        """
        for _, b in buttons.items():
            button = tk.Button(parent, background = consts.SECONDARY, text = b["text"], font=(consts.MAIN_FONT, 18), command = b["command"])
            button.place(relx = b["relx"], rely = b["rely"], anchor = CENTER, width = b.get("width", 150), height = b.get("height", 50))
    

    def _create_main_menu(self, image: tk.PhotoImage) -> None:
        """
        creates the main menu frame on all its widgets
        :param image: image to assign as background canvas
        :return: None
        """
        frame = tk.Frame(self._main_window)
        self._main_menu_frame = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self._main_menu_canvas = tk.Canvas(frame, height=600, width=600, bd=0, highlightthickness=1)
        self._main_menu_canvas.create_image(0, 0, image=image, anchor=NW, tags="IMG")
        self._main_menu_canvas.pack(side=TOP, fill=BOTH, expand=False)
        self._create_buttons(self._main_menu_canvas, self._get_menu_buttons())


    def _create_game_screen_display(self) -> None:
        """
        creates the game screen frame on all its widgets
        :return: None
        """
        root = self._main_window
        game_display_frame = tk.Frame(root, bg=consts.PRIMARY,
                               highlightbackground=consts.PRIMARY,
                               highlightthickness=5, width=600, height=600)

        self._create_side_display(game_display_frame)
        self._current_word_display(game_display_frame)

        self._four_by_four_maker(game_display_frame)
        game_display_frame.grid(row=0, column=0, columnspan=20, sticky="nsew")
        self._game_display_frame = game_display_frame



    def _create_score_frame(self, parent: tk.Widget) -> None:
        """
        creates score frame on all its widgets
        :param parent: the parents to assign the root frame
        :return: None
        """
        frame_score = tk.Frame(parent, bg= consts.SECONDARY,
                               highlightbackground=consts.SECONDARY,
                               highlightthickness=5)
        score_title = tk.Label(frame_score, text = "SCORE:", font = (consts.MAIN_FONT, 30, "underline",),bg= consts.SECONDARY)
        score_title.grid(row=0, column=0)
        score_actual = tk.Label(frame_score, textvariable = self.game.score, font = (consts.MAIN_FONT, 30),bg= consts.SECONDARY)
        score_actual.grid(row=1, column=0)
        frame_score.grid(row=0,column=0)


    def _create_time_frame(self, parent: tk.Widget) -> None: 
        """
        creates the time left frame on all its widgets
        :param parent: the parents to assign the root frame
        :return: None
        """
        frame_time = tk.Frame(parent, bg= consts.SECONDARY,
                            highlightbackground= consts.SECONDARY,
                            highlightthickness=5)
        time_title = tk.Label(frame_time, text="TIME:", font=(consts.MAIN_FONT, 30, "underline"),bg= consts.SECONDARY)
        time_title.grid(row=0,column=0)
        time_actual = tk.Label(frame_time, textvariable = self.game.time_string ,font=(consts.MAIN_FONT, 30),bg= consts.SECONDARY)
        time_actual.grid(row=1,column=0)
        self._time_actual = time_actual
        frame_time.grid(row=1, column=0)
    

    def _create_words_frame(self, parent: tk.Widget) -> None:
        """
        creates the words discovered frame on all its widgets
        :param parent: the parents to assign the root frame
        :return: None
        """
        frame_found_words = tk.Frame(parent, bg=consts.SECONDARY,
                           highlightbackground= consts.SECONDARY,
                           highlightthickness=2)
        words_title = tk.Label(frame_found_words, text="WORDS:",
                                   font=(consts.MAIN_FONT, 30, "underline"), bg = consts.SECONDARY)
        words_title.grid(row=0, column=0)
        words_actual = tk.Label(frame_found_words, bg= consts.SECONDARY, textvariable = self.game.discovered_str, font=(consts.MAIN_FONT, 12), wraplength=150)
        words_actual.grid(row=1, column=0)
        frame_found_words.grid(row=2, column=0)


    def _create_side_display(self, parent: tk.Widget) -> None:
        """
        creates the side display frame on all its widgets
        :param parent: the parents to assign the root frame
        :return: None
        """
        frame_for_side_bar = tk.Frame(parent, bg= consts.SECONDARY,
                               highlightbackground=consts.BLACK,
                               highlightthickness=2)
        self._create_score_frame(parent = frame_for_side_bar)
        self._create_time_frame(parent = frame_for_side_bar)
        self._create_words_frame(parent = frame_for_side_bar)

        b = tk.Button(parent, text="Quit", bg= "black", fg="white", font=(consts.MAIN_FONT, 14), command=self._show_main_menu_frame)
        b.grid(row=4, column=0, sticky = "new")
        frame_for_side_bar.grid(row=1, column=0, rowspan=4, sticky = "nsew")

    def _current_word_display(self, frame: tk.Widget) -> None:
        """
        creates the current choosed word frame on all its widgets
        :param parent: the parents to assign the root frame
        :return: None
        """
        frame_display = tk.Frame(frame,  bg=consts.SECONDARY,
                               highlightbackground=consts.BLACK,
                               highlightthickness=2)
        label = tk.Label(frame_display, bg=consts.SECONDARY, textvariable=self.game.current_word, font = (consts.MAIN_FONT, 43), wraplength=560,width=16)
        label.grid(row=0, column=0, sticky='w')
        button = tk.Button(frame_display, font = (consts.MAIN_FONT, 50), image=self._icons["backspace"], width = 60, height = 60, command=self.game.delete_last_letter)
        button.grid(row=0, column=3, sticky='e')
        frame_display.grid(row=0, column=0, columnspan=10, sticky='ew')


    def _four_by_four_maker(self, frame: tk.Widget) -> None:
        """
        creates the words discovered frame on all its widgets
        :param frame: the parents to assign the root frame
        :return: None
        """
        board = self.game.board
        self.buttons_board = []
        frame_grid = tk.Frame(frame, bg=consts.BLACK,
                               highlightbackground=consts.BLACK,
                               highlightthickness=2, width = 400, height = 400)
        for i in range(4):
            self.buttons_board.append([])
            for j in range(4):
                b = tk.Button(frame_grid, text= board[i][j], bg = consts.ORANGE,font=(consts.MAIN_FONT, 30), command= lambda letter = board[i][j], loc = (i,j): self.game.player_choosing(letter, loc), height = 2,width = 4)
                b.grid(row=i, column=j)
                self.buttons_board[i].append(b)

        frame_grid.grid(row=1, column=1,rowspan=4, sticky="e")


    def _about_rules_screen(self) -> None:
        """
        creates the the about and rules frame on all its widgets
        :return: None
        """
        root = self._main_window
        frame = tk.Frame(root, bg=consts.SECONDARY, height=300, width=450)
        self._about_rules_frame = frame
        l1 = tk.Label(frame, text = "Rules", bg=consts.SECONDARY, font = (consts.MAIN_FONT, 18, BOLD), justify=LEFT)
        l2 = tk.Label(frame, text = consts.RULES, bg=consts.SECONDARY, font = (consts.MAIN_FONT, 14), wraplength=600, justify=LEFT)
        l3 = tk.Label(frame, text = "About", bg=consts.SECONDARY,  font = (consts.MAIN_FONT, 18, BOLD), justify=LEFT)
        l4 = tk.Label(frame, text = consts.ABOUT, bg=consts.SECONDARY, font = (consts.MAIN_FONT, 14), wraplength=600, justify=LEFT)
        button = tk.Button(frame, background = consts.ORANGE, text = "Back", font=(consts.MAIN_FONT, 18), command = lambda play = False: self._show_main_menu_frame(play))
        button.place(relx = 0.1, rely = 0.9, anchor = CENTER, width = 100, height = 50)
        frame.grid(row=0, column=0, sticky="nsew")
        for l in [l1, l2, l3, l4]:
            l.pack(anchor=W, padx=30, pady=10)

    
    def clean_markings_from_board(self) -> None:
        """
        paints all the button board with orange (default)
        :return: None
        """
        for row in self.buttons_board:
            for b in row:
                b.configure(bg=consts.ORANGE)


    def mark_next_move_squares(self, location: Tuple) -> None:
        """
        marks certain squares in the buttons grid that the player can choose as the next move
        :param parent: the parents to assign the root frame
        :return: None
        """
        self.clean_markings_from_board()
        x, y = location
        for x_mod, y_mod in consts.DIRECTIONS:
            try:
                new_x, new_y = x+x_mod, y+y_mod
                if new_x < 0 or new_y < 0:
                    raise IndexError
                b = self.buttons_board[x+x_mod][y+y_mod]
                b.configure(bg="#ff8c66")
            except (KeyError, IndexError):
                pass



    def _center(self, root: tk.Tk) -> None:
        """
        centers a tkinter window
        :param root: the main window or Toplevel window to center
        :return: None
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
    

    def _set_game_variables(self) -> None:
        """
        assigns default values for the game
        :return: None
        """
        self.game.set_current_word(tk.StringVar())
        self.game.set_discovered_str(tk.StringVar())
        self.game.set_timer(tk.StringVar())
        self.game.set_score(tk.IntVar())
    

    def _get_menu_buttons(self) -> Dict:
        """
        returns a dicitionary that represents all the buttons in the main menu
        :return: the dictionary
        """
        return {
            1: {
                "text": "Start Game",
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
    
    def _show_game_frame_and_destroy(self, root: tk.Tk) -> None:
        """
        shows game frame and destroys root
        """
        self._show_game_frame()
        root.destroy()
    

    def _show_main_menu_frame_and_destroy(self, root: tk.Tk) -> None:
        """
        shows game frame and destroys root
        """
        self._show_main_menu_frame()
        root.destroy()
