import numpy as np
import game
import math


class NeuralNetwork():
    global inputs
    inputs = []
    global w1
    w1 = 2*np.random.random((57,64)) - 1
    global w2
    w2 = 2*np.random.random((65,64)) - 1
    global w3
    w3 = 2*np.random.random((65,56)) - 1
    global w4
    w4 = 2*np.random.random((57,4)) - 1
    global outputs
    outputs = []

    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def index(self,arr,num):
        for ind in range(4):
            if arr[ind] == sorted(arr, reverse = True)[num]:
                return ind

    def learn(self):
        matrix = game.init()
        score = 0
        run = True
        while run:
            inputs = []
            outputs = []
            for i in matrix:
                if i[0] == i[1]:
                    inputs.append(1)
                else:
                    inputs.append(-1)
                if i[0] == i[2]:
                    inputs.append(1)
                else:
                    inputs.append(-1)
                if i[0] == i[3]:
                    inputs.append(1)
                else:
                    inputs.append(-1)
                if i[1] == i[2]:
                    inputs.append(1)
                else:
                    inputs.append(-1)
                if i[1] == i[3]:
                    inputs.append(1)
                else:
                    inputs.append(-1)
                if i[2] == i[3]:
                    inputs.append(1)
                else:
                    inputs.append(-1)
            for i in range(4):
                if matrix[0][i] == matrix[1][i]:
                    inputs.append(1)
                else:
                    inputs.append(-1)
                if matrix[0][i] == matrix[2][i]:
                    inputs.append(1)
                else:
                    inputs.append(-1)
                if matrix[0][i] == matrix[3][i]:
                    inputs.append(1)
                else:
                    inputs.append(-1)
                if matrix[1][i] == matrix[2][i]:
                    inputs.append(1)
                else:
                    inputs.append(-1)
                if matrix[1][i] == matrix[3][i]:
                    inputs.append(1)
                else:
                    inputs.append(-1)
                if matrix[2][i] == matrix[3][i]:
                    inputs.append(1)
                else:
                    inputs.append(-1)
            for i in matrix:
                sum1 = 0
                for x in i:
                    if x != -1:
                        sum1 += 1
                inputs.append(sum1)
            for i in range(4):
                sum1
                for x in range(4):
                    if matrix[x][i] != -1:
                        sum1 += 1
                inputs.append(sum1)
            inputs.append(1)
            h1 = NeuralNetwork.sigmoid(np.dot(inputs,w1))
            h1 = np.append(h1,1)
            h2 = NeuralNetwork.sigmoid(np.dot(h1,w2))
            h2 = np.append(h2,1)
            h3 = NeuralNetwork.sigmoid(np.dot(h2,w3))
            h3 = np.append(h3,1)
            outputs = NeuralNetwork.sigmoid(np.dot(h3,w4))
            for i in range(4):
                index = NeuralNetwork.index(self,outputs,i)
                temp = game.do(matrix,score,index)
                matrix = temp[0]
                score = temp[1]
                run = temp[3]
                if temp[2] == True:
                    break
        return score

    def work(self,matrix,last):
        inputs = []
        outputs = []
        for i in matrix:
            if i[0] == i[1]:
                inputs.append(1)
            else:
                inputs.append(-1)
            if i[0] == i[2]:
                inputs.append(1)
            else:
                inputs.append(-1)
            if i[0] == i[3]:
                inputs.append(1)
            else:
                inputs.append(-1)
            if i[1] == i[2]:
                inputs.append(1)
            else:
                inputs.append(-1)
            if i[1] == i[3]:
                inputs.append(1)
            else:
                inputs.append(-1)
            if i[2] == i[3]:
                inputs.append(1)
            else:
                inputs.append(-1)
        for i in range(4):
            if matrix[0][i] == matrix[1][i]:
                inputs.append(1)
            else:
                inputs.append(-1)
            if matrix[0][i] == matrix[2][i]:
                inputs.append(1)
            else:
                inputs.append(-1)
            if matrix[0][i] == matrix[3][i]:
                inputs.append(1)
            else:
                inputs.append(-1)
            if matrix[1][i] == matrix[2][i]:
                inputs.append(1)
            else:
                inputs.append(-1)
            if matrix[1][i] == matrix[3][i]:
                inputs.append(1)
            else:
                inputs.append(-1)
            if matrix[2][i] == matrix[3][i]:
                inputs.append(1)
            else:
                inputs.append(-1)
        for i in matrix:
            sum1 = 0
            for x in i:
                if x != -1:
                    sum1 += 1
            inputs.append(sum1)
        for i in range(4):
            sum1
            for x in range(4):
                if matrix[x][i] != -1:
                    sum1 += 1
            inputs.append(sum1)
        inputs.append(1)
        h1 = NeuralNetwork.sigmoid(np.dot(inputs,w1))
        h1 = np.append(h1,1)
        h2 = NeuralNetwork.sigmoid(np.dot(h1,w2))
        h2 = np.append(h2,1)
        h3 = NeuralNetwork.sigmoid(np.dot(h2,w3))
        h3 = np.append(h3,1)
        outputs = NeuralNetwork.sigmoid(np.dot(h3,w4))
        index = NeuralNetwork.index(self,outputs,last)
        return index

    def give_weights(self):
        return w1,w2,w3,w4

    def adjust_weights(self,weights):
        w1 = weights[0]
        w2 = weights[1]
        w3 = weights[2]
        w4 = weights[3]

    def mutate(self):
        for y in w1:
            for x in y:
                if np.random.random() < 0.02:
                    x += 1.5*(2*np.random.random()-1)
        for y in w2:
            for x in y:
                if np.random.random() < 0.02:
                    x += 1.5*(2*np.random.random()-1)
        for y in w3:
            for x in y:
                if np.random.random() < 0.02:
                    x += 1.5*(2*np.random.random()-1)
        for y in w4:
            for x in y:
                if np.random.random() < 0.02:
                    x += 1.5*(2*np.random.random()-1)
