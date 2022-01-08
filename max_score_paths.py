from ex12_utils import __find_length_n_paths_core

def get_board_dict(board):
    size = len(board)
    bdict = {}
    for y in range(size):
        for x in range(size):
            try:
                bdict[board[y][x]].append((y, x))
            except KeyError:
                bdict[board[y][x]] = [(y, x)]

    return bdict

def find_length_n_paths_of_word(x,y,n, word, board):
    if n == 0 or n > 16:
        return []
    paths = []
    words = {word}
    __find_length_n_paths_core(x, y , "", n, board, words, [], paths)
    return paths

def calc_path(word, board_dict):
    path = []
    for c in word:
        try:
            path.append(board_dict[c])
        except KeyError:
            return None
    return 

def calc_score(path):
    return len(path)**2

def max_score_paths_naive(board, words):
    words_set = set(words)
    board_dict = get_board_dict(board)
    max_score_paths = []
    max_score_path_word = ""
    max_score = 0
    paths = []
    for word in words_set:
        path = calc_path(word, board_dict, [], paths)
        if path is not None:
            score = calc_score(path)
            if score > max_score:
                max_score = score
                max_score_path_word = word
                max_score_paths = [path]
            elif score == max_score and word != max_score_path_word:
                max_score_paths.append(path)
    return max_score_paths

