import pgzrun
from math import *
from random import *
from somefunc import * 
from time import * 
from attack_effect import * 
from pgzero.actor import Actor
from pgzero.loaders import sounds
from pgzero.clock import clock
from pgzero.screen import Screen
from pgzero.rect import Rect
from pgzero.keyboard import keys
screen: Screen  # 类型标注
TITLE = 'undetermined'

WIDTH = 800 
HEIGHT = 600 
MIDDLE = WIDTH//2,HEIGHT//2
start_time = time() 
LINE_COLOR = 'gold' 
# a = Actor('at.gif') 
def update(dt):
    screen.clear() 
    cur_time = time() - start_time 
    screen.draw.text(f'{cur_time:.2f}',midtop = MIDDLE) 
    at_effects[elapse_pos(cur_time,3)].draw()
    
    for i in range(100):
        x,y = (10*i,5 * elapse_pos(cur_time))
        to_pos = x + randint(-5,5), y+randint(5,22) 
        x,y = x + randint(-5,5) ,y+randint(-5,5)
        screen.draw.line((x,y),to_pos,rand_color())
def draw():
    pass
    # a.draw() 
    # pass 
    # screen.draw.filled_rect( Rect(0, 0, 222, 300), "gold" )
    # screen.draw.line(rand_pos(),rand_pos(),rand_color())
pgzrun.go() 
