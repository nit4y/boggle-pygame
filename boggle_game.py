
from boggle_board_randomizer import randomize_board
from tkinter import StringVar
import time

class BoggleGame():
    def __init__(self) -> None:
        # None of those should be private because they are used mostly outside the class
        self.score = 0
        self.timer = int(3)*60
        self.board = randomize_board()
        self.discovered = set()
        self.discovered_str = None
        self.current_word = None
        self.word_set = self._load_word_dict_from_file("boggle_dict.txt")

    def countdowntimer(self):
            minute, second = (self.timer // 60, self.timer % 60)
            if second == 0:
                second = "00"
            elif second < 10:
                second = ("0" + str(second))
            minute = "0" + str(minute)
            # Update the time
            self.root.update()
            if (self.timer == 0):
                minute = '00'
                second = '00'
            self.timer -= 1
            self.time_string.set("{:02d}:{:02d}".format(int(minute), int(second)))

            print(str(self.timer))
            self.root.after(1000, self.countdowntimer)

    def set_root(self, root):
        self.root = root

    def set_timer(self,time):
        self.time_string = time


    def _load_word_dict_from_file(self, filename):
        return set(open(filename).read().splitlines())


    def player_choosing(self, letter):
        self.current_word.set(self.current_word.get() + letter)
        if self.current_word.get() in self.word_set:
            print(self.current_word.get())
            self.add_discovery(self.current_word)
            self.score+=len(self.current_word.get())**2
            self.current_word.set("")
        
    def add_discovery(self, word):
        self.discovered.add(word.get())
        self.discovered_str.set(", ".join(self.discovered))

    def delete_last_letter(self):
        if len(self.current_word.get()) > 0:
            self.current_word.set(self.current_word.get()[:-1])

    
    def activate_end_message(self):
        pass

    def _set_timer(self, timer):
        self.timer = timer


    def _tick_timer(self):
        if self.timer > 0:
            # call countdown again after 1000ms (1s)
            self.timer -= 1

    def set_current_word(self, current_word):
        self.current_word = current_word


    def set_discovered_str(self, discovered):
        self.discovered_str = discovered


    def start_game(self):
       # self._tick_timer()
        self.activate_end_message()


    

