class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

NORTH = Point(0, -1)
SOUTH = Point(0, 1)
EAST = Point(1, 0)
WEST = Point(-1, 0)
NORTHWEST = NORTH + WEST
NORTHEAST = NORTH + EAST
SOUTHWEST = SOUTH + WEST
SOUTHEAST = SOUTH + EAST
DIRECTIONS = [NORTH, SOUTH, EAST, WEST, NORTHWEST, NORTHEAST, SOUTHWEST, SOUTHEAST]

class Board():
    def __init__(self, board):
        self.size_x = len(board[0])
        self.size_y = len(board)
        self.board = board

    def all_charpoints(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                yield (self.board[y][x], Point(x, y))

    def valid_point(self, point):
        return (0 <= point.x < self.size_x) and (0 <= point.y < self.size_y)

    def neighbor_charpoints(self, point):
        points = [d+point for d in DIRECTIONS if self.valid_point(d+point)]
        return [(self.board[p.y][p.x], p) for p in points]