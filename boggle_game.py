
from boggle_board_randomizer import randomize_board
from tkinter import StringVar

class BoggleGame():
    def __init__(self) -> None:
        # None of those should be private because they are used mostly outside the class
        self.score = 0
        self.timer = 0
        self.board = randomize_board()
        self.discovered = {}
        self.current_word = None
        self.word_set = self._load_word_dict_from_file("boggle_dict.txt")
    

    def _load_word_dict_from_file(self, filename):
        return set(open(filename))


    def player_choosing(self, letter):
        self.current_word.set(self.current_word.get() + letter)
        if self.current_word.get() in self.word_set:
            self.discovered.add(self.current_word)
            self.score+=len(self.current_word)**2
            self.current_word = ""
        
    
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
            self.root.after(1000, self._tick_timer(), self.timer - 1)

    def set_current_word(self, current_word):
        self.current_word = current_word

    def start_game(self):
        self._tick_timer()
        self.activate_end_message()
            
    

