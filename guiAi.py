import pygame
import os
import nn
import game
import math
import numpy as np
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,30"


pygame.init()
display = pygame.display.set_mode((1920,1020))

population = []
for i in range(12):
    population.append(nn.NeuralNetwork())
scores = []

def index(arr,num):
        for ind in range(len(arr)):
            if arr[ind] == sorted(arr, reverse = True)[num]:
                return ind

matr = []
for i in range(12):
    matr.append(game.init())
scores_game = []
for i in range(12):
    scores_game.append(0)
biggest = 0
last_biggest = 0
counter = -1
totalscore = 0
totalcounter = 0
av_score = 0
curr_work_matr = 0
last_work = 0
def train():
    scores = []
    num = 0
    global biggest
    global last_biggest
    global totalscore
    global totalcounter
    global counter
    global av_score
    for gene in population:
        scores.append(gene.learn())
    for x in scores:
        if x > biggest:
            biggest = x
    if last_biggest+10 < biggest:
        for gene in population:
            gene.adjust_weights(population[index(scores,0)].give_weights())
            gene.mutate()
        last_biggest = biggest
    for x in scores:
        num += x
    totalscore += num
    totalcounter += 1
    if num > biggest:
        counter += 1
        biggest = num
    av_score = (int)(totalscore/totalcounter/12)

def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text,position,size,color=(255,255,255)):
    largeText = pygame.font.Font('Roboto-Black.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText,color)
    TextRect.center = position
    display.blit(TextSurf, TextRect)

def number_display(number,position,color=(255,255,255)):
    text = str(number)
    largeText = pygame.font.Font('Roboto-Black.ttf',30-((int)(math.log(number,2))*2))
    TextSurf, TextRect = text_objects(text, largeText,color)
    TextRect.center = position
    display.blit(TextSurf, TextRect)

def message_score(number,position):
    text = str(number)
    largeText = pygame.font.Font('Roboto-Black.ttf',40)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = position
    display.blit(TextSurf, TextRect)

def printScore(score):
    message_score(score)

def draw_game():
    for y in range(3):
        for s in range(4):
            for i in range(1,5):
                for x in range(1,5):
                    pygame.draw.rect(display, (255,254,239), (870+s*250+x*50,220+y*250+i*50,49,49))
    pygame.draw.rect(display, (234, 225, 208), (210,240,500,60))
    message_display(str(av_score),(460,270),50,(94,79,115))
    pygame.draw.rect(display, (234, 225, 208), (310,540,300,60))
    message_display(str(totalcounter),(460,570),50,(94,79,115))
    num1 = 0
    for i in matr:
        num2 = 0
        for x in i:
            for y in x:
                if y != -1:
                    pygame.draw.rect(display, (200-((int)(math.log(y,2)))*10,230-((int)(math.log(y,2)))*10,240-((int)(math.log(y,2)))*10), (920+(num1%4)*250+num2%4*50,270+((int)(num1/4))*250+((int)(num2/4))*50,49,49))
                    number_display(y,(945+(num1%4)*250+num2%4*50,295+((int)(num1/4))*250+((int)(num2/4))*50))
                num2 += 1
        num1 += 1
    num1 = 0
    for i in scores_game:
        pygame.draw.rect(display, (234, 225, 208), (920+((int)(num1%4))*250,470+((int)(num1/4))*250,200,50))
        message_display(str(i),(1020+((int)(num1%4))*250,495+((int)(num1/4))*250),30)
        num1 += 1

def work_matr(i,last):
    temp = game.do(matr[i],scores_game[i],population[i].work(matr[i],last))
    matr[i] = temp[0]
    scores_game[i] = temp[1]
    if temp[2] == False:
        last += 1
    else:
        last = 0
    if temp[3] == False:
        i += 1
    return i,last



draw_game()
pygame.display.set_caption('2048AI')
clock = pygame.time.Clock()
run = True
learn = False
work = False


display.fill((234, 225, 208))
pygame.draw.rect(display, (255,254,239), (920,120,100,60))
pygame.draw.polygon(display, (94,79,115), [[960, 130], [960, 170], [980, 150]])
pygame.draw.rect(display, (255,254,239), (1070,120,100,60))
message_display('Reset',(1120,150),30,(94,79,115))
pygame.draw.rect(display, (255,254,239), (1220,120,100,60))
pygame.draw.polygon(display, (94,79,115), [[1260, 130], [1260, 170], [1280, 150]])
pygame.draw.rect(display, (255,254,239), (1370,120,100,60))
message_display('Reset',(1420,150),30,(94,79,115))
pygame.draw.rect(display, (255,254,239), (1520,120,100,60))
message_display('Save Weights',(1570,150),15,(94,79,115))
message_display('Average Score:',(460,200),60)
message_display('Generation:',(460,500),60)

while run:
    if learn == True:
        train()
    if work == True:
        if curr_work_matr < 12 and last_work < 4:
            temp = work_matr(curr_work_matr,last_work)
            curr_work_matr = temp[0]
            last_work = temp[1]
        else:
            matr = []
            for i in range(12):
                matr.append(game.init())
            scores_game = []
            for i in range(12):
                scores_game.append(0)
            curr_work_matr = 0
            last_work = 0
            work = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0] == 1:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            if 920 < x < 1020 and 120 < y < 180:
                work = False
                if learn == False:
                    learn = True
                else:
                    learn = False
            if 1070 < x < 1170 and 120 < y < 180:
                work = False
                learn = False
                population = []
                for i in range(12):
                    population.append(nn.NeuralNetwork())
                scores = []
                biggest = 0
                counter = -1
                totalscore = 0
                totalcounter = 0
                av_score = 0
            if 1220 < x < 1320 and 120 < y < 180:
                learn = False
                if work == False:
                    work = True
                else:
                    work = False
            if 1370 < x < 1470 and 120 < y < 180:
                learn = False
                work = False
                matr = []
                for i in range(12):
                    matr.append(game.init())
                scores_game = []
                for i in range(12):
                    scores_game.append(0)
                curr_work_matr = 0
                last_work = 0
    draw_game()
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
