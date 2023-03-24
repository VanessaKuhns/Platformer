#setup
import tkinter
import pygame, sys, random
from pygame.locals import *
from tkinter import *
pygame.init()
x = 1000
y = 600
window = pygame.display.set_mode((x,y))


#background setup
backg = pygame.image.load('gradient.png')
backg = pygame.transform.scale(backg, (x, y))
# Sorry if the x and y values get confusing :(
# I tend to adjust them in really weird ways

#button1 (level selection) setup
button1 = pygame.image.load('buttongradient.png')
button1flip = pygame.image.load('buttongradient.png')
button1flip = pygame.transform.flip(button1flip, True, False)
rect1 = button1.get_rect()
rect1 = rect1.move((x/4, y-450))
rect1flip = button1flip.get_rect()
rect1flip = rect1flip.move((x/4, y-450))
fontobj = pygame.font.SysFont('impact', 32)
lvlselect = fontobj.render('Select Level', True, (0,0,0), None)


while True:

    window.blit(backg, (0,0))
    window.blit(button1, rect1)
    window.blit(button1flip, rect1)
    window.blit(lvlselect, (x/2-70, y/2-120))

    #get mouse position in separate x and y values
    mouseX, mouseY = pygame.mouse.get_pos()

    #keep window running until exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #change appearance of button1 if mouse is hovering over it
    #specifically this code senses whether the mouse cursor is hovering over the button
    #and changes which version of button1 is showing (using transparency, or alpha values)
    if(250 <= mouseX <= 750 and 150 <= mouseY <= 250):
        button1flip.set_alpha(255)
        button1.set_alpha(0)
    else:
        button1.set_alpha(255)
        button1flip.set_alpha(0)
    pygame.display.flip()


