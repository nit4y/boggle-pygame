
from boggle_board_randomizer import randomize_board
from ex12_utils import is_near_previous

class BoggleGame():
    def __init__(self) -> None:
        self.score = None
        self.timer = int(3)*60
        self.board = randomize_board()
        self.discovered = set()
        self.discovered_str = None
        self.current_word = None
        self._used_locations = []
        self.word_set = self._load_word_dict_from_file("boggle_dict.txt")
        self.continue_timer = False


    def countdown(self):
        minute, second = (self.timer // 60, self.timer % 60)
        if second == 0:
            second = "00"
        elif second < 10:
            second = ("0" + str(second))
        minute = "0" + str(minute)
        if (self.timer == 0):
            minute = '00'
            second = '00'
        self.timer -= 1
        self.time_string.set("{:02d}:{:02d}".format(int(minute), int(second)))
        if self.continue_timer:
            self.root.after(1000, self.countdown)


    def set_root(self, root):
        self.root = root


    def set_timer(self,time):
        self.time_string = time


    def _load_word_dict_from_file(self, filename):
        return set(open(filename).read().splitlines())


    def _is_choose_legal(self, location):
        if len(self._used_locations) > 0:
            if not is_near_previous(self._used_locations[-1], location):
                return False
        if location in self._used_locations:
            return False
        return True


    def player_choosing(self, letter, location):
        if not self._is_choose_legal(location):
            return
        self._used_locations.append(location)
        self.current_word.set(self.current_word.get() + letter)
        attempt = self.current_word.get()
        if attempt not in self.discovered and attempt in self.word_set:
            self._add_discovery(self.current_word)
            self.score.set(self.score.get() + len(self.current_word.get())**2)
            self.current_word.set("")
            self._used_locations = []


    def _add_discovery(self, word):
        self.discovered.add(word.get())
        self.discovered_str.set(", ".join(self.discovered))


    def delete_last_letter(self):
        try:
            x, y = self._used_locations.pop()
            if len(self.current_word.get()) > 0:
                self.current_word.set(self.current_word.get()[:-len(self.board[x][y])])
        except IndexError as e:
            print(e)
            pass


    def set_current_word(self, current_word):
        self.current_word = current_word


    def set_discovered_str(self, discovered):
        self.discovered_str = discovered
    

    def set_score(self, score):
        self.score = score
    

    def restart(self):
        self.__init__()


    def start_timer(self):
        self.continue_timer = True


    def stop_timer(self):
        self.continue_timer = False

