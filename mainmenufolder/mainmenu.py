#setup
import tkinter
import PyQt5
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QMenuBar, QStatusBar,QDialogButtonBox, QDialog, QApplication, QMainWindow, QPushButton, QToolTip, QMessageBox, QLabel, QVBoxLayout, QWidget)
import site
site.getsitepackages()


import pygame, sys, random
from pygame.locals import *
from tkinter import *
import os
os.chdir('mainmenufolder')

from random import randint





pygame.init()
x = 1000
y = 600
window = pygame.display.set_mode((x,y))


#background setup
#backg = pygame.image.load('MenuAssets/gradient(3).png')
#backg = pygame.transform.scale(backg, (x, y))



#font setup
fontobj = pygame.font.SysFont('impact', 32)
fontobj2 = pygame.font.SysFont('impact', 25)

#button1 (New Game) setup
button1 = pygame.image.load('MenuAssets/buttongradient.png')
button1flip = pygame.image.load('MenuAssets/buttongradient.png')
button1flip = pygame.transform.flip(button1flip, True, False)
rect1 = button1.get_rect()
rect1 = rect1.move((x/4, y-550))
rect1flip = button1flip.get_rect()
rect1flip = rect1flip.move((x/4, y-550))
newgame = fontobj.render('New Game', True, (0,0,0), None)

#character selection button
button2 = pygame.image.load('MenuAssets/buttongradient.png')
button2flip = pygame.image.load('MenuAssets/buttongradient.png')
button2flip = pygame.transform.flip(button2flip, True, False)
rect2 = button2.get_rect()
rect2 = rect2.move((x/4, y-430))
rect2flip = button2flip.get_rect()
rect2flip = rect2flip.move((x/4, y-430))
charselect = fontobj.render('Select Character', True, (0,0,0), None)

#level selection button
button3 = pygame.image.load('MenuAssets/buttongradient.png')
button3flip = pygame.image.load('MenuAssets/buttongradient.png')
button3flip = pygame.transform.flip(button3flip, True, False)
rect3 = button3.get_rect()
rect3 = rect3.move((x/4, y-310))
rect3flip = button3flip.get_rect()
rect3flip = rect3flip.move((x/4, y-310))
lvlselect = fontobj.render('Select Level', True, (0,0,0), None)

#load game button
button4 = pygame.image.load('MenuAssets/buttongradient.png')
button4flip = pygame.image.load('MenuAssets/buttongradient.png')
button4flip = pygame.transform.flip(button4flip, True, False)
rect4 = button4.get_rect()
rect4 = rect4.move((x/4, y-190))
rect4flip = button4flip.get_rect()
rect4flip = rect4flip.move((x/4, y-190))
loadgame = fontobj.render('Load Game', True, (0,0,0), None)

#settings
button5 = pygame.image.load('cog.png')
button5flip = pygame.image.load('coginvert.png')
button5flip= pygame.transform.scale(button5flip, (80,80))
button5= pygame.transform.scale(button5, (80,80))
#button5flip = pygame.transform.flip(button4flip, True, False)
rect5 = button5.get_rect()
rect5 = rect5.move((x-100, y-100))
rect5flip = button5flip.get_rect()
rect5flip = rect5flip.move((x-100, y-100))

#credits
button6 = pygame.image.load('MenuAssets/buttongradient.png')
button6flip = pygame.image.load('MenuAssets/buttongradient.png')
button6flip = pygame.transform.flip(button6flip, True, False)
button6flip = pygame.transform.scale(button6flip, (200,60))
button6 = pygame.transform.scale(button6, (200,60))
rect6 = button6.get_rect()
rect6 = rect6.move((x-590, y-80))
rect6flip = button6flip.get_rect()
rect6flip = rect6flip.move((x-590, y-80))
creditsshow = fontobj.render('Credits', True, (0,0,0), None)


        


while True:
    #window.blit(backg, (0,0))
    window.blit(button1, rect1)
    window.blit(button1flip, rect1)
    window.blit(newgame, (x-550, y-520))
    window.blit(button2, rect2)
    window.blit(button2flip, rect2)
    window.blit(charselect, (x-600, y-400))
    window.blit(button3, rect3)
    window.blit(button3flip, rect3)
    window.blit(lvlselect, (x-570, y-280))
    window.blit(button4, rect4)
    window.blit(button4flip, rect4)
    window.blit(loadgame, (x-560, y-160))
    window.blit(button5, rect5)
    window.blit(button5flip, rect5)
    window.blit(button6, rect6)
    window.blit(button6flip, rect6)
    window.blit(creditsshow, (x-540, y-70))
    #get mouse position in separate x and y values
    mouseX, mouseY = pygame.mouse.get_pos()

    #keep window running until exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #change appearance of button1 if mouse is hovering over it
    #specifically this code senses whether the mouse cursor is hovering over the button
    #and changes which version of button1 is showing (using transparency, or alpha values)
    if(250 <= mouseX <= 750 and 50 <= mouseY <= 150):
        button1flip.set_alpha(255)
        button1.set_alpha(0)
    else:
        button1.set_alpha(255)
        button1flip.set_alpha(0)
    if(250 <= mouseX <= 750 and 170 <= mouseY <= 270):
        button2flip.set_alpha(255)
        button2.set_alpha(0)
    else:
        button2.set_alpha(255)
        button2flip.set_alpha(0)
    if(250 <= mouseX <= 750 and 290 <= mouseY <= 390):
        button3flip.set_alpha(255)
        button3.set_alpha(0)
    else:
        button3.set_alpha(255)
        button3flip.set_alpha(0)
    if(250 <= mouseX <= 750 and 410 <= mouseY <= 510):
        button4flip.set_alpha(255)
        button4.set_alpha(0)
    else:
        button4.set_alpha(255)
        button4flip.set_alpha(0)
    if(900 <= mouseX <= 980 and 500 <= mouseY <= 580):
        button5flip.set_alpha(255)
        button5.set_alpha(0)
    else:
        button5.set_alpha(255)
        button5flip.set_alpha(0)
    if(400 <= mouseX <= 610 and 520 <= mouseY <= 580):
        button6flip.set_alpha(255)
        button6.set_alpha(0)
    else:
        button6.set_alpha(255)
        button6flip.set_alpha(0)
    pygame.display.flip()


