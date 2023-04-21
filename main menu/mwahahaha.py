
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QFont
import PyQt5
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QMenuBar, QStatusBar,QDialogButtonBox, QDialog, QApplication, QMainWindow, QPushButton, QToolTip, QMessageBox, QLabel, QVBoxLayout, QWidget)
import site
site.getsitepackages()
import pygame, sys, random
from pygame.locals import *
from tkinter import *
import os
import signal
class CharDialog(QMainWindow):
    def __init__(self, parent=None):
        super(CharDialog, self).__init__(parent)
        self.setFixedSize(900, 300)

        self.char1button = QtWidgets.QPushButton('Character 1', self)
        self.char1button.setGeometry(0, 0, 300, 300)
        self.char2button = QtWidgets.QPushButton('Character 2', self)
        self.char2button.setGeometry(300, 0, 300, 300)
        self.char3button = QtWidgets.QPushButton('Character 3', self)
        self.char3button.setGeometry(600, 0, 300, 300)

class LevelWindow(QMainWindow):
    def __init__(self, parent=None):
        super(LevelWindow, self).__init__(parent)

class SlimeCreditsWindow(QDialog):
    def __init__(self, parent=None):
        super(SlimeCreditsWindow, self).__init__(parent)
        self.setFixedSize(1100,300)
        #display slime sprite
        self.slimecreditlabel = QtWidgets.QLabel('Slime sprites by SevenWave7 on itch.io',self)
        font = QFont('impact', 15)
        self.slimecreditlabel.move(50,100)
        self.slimecreditlabel.setFont(font)

class CreditsWindow(QMainWindow):
    def __init__(self, parent=None):
        super(CreditsWindow, self).__init__(parent)
        self.setFixedSize(1500,1000)
        self.slimespritebutton = QtWidgets.QPushButton('Slime Sprite Credits', self)
        self.slimespritebutton.setGeometry(100, 0, 300, 300)
        self.slimespritebutton.clicked.connect(self.on_slimespritebutton_clicked)
    def on_slimespritebutton_clicked(self):
        slimedialog = SlimeCreditsWindow(self)
        slimedialog.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(3000, 2000)
        self.setWindowTitle("Main Menu")
        
        # background setup
        background = QLabel(self)
        pixmap = QPixmap('gradient.png')
        pixmap = pixmap.scaled(1000, 600)
        background.setPixmap(pixmap)
        background.setGeometry(0, 0, 1000, 600)
        font = QFont('impact', 25)
        
        # button1 (New Game) setup
        
        self.button1 = QtWidgets.QPushButton('New Game', self)
        self.button1.setGeometry(500, 50, 2000, 300)
        self.button1.setStyleSheet('background-image: url(buttongradient.png);')

        self.button1.setFont(font)
        #self.setCentralWidget(self.button1)
        #self.button1.clicked.connect(self.on_button1_clicked)
    
        
        
        # character selection button
        self.button2 = QtWidgets.QPushButton('Select Character', self)
        self.button2.setGeometry(500, 450, 2000, 300)
        self.button2.setStyleSheet('background-image: url(buttongradient.png);')
        self.button2.setFont(font)
        self.button2.clicked.connect(self.on_button2_clicked)
        
        # level selection button
        
        self.button3 = QPushButton('Select Level', self)
        self.button3.setGeometry(500, 850, 2000, 300)
        self.button3.setStyleSheet('background-image: url(buttongradient.png);')
        self.button3.setFont(font)
        self.button3.clicked.connect(self.on_button3_clicked)
        
        # load game button
        button4 = QPushButton('Load Game', self)
        button4.setGeometry(500, 1250, 2000, 300)
        button4.setStyleSheet('background-image: url(buttongradient.png);')
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
        self.button6.setStyleSheet('background-image: url(buttongradient.png);')
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


