import random
from logic.direction import Direction

class Game():
    def __init__(self):
        self.score = 0
        self.matrix = [[-1]*4 for _ in range(4)]
        self.__spawn()
        self.__spawn()

    def __spawn(self):
        x, y = random.randint(0,3), random.randint(0,3)
        while self.matrix[x][y] != -1:
            x, y = random.randint(0,3), random.randint(0,3)
        self.matrix[x][y] = 2

    def __up(self):
        spawn = False
        for i in range(3):
            for x in range(3):
                for y in range(4):
                    if self.matrix[1+x][y] != -1 and self.matrix[x][y] == -1:
                        spawn = True
                        self.matrix[x][y] = self.matrix[1+x][y]
                        self.matrix[1+x][y] = -1
        for x in range(3):
            for y in range(4):
                if self.matrix[1+x][y] != -1:
                    if self.matrix[1+x][y] == self.matrix[x][y]:
                        spawn = True
                        self.matrix[x][y] += self.matrix[1+x][y]
                        self.score += self.matrix[x][y]
                        self.matrix[1+x][y] = -1
                    if self.matrix[x][y] == -1:
                        spawn = True
                        self.matrix[x][y] = self.matrix[1+x][y]
                        self.matrix[1+x][y] = -1
        if spawn == True:
            self.__spawn()
    
    def __turn_matrix(self):
        self.matrix = [list(reversed(col)) for col in zip(*self.matrix)]

    def __down(self):
        self.__turn_matrix()
        self.__turn_matrix()
        self.__up()
        self.__turn_matrix()
        self.__turn_matrix()

    def __left(self):
        self.__turn_matrix()
        self.__up()
        self.__turn_matrix()
        self.__turn_matrix()
        self.__turn_matrix()

    def __right(self):
        self.__turn_matrix()
        self.__turn_matrix()
        self.__turn_matrix()
        self.__up()
        self.__turn_matrix()

    def __game_state(self):
        arr = [-1,-1,-1,-1]
        for x in range(4):
            for y in range(3):
                if self.matrix[x][y] == self.matrix[x][y+1]:
                    arr[1] = 0
                    arr[3] = 0
        for y in range(4):
            for x in range(3):
                if self.matrix[x][y] == self.matrix[x+1][y]:
                    arr[0] = 0
                    arr[2] = 0
        if self.matrix[0][0] == -1:
            arr[0] = 0
            arr[3] = 0
        if self.matrix[0][1] == -1 or self.matrix[0][2] == -1:
            arr[0] = 0
            arr[1] = 0
            arr[3] = 0
        if self.matrix[0][3] == -1:
            arr[0] = 0
            arr[1] = 0
        if self.matrix[1][0] == -1 or self.matrix[2][0] == -1:
            arr[0] = 0
            arr[2] = 0
            arr[3] = 0
        if self.matrix[1][1] == -1 or self.matrix[1][2] == -1 or self.matrix[2][1] == -1 or self.matrix[2][2] == -1:
            arr[0] = 0
            arr[1] = 0
            arr[2] = 0
            arr[3] = 0
        if self.matrix[1][3] == -1 or self.matrix[2][3] == -1:
            arr[0] = 0
            arr[1] = 0
            arr[2] = 0
        if self.matrix[3][0] == -1:
            arr[2] = 0
            arr[3] = 0
        if self.matrix[3][1] == -1 or self.matrix[3][2] == -1:
            arr[1] = 0
            arr[2] = 0
            arr[3] = 0
        if self.matrix[3][3] == -1:
            arr[1] = 0
            arr[2] = 0
        return arr

    def step(self, direction: Direction):
        reward = 0
        arr = self.__game_state()
        done = False
        if arr[int(direction)] == 0:
            if direction == Direction.UP:
                helpoMatrix = copy_matrix(self.matrix)
                self.__up()
                if helpoMatrix != self.matrix:
                    done = True
            if direction == Direction.RIGHT:
                helpoMatrix = copy_matrix(self.matrix)
                self.__right()
                if helpoMatrix != self.matrix:
                    done = True
            if direction == Direction.DOWN:
                helpoMatrix = copy_matrix(self.matrix)
                self.__down()
                if helpoMatrix != self.matrix:
                    done = True
            if direction == Direction.LEFT:
                helpoMatrix = copy_matrix(self.matrix)
                self.__left()
                if helpoMatrix != self.matrix:
                    done = True
        run = False
        for i in range(4):
            if self.__game_state()[i] == 0:
                run = True
        return done, run, reward

def copy_matrix(matr):
    new_matr = []
    for row in matr:
        copied_row = []
        for el in row:
            copied_row.append(el)
        new_matr.append(copied_row)
    return new_matr