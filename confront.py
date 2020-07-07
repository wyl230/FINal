
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
# keymods属性有: LSHIFT, RSHIFT, SHIFT, LCTRL, RCTRL, CTRL, LALT, RALT, ALT, LMETA, RMETA, META, NUM, CAPS, MODE
# 可检测mod值，LCtrl: 64, RCtrl: 128, LAlt: 256, RAlt: 512, LShift: 1, RShift: 1, Capital: 8192
from pgzero.constants import mouse
from pgzero.animation import animate
from pgzero.keyboard import keys, Keyboard
from pgzero.screen import Screen
keyboard: Keyboard  # 类型标注
screen: Screen  # 类型标注

class Confront:
    def __init__(self):
        pass 

class Skill:
    def __init__(self,screen,name = 'uncertain'):
        self.name = name 
        self.screen  = screen 
    def act(self):
        self.screen.draw.filled_circle(rand_pos(),100,rand_color())
        self.screen.draw.filled_circle(rand_pos(),10,rand_color())
        self.screen.draw.filled_circle(rand_pos(),10,rand_color())

class Role:
    def __init__(self,ac, hp = 100):
        self.ac = ac 
        self.hp = hp 
        self.skills = ['walk'] 
        self.spinning = False 
    def draw(self):
        self.ac.draw() 
    def update(self):
        if self.spinning:
            self.ac.angle += 1
    def release_attack():
        pass 
    def smooth_walk(self,s,u,d,l,r,B,E):
        mainspeed = 10        
        if s:
            # self.ac.x += mainspeed
            self.ac.angle += 1 
        if u:
            self.ac.y -= mainspeed
        if d:
            self.ac.y += mainspeed
        if l:
            self.ac.x -= mainspeed
        if r:
            self.ac.x += mainspeed
        if B:
            self.spinning = True 
        if E:
            self.spinning = False 
    def random_walk(self):
        f = lambda :randint(-10,10) 
        self.ac.angle += randint(-1,1) 
        self.ac.x += f() 
        self.ac.y += f() 
        if not is_in(self.ac.x,self.ac.y):
            self.ac.x = 300 
            self.ac.y = 300 
    def attack(self,other,atk = 1):
        other.hp -= atk  
    def if_physical_atk(self,other):
        if self.ac.collidepoint(other.ac.pos):
            self.attack(other) 
            print(other.hp)
    def pos(self):
        return self.ac.pos 
class confront_BackGround:
    def __init__(self,*acs):
        self.acs = acs  

    def draw(self,i = 0):
        self.acs[i].draw() 

    def shake(self):
        if randint(1,10) < 5:
            self.draw() 
        else :
            self.draw(1) 