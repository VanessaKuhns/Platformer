import tkinter
import pygame, sys, random
from pygame.locals import *
pygame.init()
from tkinter import *
from spritesheet import Spritesheet
import os
#os.chdir('testcode')

pygame.init()
x = 1000
y = 600
px = 500
py = 475
canvas = pygame.Surface((x, y))
win = pygame.display.set_mode((x,y))
mousepos = pygame.mouse.get_pos()
left=False
right=False
fjump=False
rjump=False
ljump=False
jump=False
jumpCount=0
airtime=10
steps=0
vel=5
my_spritesheet = Spritesheet('charsheet(1).png')

frontidle = pygame.transform.scale(my_spritesheet.get_sprite(18,140,28,50), (70,125))
#ffjump4 = pygame.transform.scale(my_spritesheet.get_sprite(330,140,44,50)
walkLeft = [pygame.transform.scale(my_spritesheet.get_sprite(21,77,22,49),(56,125)),
            pygame.transform.scale(my_spritesheet.get_sprite(85, 590, 22, 48),(57,125)), pygame.transform.scale(my_spritesheet.get_sprite(149, 589, 22, 48),(57,125)),
            pygame.transform.scale(my_spritesheet.get_sprite(213, 589, 23, 48),(60,125)),pygame.transform.scale(my_spritesheet.get_sprite(277,589,25,49),(64,125)),
            pygame.transform.scale(my_spritesheet.get_sprite(340, 590,27,48),(70,125)),pygame.transform.scale(my_spritesheet.get_sprite(405,589,25,49),(64,125)),
            pygame.transform.scale(my_spritesheet.get_sprite(469,589,23,49),(59,125)),pygame.transform.scale(my_spritesheet.get_sprite(533,589,22,49),(56,125))]
walkRight= [pygame.transform.scale(my_spritesheet.get_sprite(21,205,22,49),(56,125)),
            pygame.transform.scale(my_spritesheet.get_sprite(85,718,22,48),(57,125)),pygame.transform.scale(my_spritesheet.get_sprite(149,717,22,48),(57,125)),
            pygame.transform.scale(my_spritesheet.get_sprite(212,717,23,48),(60,125)),pygame.transform.scale(my_spritesheet.get_sprite(274,717,25,49),(64,125)),
            pygame.transform.scale(my_spritesheet.get_sprite(337,718,27,48),(70,125)),pygame.transform.scale(my_spritesheet.get_sprite(402,717,25,49),(64,125)),
            pygame.transform.scale(my_spritesheet.get_sprite(468,717,23,49),(59,125)),pygame.transform.scale(my_spritesheet.get_sprite(533,717,22,49),(56,125))]
jumpsprite=pygame.transform.scale(my_spritesheet.get_sprite(208,140,32,50),(80,125))
slimeLeft=[pygame]
#leftJump=[pygame.transform.scale(my_spritesheet.get_sprite(),pygame.transform.scale(my_spritesheet.get_sprite(),pygame.transform.scale(my_spritesheet.get_sprite(),pygame.transform.scale(my_spritesheet.get_sprite()]
def redraw():
    global steps

    canvas.fill((255,255,255))
    win.blit(canvas, (0,0))

    if steps +1 >= 27:
        steps = 0
    if left:
        win.blit(walkLeft[steps//3], (px,py))
        steps += 1
    elif right:
        win.blit(walkRight[steps//3],(px,py))
        steps += 1
    elif fjump:
        win.blit(jumpsprite,(px-5,py))
    else:
        win.blit(frontidle,(px,py))
    pygame.display.update()


while True:
    pygame.time.delay(30)
    mouseX, mouseY = pygame.mouse.get_pos()
    #print("x:"+str(px)+" y:"+str(py))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and px>vel:
        px-=vel
        left=True
        right=False
    elif keys[pygame.K_RIGHT] and px<1000-25-vel:
        px+=vel
        left=False
        right=True
    else:
        left=False
        right=False
        steps=0
    if not(jump):
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            jump=True
            fjump=True
            left=False
            right=False
            steps=0
            jumpCount+=1
    else:
        if airtime >= -10:
            neg=1
            if airtime<0:
                neg=-1
            py-=(airtime**2) * 0.5*neg
            airtime-=1
        else:
            jump=False
            fjump=False
            airtime=10
    

    redraw()
