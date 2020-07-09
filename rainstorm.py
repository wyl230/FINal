import pgzrun
from math import *
from random import *
from somefunc import * 
from pgzero.actor import Actor
from pgzero.loaders import sounds
from pgzero.clock import clock
from pgzero.screen import Screen
from pgzero.rect import Rect
from pgzero.keyboard import keys
screen: Screen  # 类型标注 
WIDTH = 1000
HEIGHT = 562  # 1000 * 9 // 16
BOUNDS = Rect(0,0,WIDTH,HEIGHT) 
ACCEL = 1.0 
DRAG = 0.9 
TRAIL_LENGTH = 2 
MIN_WRAP_FACTOR = 0.1 
warp_factor = MIN_WRAP_FACTOR 

class Rain():
    def __init__(self,pos,vel = (0,1)):
        self.pos = pos 
        self.vel = vel 
        self.brightness = 10 
        self.speed = hypot(*vel) 
    @property
    def end_pos(self):
        x,y = self.pos 
        vx,vy = self.vel 

        return (
            x - vx * 10,
            y - vy * 10 
        )

drops = [Rain((x,y)) for x in range(1000)[::44] for y in range(1000)[::100]]
def draw():
    screen.clear() 
    for drop in drops:
        screen.draw.line(drop.end_pos,drop.pos,rand_color()) 
def update(dt):
    global drops ,warp_factor
    warp_factor = (
        MIN_WRAP_FACTOR + (warp_factor - MIN_WRAP_FACTOR) * DRAG ** dt
    )
    while len(drops) < 100:
        speed = 255 * uniform(0.3,1.0)  ** 2 

        dx = 1 
        dy = uniform(-0.1,0.1) 
        d = uniform(25 + TRAIL_LENGTH,100) 
        pos = randint(1,1000),40
        drops.append(Rain(rand_pos())) 
    for drop in drops:
        x,y = drop.pos
        vx,vy = drop.vel 

        x += vx * 100 
        y += vy * 100 
        drop.pos = x,y 
    drops = [
        drop 
        for drop in drops 
        if BOUNDS.collidepoint(drop.end_pos) 
    ]
    # global drops 
    # while len(stars) < 300: 
    # stars.append()
pgzrun.go() 