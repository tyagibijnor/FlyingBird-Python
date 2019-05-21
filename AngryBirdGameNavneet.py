import pygame
import time
import random
from random import randint,randrange

black = (0,0,0)
white = (255,255,255)

greenyellow = (184,255,0)
brightblue = (47,228,253)
orange = (255,113,0)

blockColorChoice = [greenyellow,brightblue,orange]

sunset = (253,72,47)

from pygame import mixer
mixer.init()

pygame.init()

surfaceWidth = 800
surfaceHeight = 500

surface = pygame.display.set_mode((surfaceWidth,surfaceHeight))
pygame.display.set_caption('Navneet')
clock = pygame.time.Clock()

img = pygame.image.load('angry-bird-icon.png')

imageHeight = 50
imageWidth = 40

def score(count):
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("Score: "+str(count),True,white)
    surface.blit(text,[0,0])
    
def crashmsg(text):
    smallText = pygame.font.Font('freesansbold.ttf',15)
    largeText = pygame.font.Font('freesansbold.ttf',80)
    
    titleTextSurf, titleTextRect = makeTextObjs(text,largeText)
    titleTextRect.center = surfaceHeight / 2,((surfaceWidth / 4)+50)
    surface.blit(titleTextSurf, titleTextRect)
    
    typTextSurf, typTextRect = makeTextObjs('Press any key to continue',smallText)
    typTextRect.center = (surfaceHeight / 2), ((surfaceWidth / 2)+80)
    surface.blit(typTextSurf, typTextRect)

    pygame.display.update()
    time.sleep(3)

    while replay_or_quit() == None:
        clock.tick()

    main()
    
def blocks(x_block, y_block, block_w, block_h,gap, blockColor):
    pygame.draw.rect(surface, blockColor, [x_block,y_block,block_w,block_h])
    pygame.draw.rect(surface, blockColor, [x_block,y_block+block_h+gap,block_w,surfaceHeight])
    mixer.music.load("song.mp3")
    mixer.music.play()

    

def gameOver():
    crashmsg('Game over!!')

def angrybird(x,y,image):
    surface.blit(img,(x,y))

def makeTextObjs(text, font):
    textSurface = font.render(text, True, sunset)
    return textSurface, textSurface.get_rect()

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN,pygame.KEYUP,pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        elif event.type == pygame.KEYDOWN:
            continue

        return event.key

    return None
            
def main():
    
    game_over = False
    x = 100
    y = 150
    y_move = 0
    x_block = surfaceWidth
    y_block = 0
    
    block_w = randint(10, 80)
    upSpeed = 60
    
    
    block_h = randint(0,(surfaceHeight / 2))

    
    gap = imageHeight * 3
    block_move = 4
    current_score = 0
    z = x_block - block_move
    blockColor = blockColorChoice[randrange(0,len(blockColorChoice))]
     
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5

                    
        y += y_move
        
              
        surface.fill(black)
        angrybird(x,y,img)
        
        
        blocks(x_block,y_block,block_w,block_h,gap,blockColor)
        score(current_score)
        x_block -= block_move
        
        if y > surfaceHeight-40 or y <0:
            gameOver()

        if x_block < (-1 * block_w):
            x_block = surfaceWidth
            block_h = randint(0,(surfaceHeight / 2))
            blockColor = blockColorChoice[randrange(0,len(blockColorChoice))]
            block_w = randint(20, 80)
            current_score += 1

        if x + imageWidth > x_block:
            if x < x_block + block_w:
                if y < block_h:
                    if x - imageWidth < block_w + x_block:
                        gameOver()

        if x + imageWidth > x_block:
            if y + imageHeight > block_h + gap:
                if x < block_w + x_block:
                    gameOver()

        ##if x_block < (x - block_w) < x_block + block_move + block_move-1:
          ##  current_score += 1

        if 3 <= current_score < 5:
            block_move = 5
            gap = imageHeight * 2.9

        if 5 <= current_score < 8:
            block_move = 6
            gap = imageHeight * 2.8

        if 8 <= current_score < 14:
            block_move = 7
            gap = imageHeight * 2.7

        pygame.display.update()
        clock.tick(upSpeed)

main()
pygame.quit()
quit()
