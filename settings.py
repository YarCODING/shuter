import pygame as p
import sys
from random import*
import os


SCREENSIZE = (500, 700)
SCREEN = p.display.set_mode(SCREENSIZE)

clock = p.time.Clock()
FPS = 80

background = p.image.load('background.jpg')
menu_bg = p.image.load('menu_bg.jpg')

p.mixer.init()
p.mixer.music.load('music.mp3')
p.mixer.music.set_volume(0.2)
p.mixer.music.play(-1)


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255,0) 