import random

def spawn(matrix):
    x = random.randint(0,3)
    y = random.randint(0,3)
    while matrix[x][y] != -1:
        x = random.randint(0,3)
        y = random.randint(0,3)
    matrix[x][y] = 2
    return matrix

def init():
    matrix = []
    for x in range(4):
        n = []
        for y in range(4):
            n.append(-1)
        matrix.append(n)
    matrix = spawn(matrix)
    matrix = spawn(matrix)
    return matrix

def up(matrix,score):
    spawned = False
    for i in range(3):
        for x in range(3):
            for y in range(4):
                if matrix[1+x][y] != -1:
                    if matrix[x][y] == -1:
                        spawned = True
                        matrix[x][y] = matrix[1+x][y]
                        matrix[1+x][y] = -1
    for x in range(3):
        for y in range(4):
            if matrix[1+x][y] != -1:
                if matrix[1+x][y] == matrix[x][y]:
                    spawned = True
                    matrix[x][y] += matrix[1+x][y]
                    score += matrix[x][y]
                    matrix[1+x][y] = -1
                if matrix[x][y] == -1:
                    spawned = True
                    matrix[x][y] = matrix[1+x][y]
                    matrix[1+x][y] = -1
    if spawned == True:
        matrix = spawn(matrix)
    return matrix,score

def down(matrix,score):
    spawned = False
    for i in range(3):
        for x in range(3):
            for y in range(4):
                if matrix[2-x][y] != -1:
                    if matrix[3-x][y] == -1:
                        spawned = True
                        matrix[3-x][y] = matrix[2-x][y]
                        matrix[2-x][y] = -1
    for x in range(3):
        for y in range(4):
            if matrix[2-x][y] != -1:
                if matrix[2-x][y] == matrix[3-x][y]:
                    spawned = True
                    matrix[3-x][y] += matrix[2-x][y]
                    score += matrix[3-x][y]
                    matrix[2-x][y] = -1
                if matrix[3-x][y] == -1:
                    spawned = True
                    matrix[3-x][y] = matrix[2-x][y]
                    matrix[2-x][y] = -1
    if spawned == True:
        matrix = spawn(matrix)
    return matrix,score

def left(matrix,score):
    spawned = False
    for i in range(3):
        for x in range(4):
            for y in range(3):
                if matrix[x][1+y] != -1:
                    if matrix[x][y] == -1:
                        spawned = True
                        matrix[x][y] = matrix[x][1+y]
                        matrix[x][1+y] = -1
    for x in range(4):
        for y in range(3):
            if matrix[x][1+y] != -1:
                if matrix[x][1+y] == matrix[x][y]:
                    spawned = True
                    matrix[x][y] += matrix[x][1+y]
                    score += matrix[x][y]
                    matrix[x][1+y] = -1
                if matrix[x][y] == -1:
                    spawned = True
                    matrix[x][y] = matrix[x][1+y]
                    matrix[x][1+y] = -1
    if spawned == True:
        matrix = spawn(matrix)
    return matrix,score

def right(matrix,score):
    spawned = False
    for i in range(3):
        for x in range(4):
            for y in range(3):
                if matrix[x][2-y] != -1:
                    if matrix[x][3-y] == -1:
                        spawned = True
                        matrix[x][3-y] = matrix[x][2-y]
                        matrix[x][2-y] = -1
    for x in range(4):
        for y in range(3):
            if matrix[x][2-y] != -1:
                if matrix[x][2-y] == matrix[x][3-y]:
                    spawned = True
                    matrix[x][3-y] += matrix[x][2-y]
                    score += matrix[x][3-y]
                    matrix[x][2-y] = -1
                if matrix[x][3-y] == -1:
                    spawned = True
                    matrix[x][3-y] = matrix[x][2-y]
                    matrix[x][2-y] = -1
    if spawned == True:
        matrix = spawn(matrix)
    return matrix,score

def game_state(matrix):
    arr = [-1,-1,-1,-1]
    for x in range(4):
        for y in range(3):
            if matrix[x][y] == matrix[x][y+1]:
                arr[1] = 0
                arr[3] = 0
    for y in range(4):
        for x in range(3):
            if matrix[x][y] == matrix[x+1][y]:
                arr[0] = 0
                arr[2] = 0
    if matrix[0][0] == -1:
        arr[0] = 0
        arr[3] = 0
    if matrix[0][1] == -1:
        arr[0] = 0
        arr[1] = 0
        arr[3] = 0
    if matrix[0][2] == -1:
        arr[0] = 0
        arr[1] = 0
        arr[3] = 0
    if matrix[0][3] == -1:
        arr[0] = 0
        arr[1] = 0
    if matrix[1][0] == -1:
        arr[0] = 0
        arr[2] = 0
        arr[3] = 0
    if matrix[1][1] == -1:
        arr[0] = 0
        arr[1] = 0
        arr[2] = 0
        arr[3] = 0
    if matrix[1][2] == -1:
        arr[0] = 0
        arr[1] = 0
        arr[2] = 0
        arr[3] = 0
    if matrix[1][3] == -1:
        arr[0] = 0
        arr[1] = 0
        arr[2] = 0
    if matrix[2][0] == -1:
        arr[0] = 0
        arr[2] = 0
        arr[3] = 0
    if matrix[2][1] == -1:
        arr[0] = 0
        arr[1] = 0
        arr[2] = 0
        arr[3] = 0
    if matrix[2][2] == -1:
        arr[0] = 0
        arr[1] = 0
        arr[2] = 0
        arr[3] = 0
    if matrix[2][3] == -1:
        arr[0] = 0
        arr[1] = 0
        arr[2] = 0
    if matrix[3][0] == -1:
        arr[2] = 0
        arr[3] = 0
    if matrix[3][1] == -1:
        arr[1] = 0
        arr[2] = 0
        arr[3] = 0
    if matrix[3][2] == -1:
        arr[1] = 0
        arr[2] = 0
        arr[3] = 0
    if matrix[3][3] == -1:
        arr[1] = 0
        arr[2] = 0
    return arr

def do(matrix,score,direction):
    arr = game_state(matrix)
    done = False
    matr = matrix
    helpoMatrix = []
    if arr[direction] == 0:
        if direction == 0:
            for x in matr:
                n = []
                for y in x:
                    n.append(y)
                helpoMatrix.append(n)
            temp = up(matr,score)
            matr = temp[0]
            score = temp[1]
            if helpoMatrix != matr:
                done = True
        if direction == 1:
            for x in matr:
                n = []
                for y in x:
                    n.append(y)
                helpoMatrix.append(n)
            temp = right(matr,score)
            matr = temp[0]
            score = temp[1]
            if helpoMatrix != matr:
                done = True
        if direction == 2:
            for x in matr:
                n = []
                for y in x:
                    n.append(y)
                helpoMatrix.append(n)
            temp = down(matr,score)
            matr = temp[0]
            score = temp[1]
            if helpoMatrix != matr:
                done = True
        if direction == 3:
            for x in matr:
                n = []
                for y in x:
                    n.append(y)
                helpoMatrix.append(n)
            temp = left(matr,score)
            matr = temp[0]
            score = temp[1]
            if helpoMatrix != matr:
                done = True
    run = False
    for i in range(4):
        if game_state(matrix)[i] == 0:
            run = True
    return matr,score,done,run
