from typing import Tuple
import consts

def filter_words(board, words, n):
    if n == 0:
        return []
    essential_chars = []
    filtered_words = []
    for row in board:
        for cell in row:
            essential_chars.append(cell)
    for word in words:
        if 2*n >= len(word) >= n :
            add = True
            for c in word:
                if c not in word:
                    add = False
                    break
            if add:
                filtered_words.append(word)
    return filtered_words
                    

def filter_words_for_max_score(board, words):
    essential_chars = []
    filtered_words = []
    for row in board:
        for cell in row:
            essential_chars.append(cell)
    for word in words:
        add = True
        for c in word:
            if c not in essential_chars:
                add = False
                break
        if add:
            filtered_words.append(word)
    return filtered_words


def __is_near_previous(previous, current):
    cur_y, cur_x = current[0], current[1]
    prev_y, prev_x = previous[0], previous[1]
    return abs(prev_y - cur_y) in [0, 1] and abs(prev_x - cur_x) in [0, 1]

def __is_loc_valid(loc: Tuple[int]):
    y, x = loc[0], loc[1]
    if y > 3 or y < 0 or x > 3 or x < 0:
        return False
    return True

def is_valid_path(board, path, words):
    path_word = ""
    used_locations = []
    for i, loc in enumerate(path):
        if not __is_loc_valid(loc):
            return None
        if i != 0:
            if not __is_near_previous(path[i-1], loc):
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
            if not __is_near_previous(locations[i-1], location):
                return False
        y,x = location[0],location[1]
        if not(0 <= y <= 3 and 0 <= x <= 3):
            return False
        if location in used_locations:
            return False
        used_locations.append(location)
    return True


def find_length_n_paths(n, board, words):
    paths = []
    words = set(filter_words(board, words, n))
    for y in range(4):
        for x in range(4):
            __find_length_n_paths_core(x, y , "", n, board, words, [], paths)
    return paths


def __find_length_n_paths_core(x, y, curr_word, n, board, words, used_locations, paths):
    if n > 16 or len(curr_word) > 32:
        return
    if len(used_locations) >= n:
        if curr_word in words:
            if used_locations not in paths:
                paths.append(used_locations)
        return
    
    for y_mod in [0, 1, -1]:
        for x_mod in [0, 1, -1]:
            if y_mod == 0 and x_mod == 0:
                continue
            new_y = y + y_mod
            new_x = x + x_mod
            if 0 <= new_x <= 3 and 0 <= new_y <= 3 and (new_y, new_x) not in used_locations: 
                __find_length_n_paths_core(new_x , new_y, curr_word + board[new_y][new_x], n, board, words, used_locations + [(new_y, new_x)], paths)

def find_length_n_words(n, board, words):
    words_with_n_length = []
    for word in words:
        if len(word) == n:
            words_with_n_length.append(word)
    words_with_n_length = set(words_with_n_length)

    correct_paths = [] #initalizing list we will return
    for y in range(4):
        for x in range(4):
            _find_length_n_words_core(n,board, (y,x), [], "", words_with_n_length,correct_paths)
    return correct_paths

def _find_length_n_words_core(n, board, cur_location, used_locations, word, words, correct_paths):

    used_locations.append(cur_location)
    if not _are_locations_legal(used_locations):
        return

    y, x = cur_location[0], cur_location[1]
    word += board[y][x]

    if len(word) >= n or n > 32:
        if word in words:
           # if used_locations not in correct_paths:
            #    # TODO: needs to backtrack before if attempting an existing path
                correct_paths.append(used_locations)
        return

    for direction in consts.DIRECTIONS:
        new_location = ( y + direction[0], x + direction[1])
        _find_length_n_words_core(n,board, new_location, used_locations[:], word[:], words, correct_paths)


def max_score_paths(board, words):
    words = filter_words_for_max_score(board, words)
    words = set(words)
    all_paths = []  # initalizing list we will return
    for y in range(4):
        for x in range(4):
            _max_score_paths_core(board, words, "", [], (y,x), all_paths)
    longest_paths = _find_longest_paths(all_paths)
    return longest_paths


def _max_score_paths_core(board, words, word, used_locations, cur_location, all_paths):
    used_locations.append(cur_location)
    if not _are_locations_legal(used_locations):
        return

    y, x = cur_location[0], cur_location[1]
    word += board[y][x]

    word_was_found = False
    for tested_word in words:
        if tested_word.startswith(word):
            all_paths.append((word, used_locations))
            word_was_found = True
            break
    if not word_was_found:
        return

    for direction in consts.DIRECTIONS:
        new_location = (y + direction[0], x + direction[1])
        _max_score_paths_core(board, words, word[:], used_locations[:],
                                  new_location, all_paths)


def _find_longest_paths(all_paths):
    longest_paths = []
    used_words = []
    current_longest = 0
    for path_tuple in all_paths:
        word, path = path_tuple[0], path_tuple[1]
        if len(path) > current_longest:
            used_words = [word]
            longest_paths = [path]
            current_longest = len(path)
        if len(path) == current_longest:
            if word not in used_words:
                used_words.append(word)
                longest_paths.append(path)
    return longest_paths


if __name__ == "__main__":
    board = [["a","b","c","d"],["e","f","g","h"],["i","j","k","l"],["m","n","o","p"]]
    words = ["abc","def","ghlp","ab","efj","mno","abcd"]
    #print(is_valid_path([["a","b","c"],["d","e","f"],["g","h","i"]], [(0,0),(0,1),(0,2)], ["ccc"]))
   # print(find_length_n_words(3,board,words))
   # print(_are_locations_legal( [(0,0),(0,1),(0,0)])) #FALSE
    #print(_are_locations_legal([(0, 0), (0, 1), (0, 2)])) #TRUE
    #print(_are_locations_legal([(0, 0), (0, 1), (-1,1)]))  # FALSE
   # print(_are_locations_legal([(0, 0), (0, 2), (3,3)]))  # FALSE
    #print(_are_locations_legal([(0, 0), (0, 1), (1, 1),(2,2)]))  #TRUE
    print(max_score_paths(board,words))