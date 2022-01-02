from typing import Tuple
import math

def is_near_previous(previous, current):
    cur_y, cur_x = current[0], current[1]
    prev_y, prev_x = previous[0], previous[1]
    return abs(prev_y - cur_y) in [0, 1] and abs(prev_x - cur_x) in [0, 1]


def is_valid_path(board, path, words):
    path_word = ""
    for i, loc in enumerate(path):
        if i != 0:
            if not is_near_previous(path[i-1], loc):
                return None
        y, x = loc[0], loc[1]
        path_word+=board[y][x]
    for word in words:
        if word == path_word:
            return word
    return None

    

def find_length_n_paths(n, board, words):
    pass

def find_length_n_words(n, board, words):
    pass

def max_score_paths(board, words):
    pass

if __name__ == "__main__":
    print(is_valid_path([["a","b","c"],["d","e","f"],["g","h","i"]], [(0,0),(0,1),(0,2)], ["ccc"]))

