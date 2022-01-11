from typing import List, Set, Tuple
import consts

def is_near_previous(previous, current) -> bool:
    """
    checks if a given location is near another one
    :param previous: a tuple of y,x which is a location
    :param current: same
    :return: True if they are, False otherwise
    """
    cur_y, cur_x = current[0], current[1]
    prev_y, prev_x = previous[0], previous[1]
    return abs(prev_y - cur_y) in [0, 1] and abs(prev_x - cur_x) in [0, 1]

def __is_loc_valid(loc: Tuple[int]) -> bool:
    """
    checks if a given location is valid as for the Boggle rules
    :return: True if it is, False otherwise
    """
    y, x = loc[0], loc[1]
    if y > 3 or y < 0 or x > 3 or x < 0:
        return False
    return True

def is_valid_path(board, path, words):
    """
    checks if a given path is valid as for a given Boggle board and an available word list to look from
    :param board: a two dimensional list representing a Boggle board
    :param words: the words to look from
    :param path: the path to check
    :return: True if it is, False otherwise
    """
    path_word = ""
    used_locations = []
    for i, loc in enumerate(path):
        if not __is_loc_valid(loc):
            return None
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
    
def __are_locations_legal(locations: List[Tuple[int,int]]) -> bool:
    """
    checks if a list of tuples, which represents locations are valid and legal to a Boggle game board
    :param locations: the list of locations described
    :return: True if it is, False otherwise
    """
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

def find_length_n_paths(n: int, board: List[List[Tuple[int,int]]], words: List[str]) -> List[List[Tuple[int,int]]]:
    """
    gets all paths of length n to words in a Boggle game board
    :param n: length to the paths (how much squares)
    :param board: a 2 dimensional board which represnets the Boggle board
    :param words: the avilable words to look. only matches paths which represents words in the words set will be returned
    :return: a list of paths matches the creteria
    """
    if n == 0 or n > 16:
        return []
    paths = []
    words = set(words)
    for y in range(4):
        for x in range(4):
            __find_length_n_paths_core(x, y , "", n, board, words, [], paths)
    return paths

def __find_length_n_paths_core(x: int, y: int, curr_word: str, n: int, board: List[List[Tuple[int,int]]], words: Set[str], used_locations: List[Tuple[int,int]], paths: List[List[Tuple[int,int]]]) -> None:
    """
    core method to find_length_n_paths, a recursive method works with backtracing to find all possible paths matches creteria 
    :param x: x value for a given cell in the board
    :param y: y value same
    :param curr_word: the current word the path is building
    :param n: length to the paths (how much squares)
    :param board: a 2 dimensional board which represnets the Boggle board
    :param words: the avilable words to look. only matches paths which represents words in the words set will be returned
    :param used_locations: all the locations already present in the path
    :param paths: the return list
    :return: a list of paths matches the creteria
    """
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

def find_length_n_words(n: int, board: List[List[Tuple[int,int]]], words: List[str]) -> List[List[Tuple[int,int]]]:
    """
    gets all paths to words of length n in a Boggle game board
    :param n: length to the paths (how much squares)
    :param board: a 2 dimensional board which represnets the Boggle board
    :param words: the avilable words to look. only matches paths which represents words in the words set will be returned
    :return: a list of paths matches the creteria
    """
    if n == 0 or n > 16:
        return []
    words = set(words)
    correct_paths = [] #initalizing list we will return
    for y in range(4):
        for x in range(4):
            __find_length_n_words_core(n, board, y, x, [], "", words, correct_paths)
    return correct_paths

def __find_length_n_words_core(n: int, board: List[List[Tuple[int,int]]], y: int, x: int , used_locations: List[Tuple[int, int]], word: str, words: Set[str], correct_paths: List[List[Tuple[int,int]]]) -> None:
    """
    core method to find_length_n_words, a recursive method works with backtracing to find all possible paths matches creteria 
    :param x: x value for a given cell in the board
    :param y: y value same
    :param word: the current word the path is building
    :param n: length to the paths (how much squares)
    :param board: a 2 dimensional board which represnets the Boggle board
    :param words: the avilable words to look. only matches paths which represents words in the words set will be returned
    :param correct_paths: the return list
    :return: a list of paths matches the creteria
    """
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


def max_score_paths(board: List[List[Tuple[int,int]]], words: List[str]) -> List[List[Tuple[int,int]]]:
    """
    calculates the paths combination which results in the most score in a Boggle game.
    :param board: a 2 dimensional board which represnets the Boggle board
    :param words: the avilable words to look. only matches paths which represents words in the words set will be returned
    """
    max_word_length = 0 #initlazing
    words = set(words)
    for word in words:
        if len(word) > max_word_length:
            max_word_length = len(word)
    all_paths = []  # initalizing list we will return
    for y in range(4):
        for x in range(4):
            __max_score_paths_core(board, words, "", [], (y,x), all_paths, max_word_length)
    longest_paths = _find_correct_paths(all_paths,words)
    return longest_paths

def __max_score_paths_core(board: List[List[Tuple[int,int]]], words: Set[str], word: str, used_locations: List[Tuple[int,int]], cur_location: Tuple[int,int], all_paths:  List[List[Tuple[int,int]]], max_word_length: int) -> None:
    """
    core method to max_score_paths, a recursive method works with backtracing to find all possible paths matches creteria 
    :param word: the current word the path is building
    :param board: a 2 dimensional board which represnets the Boggle board
    :param words: the avilable words to look. only matches paths which represents words in the words set will be returned
    :param all_paths: the return list
    :param used_locations: all the locations already present in the path
    :param cur_location: the current location processing
    :return: a list of paths matches the creteria
    """
    y, x = cur_location[0], cur_location[1]
    word += board[y][x]
    
    used_locations.append(cur_location)
    
    if word in words:
        all_paths.append((word, used_locations))
    
    if len(word) + 1 > max_word_length:
        return

    for y_mod, x_mod in consts.DIRECTIONS:
        new_y, new_x = y + y_mod, x + x_mod
        new_location = (new_y, new_x)
        if 0 <= new_x <= 3 and 0 <= new_y <= 3 and (new_y, new_x) not in used_locations: 
            __max_score_paths_core(board, words, word, used_locations[:], new_location, all_paths, max_word_length)

def _find_correct_paths(all_paths: List[Tuple[str, List[Tuple[int, int]]]], words: Set[str]) -> List[List[Tuple[int,int]]]:
    """
    filters all the paths to ensure that the longest path for each word is returned
    :param all_paths: all the paths matching the creteria, that was found by __max_score_paths_core
    :param words: the set of the words to search from
    :return: the list of the paths that results in a perfect boggle game, with maximum score.
    """
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
