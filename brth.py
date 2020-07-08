import pgzrun
# import globalValues
import time 
from math import *
from random import *
from somefunc import *
from confront import * 
from button import * 
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
TITLE = '好听的名字呢？？？？'
LINE_COLOR = 'gold'

rab_live = True
start_time = time.time()

class Gameclass:
    def __init__(self):
        self.level = 1
        self.time = 0.
        self.score = 0
        self.game_speed = 30
        self.time_elapsed = 0.
        self.blink = True
        self.n_frames = 0
        # self.game_on = False
        self.game_on = True 
        self.game_message = 'fine'
        self.reset()
        self.on = False
        # self.confronting = False 
        self.confronting = True 

    def reset(self):
        pass

    def check_game_over(self):
        pass


WIDTH = 1000
HEIGHT = 562  # 1000 * 9 // 16
MIDDLE = WIDTH//2,HEIGHT//2
start_pic = Actor('gamestart', (1000//2, 562//2))
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


game = Gameclass()
the_one = Role(Actor('op1b'))
this_part = [] 
opposite = [Role(Actor('pokemon2s')) for _ in range(3)]
# ef1 = Effect() 
def pos_update():
    pass

def update_confront():
    a = Skill(screen) 
    cur_time = time.time() - start_time 
    # the_one.random_walk() 操控的角色抖动 可用来加大难度 
    if percent(3):
            a.scherm(the_one.pos())
    for p in opposite:
        p.update()
        p.if_physical_atk(the_one)    
        the_one.release_attack(p,keyboard[keys.Q],screen)      
        the_one.drift_attack(p,keyboard[keys.J],screen,a,cur_time)
    for q in this_part:
        q.update() 

            # if keyboard[keys.P]:
                # a.purify(opposite,this_part) 
    check_death() 


def check_death():
    for p in opposite:
        if p.hp <= 0:
            opposite.remove(p) 
    if the_one.hp < 0:
        screen.draw.text('you lose',midtop = rand_pos())
        # sleep(1)
        time.sleep(1.0)
        # clock.schedule_unique(draw, 1.0)
        # clock.schedule_unique(update, 1.0)
        # print('you lose') 
        game.confronting = False 
def draw_main_info():
    pass
def update(dt):
    if not game.on:
        update_stars(dt)
        pos_update()
        # return
    if game.confronting:
        pass 
        # update_confront() 在这里调用不能draw
    # 游戏主界面 

    # 展示信息 
    draw_main_info() 
        
def draw_info(screen):
    cur_row = 0 
    btn = Button(screen,f'wyl hp = {the_one.hp}',(0,0),the_one.hp,22 ) 
    btn.draw_button()  
    cur_row += 23
    btn = Button(screen,f'wyl mp = {the_one.mp}',(0,cur_row),the_one.mp,22 ) 
    btn.draw_button()  
    for p in opposite:
        cur_row += 25
        btn2 = Button(screen,f'oppo[{cur_row//25}] hp = {p.hp}',(0,cur_row),p.hp,22 ) 
        btn2.draw_button() 
def draw_confront():
    bg = confront_BackGround(Actor('bg6'))
    # bg = confront_BackGround(Actor('confrontbg4a'),Actor('confrontbg4b')) 
    # bg.shake()
    bg.draw() 
    the_one.draw()  
    the_one.smooth_walk(keyboard[keys.SPACE], keyboard[keys.UP], keyboard[keys.DOWN], keyboard[keys.LEFT], keyboard[keys.RIGHT],keyboard[keys.B],keyboard[keys.E],keyboard[keys.Q])
    for p in opposite + this_part:
        p.draw() 
        p.random_walk()
    draw_info(screen) 


    # screen.draw.filled_circle(rand_pos(),10,rand_color())
    # screen.draw.text('asdf',midtop = rand_pos()) 

def draw():
    global TITLE 
    screen.clear()
    if not game.on:
        start_pic.draw()
        draw_stars()
        # screen.fill('red')
        # screen.blit('background',(0,0))
        # 
        # return
    if game.confronting:
        TITLE = 'nothing can be done now..'
        draw_confront() 
        update_confront() 
        return 
    # 下面写游戏开始后的内容


def on_mouse_down(pos):
    print(f"you just click{pos}")
    if not game.on:
        if start_pic.collidepoint(pos):
            game.on = True
        return 
    # 

def on_mouse_move(pos):
    if not game.on:
        if start_pic.collidepoint(pos):
            start_pic.angle = 20
        else:
            start_pic.angle = 0
            global centerx, centery 
            centerx, centery = pos 
        return 
    # 


def confront_one_key_down(key):
    if key is keys.P:
        a = Skill(screen)
        a.purify(opposite,this_part) 
def on_key_down(key):
    if game.confronting:
        confront_one_key_down(key) 
        return 
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
