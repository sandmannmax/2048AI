import random
from logic.direction import Direction
import math

class Game():
    def __init__(self):
        self.score = 0
        self.__matrix = [[0]*4 for _ in range(4)]
        self.__spawn()
        self.__spawn()

    def __get_spawned_number(self):
        possibility = random.randint(0,99)
        return 1 if possibility < 90 else 2

    def __spawn(self):
        x, y = random.randint(0,3), random.randint(0,3)
        while self.__matrix[x][y] != 0:
            x, y = random.randint(0,3), random.randint(0,3)
        self.__matrix[x][y] = self.__get_spawned_number()

    def __up(self) -> int:
        reward = 0
        spawn = False
        for i in range(3):
            for x in range(3):
                for y in range(4):
                    if self.__matrix[1+x][y] != 0 and self.__matrix[x][y] == 0:
                        spawn = True
                        self.__matrix[x][y] = self.__matrix[1+x][y]
                        self.__matrix[1+x][y] = 0
        for x in range(3):
            for y in range(4):
                if self.__matrix[1+x][y] != 0:
                    if self.__matrix[1+x][y] == self.__matrix[x][y]:
                        spawn = True
                        self.__matrix[x][y] += 1
                        self.score += 2**self.__matrix[x][y]
                        self.__matrix[1+x][y] = 0
                        reward += 1
                    if self.__matrix[x][y] == 0:
                        spawn = True
                        self.__matrix[x][y] = self.__matrix[1+x][y]
                        self.__matrix[1+x][y] = 0
        if spawn == True:
            self.__spawn()
        return reward
    
    def __turn_matrix(self):
        self.__matrix = [list(reversed(col)) for col in zip(*self.__matrix)]

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

    def __get_allowed_directions(self):
        allowed_directions = [False,False,False,False]
        for x in range(4):
            for y in range(3):
                if self.__matrix[x][y] == self.__matrix[x][y+1]:
                    allowed_directions[1] = True
                    allowed_directions[3] = True
        for y in range(4):
            for x in range(3):
                if self.__matrix[x][y] == self.__matrix[x+1][y]:
                    allowed_directions[0] = True
                    allowed_directions[2] = True
        if self.__matrix[0][0] == 0:
            allowed_directions[0] = True
            allowed_directions[3] = True
        if self.__matrix[0][1] == 0 or self.__matrix[0][2] == 0:
            allowed_directions[0] = True
            allowed_directions[1] = True
            allowed_directions[3] = True
        if self.__matrix[0][3] == 0:
            allowed_directions[0] = True
            allowed_directions[1] = True
        if self.__matrix[1][0] == 0 or self.__matrix[2][0] == 0:
            allowed_directions[0] = True
            allowed_directions[2] = True
            allowed_directions[3] = True
        if self.__matrix[1][1] == 0 or self.__matrix[1][2] == 0 or self.__matrix[2][1] == 0 or self.__matrix[2][2] == 0:
            allowed_directions[0] = True
            allowed_directions[1] = True
            allowed_directions[2] = True
            allowed_directions[3] = True
        if self.__matrix[1][3] == 0 or self.__matrix[2][3] == 0:
            allowed_directions[0] = True
            allowed_directions[1] = True
            allowed_directions[2] = True
        if self.__matrix[3][0] == 0:
            allowed_directions[2] = True
            allowed_directions[3] = True
        if self.__matrix[3][1] == 0 or self.__matrix[3][2] == 0:
            allowed_directions[1] = True
            allowed_directions[2] = True
            allowed_directions[3] = True
        if self.__matrix[3][3] == 0:
            allowed_directions[1] = True
            allowed_directions[2] = True
        return allowed_directions

    def step(self, direction: Direction):
        reward = 0
        allowed_directions = self.__get_allowed_directions()
        if allowed_directions[int(direction)] == True:
            if direction == Direction.UP:
                reward = self.__up()
            if direction == Direction.RIGHT:
                reward = self.__right()
            if direction == Direction.DOWN:
                reward = self.__down()
            if direction == Direction.LEFT:
                reward = self.__left()
        done = True
        allowed_directions = self.__get_allowed_directions()
        for i in range(4):
            if allowed_directions[i] == True:
                done = False
        return done, reward

    def get_state(self):
        return self.__matrix

    def get_state_gui(self):
        matrix_adj = [[0]*4 for _ in range(4)]
        for i, row in enumerate(self.__matrix):
            for j, el in enumerate(row):
                if el != 0:
                    matrix_adj[i][j] = 2**el
        return matrix_adj
