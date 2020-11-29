import nn
import numpy as np

population = []
for i in range(12):
    population.append(nn.NeuralNetwork())
scores = []

def index(arr,num):
        for ind in range(len(arr)):
            if arr[ind] == sorted(arr, reverse = True)[num]:
                return ind


biggest = 0
counter = -1
totalscore = 0
totalcounter = 1
while True:
    scores = []
    num = 0
    for gene in population:
        scores.append(gene.learn())
    for gene in population:
        gene.adjust_weights(population[index(scores,0)].give_weights())
        gene.mutate()
    for x in scores:
        num += x
    totalscore += num
    totalcounter += 1
    if num > biggest:
        counter += 1
        biggest = num
    print((int)(totalscore/totalcounter/30),totalcounter)
    
    

    
