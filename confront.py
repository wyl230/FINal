
import pgzrun
# 编写注意 pos等调用在.ac.
# import globalValues
from math import *
from random import *
from somefunc import *
from attack_effect import *
from pgzero.actor import Actor
from pgzero.loaders import sounds
from pgzero.clock import clock
from pgzero.rect import Rect
from pgzero.keyboard import keys
from pgzero.actor import Actor
from pgzero.rect import Rect, ZRect
from pgzero.loaders import sounds, images
from pgzero import music, tone
from pgzero.clock import clock
from pgzero.builtins import keymods  # 似乎没有作用
# keymods属性有: LSHIFT, RSHIFT, SHIFT, LCTRL, RCTRL, CTRL, LALT, RALT, ALT, LMETA, RMETA, META, NUM, CAPS, MODE
# 可检测mod值，LCtrl: 64, RCtrl: 128, LAlt: 256, RAlt: 512, LShift: 1, RShift: 1, Capital: 8192
from pgzero.constants import mouse
from pgzero.animation import animate
from pgzero.keyboard import keys, Keyboard
from pgzero.screen import Screen
from role import * 
from skills import * 
keyboard: Keyboard  # 类型标注
screen: Screen  # 类型标注

def confront_init():
    pass 
class Confront:
    def __init__(self):
        pass

class confront_BackGround:
    def __init__(self, *acs):
        self.acs = acs

    def draw(self, i=0):
        self.acs[i].draw()

    def drop(self):
        pass

    def shake(self):
        if randint(1, 10) < 5:
            self.draw()
        else:
            self.draw(1)
