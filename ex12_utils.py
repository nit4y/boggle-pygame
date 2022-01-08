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
                    

def __filter_words_for_max_score(board, words):
    essential_chars = []
    filtered_words = []
    for row in board:
        for cell in row:
            essential_chars.append(cell)
    for word in words:
        for char in word:
            if char in essential_chars:
                filtered_words.append(word)
                break
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

    
def __are_locations_legal(locations: list[(int,int)]) -> bool:
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
    if n == 0 or n > 16:
        return []
    paths = []
    words = set(words)
    for y in range(4):
        for x in range(4):
            __find_length_n_paths_core(x, y , "", n, board, words, [], paths)
    return paths


def __find_length_n_paths_core(x, y, curr_word, n, board, words, used_locations, paths):
    if len(curr_word) > 32:
        return
    if len(used_locations) >= n:
        if curr_word in words:
            if used_locations not in paths:
                paths.append(used_locations)
        return
    
    for y_mod, x_mod in consts.DIRECTIONS:
            new_y, new_x = y + y_mod, x + x_mod
            if 0 <= new_x <= 3 and 0 <= new_y <= 3 and (new_y, new_x) not in used_locations: 
                __find_length_n_paths_core(new_x , new_y, curr_word + board[new_y][new_x], n, board, words, used_locations + [(new_y, new_x)], paths)


def find_length_n_words(n, board, words):
    if n == 0 or n > 16:
        return []
    words = set(words)
    correct_paths = [] #initalizing list we will return
    for y in range(4):
        for x in range(4):
            __find_length_n_words_core(n, board, y, x, [], "", words, correct_paths)
    return correct_paths

def __find_length_n_words_core(n, board, y, x , used_locations, word, words, correct_paths):
    if n > 32:
        return
    if len(word) >= n:
        if word in words:
            if used_locations not in correct_paths:
                correct_paths.append(used_locations)
        return
    for y_mod, x_mod in consts.DIRECTIONS:
        new_y, new_x = y + y_mod, x + x_mod
        if 0 <= new_x <= 3 and 0 <= new_y <= 3 and (new_y, new_x) not in used_locations: 
            __find_length_n_words_core(n, board, new_y, new_x, used_locations + [(new_y,new_x)], word + board[new_y][new_x], words, correct_paths)


def max_score_paths(board, words):
    words = __filter_words_for_max_score(board, words)
    max_word_length = 0 #initlazing
    for word in words:
        if len(word) > max_word_length:
            max_word_length = len(word)
    words = set(words)
    all_paths = []  # initalizing list we will return
    for y in range(4):
        for x in range(4):
            __max_score_paths_core(board, words, "", [], (y,x), all_paths, max_word_length)
    longest_paths = _find_correct_paths(all_paths,words)
    return longest_paths


def __max_score_paths_core(board, words, word, used_locations, cur_location, all_paths, max_word_length):
    used_locations.append(cur_location)
    if not __are_locations_legal(used_locations):
        return

    y, x = cur_location[0], cur_location[1]
    word += board[y][x]

    word_has_future = False
    for tested_word in words:
        if tested_word.startswith(word):
            word_has_future = True
            all_paths.append((word, used_locations))
            break
    if not word_has_future:
        return

    for direction in consts.DIRECTIONS:
        new_location = (y + direction[0], x + direction[1])
        __max_score_paths_core(board, words, word[:], used_locations[:],
                                  new_location, all_paths,max_word_length)




def _find_correct_paths(all_paths, words):
    corect_paths = {}
    for path_tuple in all_paths:
        word, path = path_tuple[0], path_tuple[1]
        if word in words:
            if word not in corect_paths:
                corect_paths[word] = path
            else:
                if len(path) > len(corect_paths[word]):
                    corect_paths[word] = path
    #now we will extract the paths:
    correct_paths_list = []
    for word in corect_paths:
        correct_paths_list.append(corect_paths[word])
    return correct_paths_list


if __name__ == "__main__":
    board = [["a","b","c","d"],["e","f","g","h"],["i","j","k","l"],["m","n","o","p"]]
    words = ["abc","def","ghlp","ab","efj","mno","abcd"]
    #print(is_valid_path([["a","b","c"],["d","e","f"],["g","h","i"]], [(0,0),(0,1),(0,2)], ["ccc"]))
   # print(find_length_n_words(3,board,words))
   # print(__are_locations_legal( [(0,0),(0,1),(0,0)])) #FALSE
    #print(__are_locations_legal([(0, 0), (0, 1), (0, 2)])) #TRUE
    #print(__are_locations_legal([(0, 0), (0, 1), (-1,1)]))  # FALSE
   # print(__are_locations_legal([(0, 0), (0, 2), (3,3)]))  # FALSE
    #print(__are_locations_legal([(0, 0), (0, 1), (1, 1),(2,2)]))  #TRUE
    board = [["QU", "E", "W", "L"],
            ["I", "E", "T", "R"],
            ["E", "N", "Z", "D"],
            ["A", "M", "L", "J"]]
    words = ["QUEEN","SITE","WIELD","KIT"]
    print(max_score_paths(board,words))