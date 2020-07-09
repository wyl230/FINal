
import pgzrun
# import globalValues
from math import *
# from brth import *
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
vortexs = [Actor('vortex1'),Actor('vortex2'),Actor('vortex3'),Actor('vortex4'),Actor('vortex5'),]
vortex = [Actor('vortex1'),Actor('vortex2'),Actor('vortex3'),Actor('vortex4'),Actor('vortex5'),]
class Effect:
    def __init__(self,pos):
        self.dist = 0.0
        self.at_affects = at_effects
        self.cnt = 0
        for p in self.at_affects:
            p.x,p.y = pos 
    def init(self):
        self.cnt = 0
    def hunt_effects(self,f,t,cur_time):
        if self.cnt == 0:
            for v in at_effects:
                v.pos = f 
            self.cnt = 1
        elif self.cnt >= 5:
            self.init() 
        else :
            fx,fy = f 
            tx,ty = t 
            d = tx - fx,ty - fy 
            dx ,dy =(i/5 for i in d)  
            for i,e in zip(range(len(at_effects)),at_effects):
                x,y = e.pos 
                at_effects[i].pos = x + dx,y + dy
                print(at_effects[i].pos,x+dx,y+dy)
                at_effects[i].angle += 1
            self.cnt += 1                 
        # print(at_effects[0].pos)
        at_effects[elapse_pos(cur_time,3)].draw() 
    def show_effects(self,f,t,cur_time,cnt2,another = True  ):
        # dist = cal_dist(f,t) 
        if another:
            p = rand_pos() 
            for v in at_effects:
                v.pos = p
            at_effects[elapse_pos(cur_time,3)].draw() 
        else:
            # chose = choice(vortexs) 
            chose = vortexs[cnt2%5]
        # or below  also attck all 
            chose.pos = f
            chose.draw() 
            # print(self.dist)
    def real_effects(self,me,other,skill):
        other.hp -= skill.power 
        me.mp -= skill.consume 

def instant_text(msg,screen,pos = rand_pos()):
    screen.draw.text(msg,midtop = pos ) 
