from tkinter import *
import pygame
from pygame import *
from pygame.locals import *
from level_2 import *
from level_3 import *
from level_4 import *
from level_5 import *
from PIL import Image, ImageTk


#level 1
def level_2(win, logo: PhotoImage):
    
    
    #toplevel
    ml1_wn = Toplevel(win)
    ml1_wn.title("Slush Rush Level 1")
    ml1_wn.geometry('1200x480')
    ml1_wn.resizable(False, False)
    ml1_wn.iconphoto(False, logo)

    
   


#level 2
def level_3(win, logo: PhotoImage):
    
    #toplevel
    ml1_wn = Toplevel(win,bg='LightBlue')
    ml1_wn.title("Slush Rush Level 2")
    ml1_wn.geometry('1200x480')
    ml1_wn.resizable(False, False)
    ml1_wn.iconphoto(False, logo)
    
    
    
    Lvl3_wn.mainloop()
    
#level 3  
def level_4(win, logo: PhotoImage):
    
    #toplevel
    ml1_wn = Toplevel(win,bg='LightBlue')
    ml1_wn.title("Slush Rush Level 4")
    ml1_wn.geometry('1200x480')
    ml1_wn.resizable(False, False)
    ml1_wn.iconphoto(False, logo)
    
    
    
    Lvl4_wn.mainloop()
    

#level 4
def level_5(win, logo: PhotoImage):
    
    #toplevel
    ml1_wn = Toplevel(win,bg='LightBlue')
    ml1_wn.title("Slush Rush Level 5")
    ml1_wn.geometry('1200x480')
    ml1_wn.resizable(False, False)
    ml1_wn.iconphoto(False, logo)
    
    
    
    Lvl4_wn.mainloop()
    
    
    





root = Tk()
root.title("Slush Rush")
root.geometry('1200x480')
root.config (bg="pink")
root.resizable(False, False)

#window icon
photo = ImageTk.PhotoImage(Image.open('icon.png'))
root.iconphoto(False, photo)






Label(root, font=("Comic Sans MS", 16), text= "SLUSH RUSH LEVEL SELECTION", bg='pink').place(x=425, y=0)

Lvl2_wn = Button(root, text='LEVEL 1', font=("Comic Sans MS", 16), command=lambda: level_2(root, photo), bg='white')
Lvl2_wn.place(x=250, y=190)

Lvl3_wn = Button(root, text='LEVEL 2', font=("Comic Sans MS", 16), command=lambda: level_3(root, photo), bg='white')
Lvl3_wn.place(x=450, y=190)

Lvl4_wn = Button(root, text='LEVEL 3', font=("Comic Sans MS", 16), command=lambda: level_4(root, photo), bg='white')
Lvl4_wn.place(x=650, y=190)


Lvl5_wn = Button(root, text='LEVEL 4', font=("Comic Sans MS", 16), command=lambda: level_5(root, photo), bg='white')
Lvl5_wn.place(x=850, y=190)








root.update()
root.mainloop()