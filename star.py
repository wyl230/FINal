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
warp_factor = MIN_WRAP_FACTOR
centerx = WIDTH // 2
centery = HEIGHT // 2
ACCEL = 1.0
DRAG = 0.9
TRAIL_LENGTH = 2
MIN_WRAP_FACTOR = 0.1
BOUNDS = Rect(0, 0, WIDTH, HEIGHT)


stars = []

lastc = (255, 255, 255)

def set_star_point(pos):
    global centerx,centery 
    centerx,centery = pos 
def draw_stars(screen):
    def f(): return randint(10, 255)  # brighter
    global lastc

    if randint(1, 60) != 1:
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

