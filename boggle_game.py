
from typing import Set, Tuple
from boggle_board_randomizer import randomize_board
from ex12_utils import is_near_previous
import consts
from tkinter import Tk, StringVar

class BoggleGame():
    """
    A class thats used to make all calculations for the Boggle game.
    """
    def __init__(self) -> None:
        """
        initializes a BoggleGame instance
        :return: None
        """
        self.score = None
        self.timer = int(1)*60
        self.board = randomize_board()
        self.discovered = set()
        self.discovered_str = None
        self.current_word = None
        self._used_locations = []
        self.word_set = self._load_word_dict_from_file(consts.DICT_FILE_PATH)
        self.continue_timer = False


    def countdown(self) -> None:
        """
        makes and manages the countdown timer for the game
        :return: None
        """
        minute, second = (self.timer // 60, self.timer % 60)
        if second == 0:
            second = "00"
        elif second < 10:
            second = ("0" + str(second))
        minute = "0" + str(minute)
        if (self.timer < 30):
            self.root._time_actual.configure(fg="red")
        if (self.timer == 0):
            minute = '00'
            second = '00'
            self.time_string.set("{:02d}:{:02d}".format(int(minute), int(second)))
            self.root.show_end_message()
            return
        self.timer -= 1
        self.time_string.set("{:02d}:{:02d}".format(int(minute), int(second)))
        if self.continue_timer:
            self.root._main_window.after(1000, self.countdown)


    def set_root(self, root: Tk) -> None:
        """
        setter method for the root property
        :param root: the root to set
        :return: None
        """
        self.root = root


    def set_timer(self, time):
        """
        setter method for the timer property
        :param time: the time to set
        """
        self.time_string = time


    def _load_word_dict_from_file(self, filename: str) -> Set:
        """
        loads a word set from a file
        :param filename: the file path
        :return: a set of the words in the file seperated by newline
        """
        return set(open(filename).read().splitlines())


    def _is_choose_legal(self, location: Tuple) -> bool:
        """
        calculates if a user square choosing is legal
        :return: True if it is, False otherwise
        """
        if len(self._used_locations) > 0:
            if not is_near_previous(self._used_locations[-1], location):
                return False
        if location in self._used_locations:
            return False
        return True


    def player_choosing(self, letter: str, location: Tuple) -> None:
        """
        processes a player choosing, executes all relevant triggers. (route marking, changing the word string and such)
        :param letter: the letter the player chose
        :param location: the location of that letter on the board
        :return: None
        """
        if not self._is_choose_legal(location):
            return
        self._used_locations.append(location)
        if self.current_word.get() == consts.SUCCESS_MESSAGE:
            self.current_word.set(letter)
        else:
            self.current_word.set(self.current_word.get() + letter)
        self.root.mark_next_move_squares(location)
        attempt = self.current_word.get()
        if attempt not in self.discovered and attempt in self.word_set:
            self._add_discovery(self.current_word)
            self.score.set(self.score.get() + len(self.current_word.get())**2)
            self.current_word.set(consts.SUCCESS_MESSAGE)
            self._used_locations = []
            self.root.clean_markings_from_board()


    def _add_discovery(self, word: StringVar) -> None:
        """
        adds a word discovery to the set of the player's discoveries
        :return: None
        """
        self.discovered.add(word.get())
        self.discovered_str.set(", ".join(self.discovered))


    def delete_last_letter(self) -> None:
        """
        deletes the last choosing of the player from all relevant savings
        :return: None
        """
        try:
            x, y = self._used_locations.pop()
            if len(self.current_word.get()) > 0:
                self.current_word.set(self.current_word.get()[:-len(self.board[x][y])])
                self.root.mark_next_move_squares(self._used_locations[-1])
        except IndexError as e:
            self.root.clean_markings_from_board()


    def set_current_word(self, current_word: StringVar) -> None:
        """
        setter method for the current_word property
        :param current_word:
        :return: None
        """
        self.current_word = current_word


    def set_discovered_str(self, discovered: StringVar) -> None:
        """
        setter method for the discovered_str property
        :return: None
        """
        self.discovered_str = discovered
    

    def set_score(self, score) -> None:
        """
        setter method for the score property
        :return: None
        """
        self.score = score
    

    def restart(self) -> None:
        """
        reinitiates the object, restarts the game in logic
        :return: None
        """
        self.__init__()


    def start_timer(self) -> None:
        """
        starts the timer in terms of the game loop managemenet
        :return: None
        """
        self.continue_timer = True


    def stop_timer(self):
        """
        stops the timer in terms of the game loop managemenet
        :return: None
        """
        self.continue_timer = False

