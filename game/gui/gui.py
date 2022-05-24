from logic import Direction
import pygame
import logic.game as game
import math

#-------------------------------------------------------------------------------------------------------------------

pygame.init()
gameDisplay = pygame.display.set_mode((500,600))
gameDisplay.fill((234, 225, 208))
pygame.display.set_caption('2048')
clock = pygame.time.Clock()
for i in range(1,5):
    for x in range(1,5):
        pygame.draw.rect(gameDisplay, (255,254,239), (-50+x*100,50+i*100,99,99))
run = True
score = 0

#-------------------------------------------------------------------------------------------------------------------

def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def message_display(number,position):
    text = str(number)
    largeText = pygame.font.Font('./game/gui/assets/Roboto-Black.ttf',80-((int)(math.log(number,2))*4))
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = position
    gameDisplay.blit(TextSurf, TextRect)

def message_score(number):
    text = str(number)
    largeText = pygame.font.Font('./game/gui/assets/Roboto-Black.ttf',40)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (250,50)
    gameDisplay.blit(TextSurf, TextRect)

def printScore(score):
    message_score(score)

def draw(g: game.Game):
    gameDisplay.fill((234, 225, 208))
    for i in range(1,5):
        for x in range(1,5):
            pygame.draw.rect(gameDisplay, (255,254,239), (-50+x*100,50+i*100,99,99))
    count = -1
    for x in g.matrix:
        for i in x:
            count += 1
            if i != -1:
                pygame.draw.rect(gameDisplay, (200-((int)(math.log(i,2)))*10,230-((int)(math.log(i,2)))*10,240-((int)(math.log(i,2)))*10), (50+count%4*100,150+(int)(count/4)*100,99,99))
                message_display(i,(100+count%4*100,200+((int)((count/4)))*100))
    printScore(g.score)
#-------------------------------------------------------------------------------------------------------------------

g = game.Game()
draw(g)

mapping = {pygame.K_UP: Direction.UP, pygame.K_RIGHT: Direction.RIGHT, pygame.K_DOWN: Direction.DOWN, pygame.K_LEFT: Direction.LEFT}

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            done, run, _ = g.step(mapping[event.key])
        draw(g)
        pygame.display.update()
        clock.tick(30)

pygame.quit()
quit()
