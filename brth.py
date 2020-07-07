import pgzrun
# import globalValues 
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
TITLE = 'undetermined' 
LINE_COLOR = 'gold' 

rab_live = True 

class Gameclass:
    def __init__(self):
        self.level = 1 
        self.time = 0.
        self.score = 0
        self.game_speed = 30
        self.time_elapsed = 0.
        self.blink = True
        self.n_frames = 0
        self.game_on = False
        self.game_message = 'fine'
        self.reset()
        self.on = False 
    
    def reset(self):
        pass

    def check_game_over(self):
        pass


WIDTH = 1000
HEIGHT = 562 # 1000 * 9 // 16
start_pic = Actor('gamestart',(1000//2,562//2)) 
ACCEL = 1.0
DRAG = 0.9
TRAIL_LENGTH = 2
MIN_WRAP_FACTOR = 0.1
BOUNDS = Rect(0, 0, WIDTH, HEIGHT)
FONT = 'eunomia_regular'

warp_factor = MIN_WRAP_FACTOR
centerx = WIDTH // 2
centery = HEIGHT // 2
stars = []


class Star:
    __slots__ = (
        'pos', 'vel', 'brightness', 'speed', 'position_history'
    )

    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.brightness = 10
        self.speed = hypot(*vel)

    @property
    def end_pos(self):
        x, y = self.pos
        vx, vy = self.vel

        return (
            x - vx * warp_factor * TRAIL_LENGTH / 60,
            y - vy * warp_factor * TRAIL_LENGTH / 60,
        )


lastc = (1, 1, 1)


def draw_stars():
    def f(): return randint(0, 255)
    global lastc

    if randint(1, 120) != 1:
        color = lastc
    else:
        color = (f(), f(), f())
    lastc = color
    for star in stars:
        b = star.brightness
        cur_color = (int(i*b/5) for i in color)
        # color = (b*2,b*2,b*2)
        # color = (1,111,11)
        screen.draw.line(star.end_pos, star.pos, color)


def update_stars(dt):
    global stars, warp_factor
    warp_factor = (
        MIN_WRAP_FACTOR + (warp_factor - MIN_WRAP_FACTOR) * DRAG ** dt
    )

    while len(stars) < 300:
        # Pick a direction and speed
        angle = uniform(-pi, pi)
        speed = 255 * uniform(0.3, 1.0) ** 2

        # Turn the direction into position and velocity vectors
        dx = cos(angle)
        dy = sin(angle)
        d = uniform(25 + TRAIL_LENGTH, 100)
        pos = centerx + dx * d, centery + dy * d
        vel = speed * dx, speed * dy

        stars.append(Star(pos, vel))

    # Update the positions of stars
    for s in stars:
        x, y = s.pos
        vx, vy = s.vel

        # Move according to speed and warp factor
        x += vx * warp_factor * dt
        y += vy * warp_factor * dt
        s.pos = x, y

        # Grow brighter
        s.brightness = min(s.brightness + warp_factor * 200 * dt, s.speed)

        # Get faster
        s.vel = vx * 2 ** dt, vy * 2 ** dt

    # Drop any stars that are completely off-screen
    stars = [
        star
        for star in stars
        if BOUNDS.collidepoint(star.end_pos)
    ]


game = Gameclass() 

def pos_update():
    pass 
def update(dt):
    if not game.on:
        update_stars(dt)
        pos_update()
        return 


def draw():
    screen.clear()
    if not game.on:
        start_pic.draw()
        draw_stars()
        # screen.fill('red')
        # screen.blit('background',(0,0))
        return 
    # 下面写游戏开始后的内容


def on_mouse_down(pos):
    print(f"you just click{pos}") 
    if not game.on:
        if start_pic.collidepoint(pos):
            game.on = True 
def on_mouse_move(pos):
    if not game.on:
        if start_pic.collidepoint(pos):
            start_pic.angle = 20
        else :
            start_pic.angle = 0
def on_key_down(key):
    pass
    # mainspeed = 10
    # if key is keys.UP:
    #     rab.y -= mainspeed
    # elif key is keys.DOWN:
    #     rab.y += mainspeed
    # elif key is keys.LEFT:
    #     rab.x -= mainspeed
    # elif key is keys.RIGHT:
    #     rab.x += mainspeed


pgzrun.go()
