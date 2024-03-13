import sys
from argparse import ArgumentParser, FileType
from trie import Trie
from board import Board, Point
from collections import Counter
import colors

def get_args():
    parser = ArgumentParser("Pass a puzzle board to solve")
    parser.add_argument("--min", type=int, default=2, help="Minimum length of word to return")
    parser.add_argument("--check-word", help="Check if a given word is in the built trie")
    parser.add_argument("--debug", action="store_true", help="Show debug output")
    parser.add_argument("-s", "--suppress-output", action="store_true", help="Hide answer output")
    parser.add_argument("-n", "--neighbors", help="Combine with --debug to show neighbors for an input point")
    parser.add_argument("-p", "--puzzle_file", type=FileType('r'), help="File with the board to solve")
    args = parser.parse_args()
    return args

def build_trie(words):
    trie = Trie()
    for word in words:
        trie.add_word(word)
    return trie

def build_board(puzzle):
    board_list = []
    for line in puzzle.readlines():
        board_list.append(line.lower().strip().split(" "))
    board = Board(board_list)
    return board

def check_strand(path, board, trie, minlen):
    this_char, this_point = path[-1]
    this_str = "".join(c for (c, _) in path)
    node = trie.get_node(this_str)
    candidates = []
    if node is not None:
        if (node.is_word and len(this_str) >= minlen):
            candidates.append((this_str, path))
        for char, point in board.neighbor_charpoints(this_point):
            if point not in [p for (_, p) in path]:
                new_path = list(path)
                new_path.append((char,point))
                candidates.extend(check_strand(new_path, board, trie, minlen))
    return candidates

def solve(board, trie, minlen):
    all_strands = []
    for char, point in board.all_charpoints():
        path = [(char, point)]
        # print(f"{point.x},{point.y}: {char}")
        # print_board(board, [point], highlight_color=colors.red)
        # print("")
        all_strands.extend(check_strand(path, board, trie, minlen))
    return all_strands

def print_candidate(string, path, board):
    print(f"{string}:")
    print_board(board, [p for _,p in path], highlight_color=colors.cyan)

def print_board(
        board,
        highlights=[],
        show_index=False,
        highlight_color=colors.green,
        base_color=colors.dim,
        highlight_index=True,
        highlight_char=True):
    line = []
    lines = []
    for char, point in board.all_charpoints():
        char = char.upper()
        pointspec = f"{point.x},{point.y}: " if show_index else ""
        charspec = f"{base_color(char)}"
        if point in highlights:
            if show_index and highlight_index:
                pointspec = highlight_color(pointspec)
            if highlight_char:
                charspec = highlight_color(char)
        boardentryspec = f"{pointspec}{charspec}"
        line.append(boardentryspec)
        end_of_line = point.x == board.size_x-1
        if end_of_line:
            lines.append(" ".join(line))
            line = []
    print("\n".join(lines))
    print("")

def debug_output(board, neighbor_check=None):
    neighbors = None
    if neighbor_check is not None:
        x,y = list(map(int, neighbor_check.split(",")))
        target = Point(x,y)
        neighbors = [p for _,p in board.neighbor_charpoints(target)]
    print(f"Board size: x: {board.size_x}, {board.size_y}")
    print_board(board, neighbors, show_index=True, highlight_char=False)

def main():
    args = get_args()
    board = build_board(args.puzzle_file)
    if args.debug:
        debug_output(board, args.neighbors)
        return 0
    with open("/usr/share/dict/words") as words_file:
        words = [w.strip() for w in words_file.readlines()]
    trie = build_trie(words)
    if (args.check_word):
        node = trie.get_node(args.check_word)
        print(node.is_word)
        return 0
    candidates = solve(board, trie, args.min)
    wordcounts = Counter(string for string, path in candidates)
    filtered = [ (string, path) for string, path in candidates if wordcounts[string] == 1]
    if not args.suppress_output:
        for string, path in filtered:
            print_candidate(string, path, board)
    return 0

if __name__=="__main__":
    sys.exit(main())
