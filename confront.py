
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
keyboard: Keyboard  # 类型标注
screen: Screen  # 类型标注

class Confront:
    def __init__(self):
        pass 
    
class Skill:
    def __init__(self,screen,name = 'uncertain',consume = 1,power = 10):
        self.name = name 
        self.screen  = screen 
        self.consume = consume 
        self.power = power 
    def act(self):
        self.screen.draw.filled_circle(rand_pos(),100,rand_color())
        self.screen.draw.filled_circle(rand_pos(),10,rand_color())
        self.screen.draw.filled_circle(rand_pos(),10,rand_color())
    def scherm(self,pos = rand_pos()):
        self.screen.draw.filled_circle(pos,150,'lavender')
    def table_turn(self,others,this_part):
        o = choice(others) 
        others.remove(o) 
        this_part.append(o) 
    def purify(self,others,this_part):
        if not others:
            return (0,0) 
        o = choice(others) 
        others.remove(o) 
        this_part.append(o) 
        return o.pos() 
    def drift(self,me,other,e,cur_time):
        # 单次攻击 
        f,t = me.ac.pos,other.ac.pos
        print(f,t)
        e.show_effects(f,t,cur_time)  
        e.real_effects(me,other,self) 


class Role:
    def __init__(self,ac,skills = None, hp = 1000,mp = 1000 ):
        self.skills = skills 
        self.mp = mp 
        self.ac = ac 
        self.hp = hp 
        # self.skills = ['walk'] 
        self.spinning = False 
        self.has_scherm = False 
    def draw(self):
        self.ac.draw() 
    def update(self):
        if self.spinning:
            self.ac.angle += 1
    def drift_attack(self,other,J,screen,skill,cur_time,consume = 1):
        if not J:
            return 
        e = Effect(self.ac.pos) 
        skill.drift(self,other,e,cur_time )  
    def release_attack(self,other,Q,screen,consume = 1):
        if  not Q or self.mp <= 0:
            return 
        self.mp -= consume  
        for point in around_pos(self.ac.pos):
            screen.draw.filled_circle(point,5,rand_color())
            if other.ac.collidepoint(point):
                self.attack(other) 
        # pass 
    def set_scherm(self,skill, pos = rand_pos()):
        skill.scherm(pos) 
        self.has_scherm = True 

    def smooth_walk(self,s,u,d,l,r,B,E,Q):
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
        # pass
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
        # if self.ac.collidepoint(other.ac.pos):
        if self.ac.colliderect(other.ac) :
            self.attack(other) 
    def pos(self):
        return self.ac.pos 
class confront_BackGround:
    def __init__(self,*acs):
        self.acs = acs  

    def draw(self,i = 0):
        self.acs[i].draw() 
    def drop(self):
        pass 
    def shake(self):
        if randint(1,10) < 5:
            self.draw() 
        else :
            self.draw(1) 