from tetriminos import Tetriminos

class Tetris:
    state = "start"
    field = []
    height = 0
    width = 0
    zoom = 20
    x = 100
    y = 60
    tetriminos = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.state = "start"
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def new_figure(self):
        self.tetriminos = Tetriminos(3, 0)

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.tetriminos.image():
                    if i + self.tetriminos.y > self.height - 1 or j + self.tetriminos.x > self.width - 1 or j + self.tetriminos.x < 0 or self.field[i + self.tetriminos.y][j + self.tetriminos.x] > 0:
                        intersection = True
        return intersection

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zero = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zero += 1
            if zero == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]

    def go_bottom(self):
        while not self.intersects():
            self.tetriminos.y += 1
        self.tetriminos.y -= 1
        self.freeze()

    def go_down(self):
        self.tetriminos.y += 1
        if self.intersects():
            self.tetriminos.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.tetriminos.image():
                    self.field[i + self.tetriminos.y][j + self.tetriminos.x] = self.tetriminos.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state = "gameover"

    def go_side(self, dx):
        old_x = self.tetriminos.x
        self.tetriminos.x += dx
        if self.intersects():
            self.tetriminos.x = old_x

    def rotate(self):
        old_rotation = self.tetriminos.rotation
        self.tetriminos.rotate()
        if self.intersects():
            self.tetriminos.rotation = old_rotation