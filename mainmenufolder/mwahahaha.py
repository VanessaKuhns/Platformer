
import sys
import PyQt5
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QFont, QImage, QPalette, QColor
from PyQt5.QtCore import QIODevice, QProcess, Qt, QSize
from PyQt5.QtWidgets import (QPlainTextEdit, QMenuBar, QStatusBar, QDialogButtonBox, QDialog, QApplication, QMainWindow, QPushButton, QToolTip, QMessageBox, QLabel, QVBoxLayout, QWidget)
import site
import urllib
site.getsitepackages()
import pygame, sys, random
from pygame.locals import *
from tkinter import *
import os
import signal


#character selection window
class CharDialog(QMainWindow):
    def __init__(self, parent=None):
        super(CharDialog, self).__init__(parent)
        self.setFixedSize(900, 300)
        
        self.char1button = QtWidgets.QPushButton('', self)
        self.char1button.setGeometry(0, 0, 300, 300)
        self.char1button.setStyleSheet("background-image: url(mainmenufolder/MenuAssets/char1.png)")
        self.char1button.clicked.connect(self.on_char1button_clicked)

        self.char2button = QtWidgets.QPushButton('', self)
        self.char2button.setGeometry(300, 0, 300, 300)
        self.char2button.setStyleSheet("background-image: url(mainmenufolder/MenuAssets/char2.png)")
        self.char2button.clicked.connect(self.on_char2button_clicked)

        self.char3button = QtWidgets.QPushButton('', self)
        self.char3button.setGeometry(600, 0, 300, 300)
        self.char3button.setStyleSheet("background-image: url(mainmenufolder/MenuAssets/char3.png)")
        self.char3button.clicked.connect(self.on_char3button_clicked)
    def on_char1button_clicked(self):
        global charChoice
        charChoice = 1
        print(charChoice)
    def on_char2button_clicked(self):
        global charChoice
        charChoice = 2
        print(charChoice)
    def on_char3button_clicked(self):
        global charChoice
        charChoice = 3
        print(charChoice)
     
class testwindow(QDialog):
    def __init__(self, parent=None):
        super(testwindow, self).__init__(parent)
        self.setFixedSize(1100,300)
        #display slime sprite
        self.slimecreditlabel = QtWidgets.QLabel("ha",self)
        font = QFont('impact', 15)
        self.slimecreditlabel.move(50,100)
        self.slimecreditlabel.setFont(font)
        print(charChoice)


#level selection window
class LevelWindow(QMainWindow):
    def __init__(self, parent=None):
        super(LevelWindow, self).__init__(parent)
        self.setFixedSize(800,1200)
        font = QFont('impact', 15)
        
        self.lvl1button = QtWidgets.QPushButton('Level One', self)
        self.lvl1button.setGeometry(0,0,800,200)
        self.lvl1button.setStyleSheet("background-image: url(mainmenufolder/levels/level_1.png)")
        self.lvl1button.setFont(font)

        self.lvl2button = QtWidgets.QPushButton('Level Two', self)
        self.lvl2button.setGeometry(0,200,800,200)
        self.lvl2button.setStyleSheet("background-image: url(mainmenufolder/levels/level_2.png)")
        palette = self.lvl2button.palette()
        palette.setColor(QPalette.ButtonText, QColor('white'))
        self.lvl2button.setPalette(palette)
        self.lvl2button.setFont(font)

        self.lvl3button = QtWidgets.QPushButton('Level Three', self)
        self.lvl3button.setGeometry(0,400,800,200)
        self.lvl3button.setStyleSheet("background-image: url(mainmenufolder/levels/level_3.png)")
        self.lvl3button.setFont(font)
        #palette = self.lvl3button.palette()
        palette.setColor(QPalette.ButtonText, QColor('blue'))
        self.lvl3button.setPalette(palette)

        self.lvl4button = QtWidgets.QPushButton('Level Four', self)
        self.lvl4button.setGeometry(0,600,800,200)
        self.lvl4button.setStyleSheet("background-image: url(mainmenufolder/levels/level_4.png)")
        self.lvl4button.setFont(font)
        #palette = self.lvl4button.palette()
        palette.setColor(QPalette.ButtonText, QColor('red'))
        self.lvl4button.setPalette(palette)

        self.lvl5button = QtWidgets.QPushButton('Level Five', self)
        self.lvl5button.setGeometry(0,800,800,200)
        self.lvl5button.setStyleSheet("background-image: url(mainmenufolder/levels/level_5.png)")
        self.lvl5button.setFont(font)
        #palette = self.lvl5button.palette()
        palette.setColor(QPalette.ButtonText, QColor('light green'))
        self.lvl5button.setPalette(palette)

        self.lvl6button = QtWidgets.QPushButton('Level Six', self)
        self.lvl6button.setGeometry(0,1000,800,200)
        self.lvl6button.setStyleSheet("background-image: url(mainmenufolder/levels/level_6.png)")
        self.lvl6button.setFont(font)
        #palette = self.lvl6button.palette()
        palette.setColor(QPalette.ButtonText, QColor('gold'))
        self.lvl6button.setPalette(palette)

#Slime spritesheet credits window
class SlimeCreditsWindow(QDialog):
    def __init__(self, parent=None):
        super(SlimeCreditsWindow, self).__init__(parent)
        self.setFixedSize(1100,300)
        #display slime sprite
        self.slimecreditlabel = QtWidgets.QLabel('Slime sprites by SevenWave7 on itch.io',self)
        font = QFont('impact', 15)
        self.slimecreditlabel.move(50,100)
        self.slimecreditlabel.setFont(font)

#Character 1 spritesheet credits
class Char1CreditsWindow(QDialog):
    def __init__(self, parent=None):
        super(Char1CreditsWindow, self).__init__(parent)
        self.setFixedSize(3000,1600)
        self.char1creditlabel = QtWidgets.QLabel('Authors: bluecarrot16, Evert, TheraHedwig, Benjamin K. Smith (BenCreating), MuffinElZangano, Durrani, Pierre Vigier (pvigier), Eliza Wyatt (ElizaWy), Matthew Krohn (makrohn),\nJohannes Sj?lund (wulax), Stephen Challener (Redshrike), Manuel Riecke (MrBeast), ElizaWy\n\n- body/bodies/teen/universal/olive.png: \nby bluecarrot16, Evert, TheraHedwig, Benjamin K. Smith (BenCreating), MuffinElZangano, Durrani, Pierre Vigier (pvigier), Eliza Wyatt (ElizaWy), Matthew Krohn (makrohn),\n Johannes Sj?lund (wulax), Stephen Challener (Redshrike). License(s): CC-BY-SA 3.0, GPL 3.0. \n\t- https://opengameart.org/content/liberated-pixel-cup-lpc-base-assets-sprites-map-tiles\n\t- https://opengameart.org/content/lpc-medieval-fantasy-character-sprites\n\t- https://opengameart.org/content/lpc-ladies\n\t- https://opengameart.org/content/lpc-teen-unisex-base-clothes\n\t- https://opengameart.org/content/lpc-jump-expanded\n\n- head/heads/human_female/universal/olive.png: by bluecarrot16, Benjamin K. Smith (BenCreating), Stephen Challener (Redshrike). License(s): OGA-BY 3.0, CC-BY-SA 3.0, GPL 3.0. \n\t- https://opengameart.org/content/\n\t- https://opengameart.org/content/lpc-character-bases\n\n- hair/bedhead/male/black.png: by Manuel Riecke (MrBeast). License(s): CC-BY-SA 3.0, GPL 3.0. \n\t- https://opengameart.org/content/liberated-pixel-cup-lpc-base-assets-sprites-map-tiles\n\n- torso/clothes/longsleeve/teen/charcoal.png: by bluecarrot16, ElizaWy, Stephen Challener (Redshrike). License(s): OGA-BY 3.0, GPL 3.0. \n\t- https://opengameart.org/content/liberated-pixel-cup-lpc-base-assets-sprites-map-tiles\n\t- https://opengameart.org/content/lpc-teen-unisex-base-clothes\n\t- http://opengameart.org/content/lpc-clothing-updates\n\n- legs/pants/teen/blue.png: by bluecarrot16, ElizaWy, Stephen Challener (Redshrike). License(s): OGA-BY 3.0, GPL 3.0. \n\t- https://opengameart.org/content/liberated-pixel-cup-lpc-base-assets-sprites-map-tiles\n\t- https://opengameart.org/content/lpc-teen-unisex-base-clothes\n\t- http://opengameart.org/content/lpc-clothing-updates', self)
        font = QFont('impact', 10)
        self.char1creditlabel.move(50,100)
        self.char1creditlabel.setFont(font)
        self.char1creditlabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
        
#Credit Selection
class CreditsWindow(QMainWindow):
    def __init__(self, parent=None):
        super(CreditsWindow, self).__init__(parent)
        self.setFixedSize(1500,1000)
        self.slimespritebutton = QtWidgets.QPushButton('Slime Sprite Credits', self)
        self.slimespritebutton.setGeometry(0, 0, 300, 300)
        self.slimespritebutton.clicked.connect(self.on_slimespritebutton_clicked)
        self.char1credits = QtWidgets.QPushButton('Character 1 Spritesheet Credits', self)
        self.char1credits.setGeometry(300, 0, 500, 300)
        self.char1credits.clicked.connect(self.on_char1creditsbutton_clicked)
    def on_slimespritebutton_clicked(self):
        slimedialog = SlimeCreditsWindow(self)
        slimedialog.show()
    def on_char1creditsbutton_clicked(self):
        char1dialog = Char1CreditsWindow(self)
        char1dialog.show()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(3000, 2000)
        #self.setGeometry
        self.setWindowTitle("Main Menu")
        font = QFont('impact', 25)
        buttonimage = "background-image: url(mainmenufolder/MenuAssets/buttongradient.png)"
        
        # button1 (New Game) setup  
        self.button1 = QtWidgets.QPushButton('New Game', self)
        self.button1.setGeometry(500, 50, 2000, 300)
        self.button1.setStyleSheet(buttonimage)
        self.button1.setFont(font)
    
        
        
        # character selection button
        self.button2 = QtWidgets.QPushButton('Select Character', self)
        self.button2.setGeometry(500, 450, 2000, 300)
        self.button2.setStyleSheet(buttonimage)
        self.button2.setFont(font)
        self.button2.clicked.connect(self.on_button2_clicked)
        
        # level selection button
        self.button3 = QPushButton('Select Level', self)
        self.button3.setGeometry(500, 850, 2000, 300)
        self.button3.setStyleSheet(buttonimage)
        self.button3.setFont(font)
        self.button3.clicked.connect(self.on_button3_clicked)
        
        # load game button
        button4 = QPushButton('Load Game', self)
        button4.setGeometry(500, 1250, 2000, 300)
        button4.setStyleSheet(buttonimage)
        button4.setFont(font)

        
        # settings
        button5 = QPushButton('', self)
        button5.setGeometry(820, 480, 80, 80)
        button5.setIcon(QIcon('cog.png'))
        button5.setStyleSheet('border:none; background-color:transparent;')
        button5.setIconSize(button5.rect().size())
        
        # credits
        self.button6 = QtWidgets.QPushButton('Credits', self)
        self.button6.setGeometry(500, 1650, 2000, 300)
        self.button6.setStyleSheet(buttonimage)
        self.button6.setFont(font)
        self.button6.clicked.connect(self.on_button6_clicked)

    def on_button2_clicked(self):
        dialog1 = CharDialog(self)
        dialog1.show()
    def on_button3_clicked(self):
        dialog2 = LevelWindow(self)
        dialog2.show()
    def on_button6_clicked(self):
        dialog3 = CreditsWindow(self)
        dialog3.show()
def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


