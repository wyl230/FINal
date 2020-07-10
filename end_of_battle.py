from math import *
from random import *
from somefunc import *
from pre_written import *
from confront import *
from rainstorm import *
from button import *
from pgzero.actor import Actor
from pgzero.loaders import sounds
from pgzero.keyboard import keys
from pgzero.rect import Rect, ZRect
from pgzero.loaders import sounds, images
from pgzero import music, tone
from pgzero.clock import clock
from pgzero.builtins import keymods  # 似乎没有作用
from pgzero.constants import mouse
from pgzero.animation import animate
from pgzero.keyboard import keys, Keyboard
from pgzero.screen import Screen
keyboard: Keyboard  # 类型标注
screen: Screen  # 类型标注
lose = Actor('lose',anchor=(50,100)) 
win = Actor('win',anchor=(50,100)) 
bg = [Actor('nbg1s'),Actor('nbg2ll'),Actor('nbg2ds'),Actor('confrontbg1'),Actor('confrontbg2'),Actor('confrontbg3')]
tip = Actor('tip1',midbottom=(WIDTH//2,HEIGHT-100))
def draw_lose(screen = None):
    bg[0].draw()
    lose.draw()
    screen.draw.text()
    tip.draw()
def draw_win(screen = None):
    choice(bg[1:3]).draw()
    win.draw()
    tip.draw()