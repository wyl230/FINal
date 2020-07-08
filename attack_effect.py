
import pgzrun
# import globalValues
from math import *
from random import *
# from somefunc import *
from somefunc import *
import numpy as np 
from pgzero.actor import Actor
from pgzero.loaders import sounds
from pgzero.clock import clock
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
    def __init__(self,pos):
        self.dist = 0.0
        self.at_affects = at_effects
        for p in self.at_affects:
            p.x,p.y = pos 
    def init(self):
        self.dist = 0.0 
    def show_effects(self,f,t,cur_time,dx = 10,dy = 10 ):
        dist = cal_dist(f,t) 
        at_effects[elapse_pos(cur_time,3)].draw() 
        if self.dist >= dist:
            return 
        fx,fy = f 
        tx,ty = t 
        d = tx - fx,ty - fy 
        dx ,dy = d[0]/5,d[1]/5 
        for e in at_effects:
            x,y = e.pos 
            e.pos = x + dx,y + dy
            e.angle += 1
            self.dist += cal_dist((0,0),(dx,dy)) 
            # print(self.dist)
    def real_effects(self,me,other,skill):
        other.hp -= skill.power 
        me.mp -= skill.consume 

def instant_text(msg,screen,pos = rand_pos()):
    screen.draw.text(msg,midtop = pos ) 
