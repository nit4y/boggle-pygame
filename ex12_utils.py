from typing import Tuple
import math

def is_near_previous(previous, current):
    cur_y, cur_x = current[0], current[1]
    prev_y, prev_x = previous[0], previous[1]
    return abs(prev_y - cur_y) in [0, 1] and abs(prev_x - cur_x) in [0, 1]


def is_valid_path(board, path, words):
    path_word = ""
    used_locations = []
    for i, loc in enumerate(path):
        if i != 0:
            if not is_near_previous(path[i-1], loc):
                return None
        y, x = loc[0], loc[1]
        if (y, x) in used_locations:
            return None
        path_word += board[y][x]
        used_locations.append((y, x))
    for word in words:
        if word == path_word:
            return word
    return None

    
def _are_locations_legal(locations: list[(int,int)]) -> bool:
    used_locations = []
    for i , location in enumerate(locations):
        if i != 0:
            if not is_near_previous(locations[i-1], location):
                return False
        y,x = location[0],location[1]
        if not(0 <= y <= 3 and 0 <= x <= 3):
            return False
        if location in used_locations:
            return False
        used_locations.append(location)
    return True

def _does_word_have_future(word, words) -> bool:
    pass


def find_length_n_paths(n, board, words):
    words_with_n_length = []
    for word in words:
        if len(word) == n:
            words_with_n_length.append(word)

    for y in range(4):
        for x in range(4):
            current_location = [(y,x)]
            word_first_letter = board[y][x]
            _find_length_n_paths_core(n,board,(y,x),[],"",words_with_n_length)


DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]

def _find_length_n_paths_core(n, board, cur_location, used_locations, word, words):
    if len(word) >= n:
        if word in words:
            return word
        return

    used_locations.append(cur_location)
    if not _are_locations_legal(used_locations):
        return

    y, x = cur_location[0], cur_location[1]
    #print(used_locations)
    word += board[y][x]
    for direction in DIRECTIONS:
        new_location = ( y + direction[0], x + direction[1])
        _find_length_n_paths_core(n,board,new_location,used_locations[:], word[:], words)






def find_length_n_words(n, board, words):
    pass

def max_score_paths(board, words):
    pass

if __name__ == "__main__":
    board = [["a","b","c","d"],["e","f","g","h"],["i","j","k","l"],["m","n","o","p"]]
    words = ["abc","def","ghif","ab"]
    #print(is_valid_path([["a","b","c"],["d","e","f"],["g","h","i"]], [(0,0),(0,1),(0,2)], ["ccc"]))
    print(find_length_n_paths(3,board,words))
   # print(_are_locations_legal( [(0,0),(0,1),(0,0)])) #FALSE
    #print(_are_locations_legal([(0, 0), (0, 1), (0, 2)])) #TRUE
    #print(_are_locations_legal([(0, 0), (0, 1), (-1,1)]))  # FALSE
   # print(_are_locations_legal([(0, 0), (0, 2), (3,3)]))  # FALSE
    #print(_are_locations_legal([(0, 0), (0, 1), (1, 1),(2,2)]))  #TRUE
