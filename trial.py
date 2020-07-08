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
cur_time = 0.0 
def draw_rain():
    for i in range(100):
        x,y = (10*i,5 * elapse_pos(cur_time))
        to_pos = x + randint(-5,5), y+randint(5,22) 
        x,y = x + randint(-5,5) ,y+randint(-5,5)
        screen.draw.line((x,y),to_pos,rand_color())
def draw_time_info():
    # print(1)
    global cur_time
    # screen.draw.text(f'{cal_dist((0,0),(1,1))}',midtop = MIDDLE)
    screen.draw.text(f'{cur_time:.2f}',midtop = MIDDLE) 
cnt = 1 
def f():
    global cnt 
    print(cnt)
    cnt += 1  
# a = Effect() 
def update(dt):
    global cur_time 
    screen.clear() 
    cur_time = time() - start_time 
    # a.show_effects((0,0),(444,333),cur_time) 
    # at_effects[elapse_pos(cur_time,3)].draw()
    # for e in at_effects:
    #     x,y = e.pos 
    #     e.pos = x + 10,y + 10 
    #     e.angle += 1
    # draw colorful rain 
    # draw_time_info() 
    # draw_rain(cur_time) 
    # clock.schedule(draw_rain,1.1) 
    # if cur_time < 1 : 
    #     clock.schedule_unique(f,1.1) 
# 此类函数就在draw 和 update以外调用
clock.schedule_interval(f,1.1) 
    # 
def draw():
    clock.schedule(draw_time_info,2.0)
    pass
    # a.draw() 
    # pass 
    # screen.draw.filled_rect( Rect(0, 0, 222, 300), "gold" )
    # screen.draw.line(rand_pos(),rand_pos(),rand_color())
pgzrun.go() 

