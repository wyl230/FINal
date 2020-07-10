
# 当前玩家所具有的能力 

import pgzrun
# import globalValues
import time
import end_of_battle as eb 
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
# skills: point scherm drift rain
class State:
    def __init__(self):
        self.has_skills = [False if _ else True for _ in range(4) ] 
        self.hp = 1000
        self.mp = 800 
        self.shake = False 
        self.skills_power = [5 for _ in range(4)]
        # self.skill.consume = 
        self.purification_capacity = 2 
