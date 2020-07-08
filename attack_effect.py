
import pgzrun
# import globalValues
from math import *
from random import *
# from somefunc import *
from somefunc import *
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
from pgzero.constants import mouse
from pgzero.animation import animate
from pgzero.keyboard import keys, Keyboard
from pgzero.screen import Screen
keyboard: Keyboard  # 类型标注
screen: Screen  # 类型标注

at_effects = [Actor('at1'),Actor('at2'),Actor('at3')]

class Effect:
    def __init__(self): 
        pass 
    def show_effects(self,f,t):
        pass 
    def read_effects(self,me,other,skill):
        other.hp -= skill.power 
        me.mp -= skill.consume 