import pgzrun
# import globalValues
import time
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
cur_time = 0.0
cnt = 0
rab_live = True
start_time = time.time()
rain = Draw_rain(100, 150)
randcolors = [choice(COLORS) for i in range(20)]
randposes = [rand_pos() for _ in range(100)] 
randtexts = [choice(texts) for _ in range(100) ]
class Gameclass:
    def __init__(self):
        self.level = 1
        self.time = 0.
        self.score = 0
        self.game_speed = 30
        self.time_elapsed = 0.
        self.show_text = False
        self.show_text_pos = (MIDDLE)
        self.blink = True
        self.n_frames = 0
        self.game_on = False
        self.preparing = False
        self.click_cnt = 0
        # self.game_on = True
        self.game_message = 'fine'
        self.reset()
        self.on = False
        self.confronting = False
        self.raining = False
        # self.confronting = True

    def reset(self):
        pass

    def check_game_over(self):
        pass


WIDTH = 1000
HEIGHT = 562  # 1000 * 9 // 16
MIDDLE = WIDTH//2, HEIGHT//2
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


lastc = (255, 255, 255)


def draw_stars():
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


game = Gameclass()
all_actors = [Actor('poke9', rand_pos()), Actor('poke', rand_pos()), Actor('poke2', rand_pos()), Actor('poke3', rand_pos()), Actor('poke4', rand_pos(
)), Actor('poke5', rand_pos()), Actor('poke6', rand_pos()), Actor('poke7', rand_pos()), Actor('poke8', rand_pos()), Actor('pokea', rand_pos())]
the_one = Role(Actor('op1b', rand_pos()), 'YOU')
this_part = []
opposite = [Role(Actor('pokemon2s', rand_pos()), 'cute dragonfly')
            for _ in range(randint(2, 3))]
add_opst = [Role(choice(all_actors)) for _ in range(5)]
opposite.extend(add_opst)
# ef1 = Effect()


def pos_update():
    pass


def update_confront():
    a = Skill(screen)
    global cur_time
    cur_time = time.time() - start_time
    # the_one.random_walk() 操控的角色抖动 可用来加大难度
    # 随机出现的屏障
    if percent(3):
        a.scherm(the_one, the_one.pos(), 30)
    for p in opposite:
        p.update()
        p.if_physical_atk(the_one)
        the_one.release_attack(p, keyboard[keys.Q], screen)
        the_one.drift_attack(
            p, keyboard[keys.J], screen, a, cur_time, False)  # False has votex
    for q in this_part:
        q.update()
    if game.show_text:
        instant_text('purifying!!!', screen, game.show_text_pos)
        # if keyboard[keys.P]:
        # a.purify(opposite,this_part)
    # if game.raining:
    #     pass
    #     # rain.update_rain()
    check_death()


def check_death():
    global opposite
    for p in opposite:
        if p.hp <= 0:
            opposite.remove(p)
    if the_one.hp < 0:
        screen.draw.text('you lose', midtop=rand_pos())
        # sleep(1)
        # time.sleep(1.0)
        # clock.schedule_unique(draw, 1.0)
        # clock.schedule_unique(update, 1.0)
        # print('you lose')
        game.confronting = False
        game.on = False
        the_one.hp = 1000
    elif not opposite:
        print('you win')
        game.confronting = False
        game.on = False  # 合并之后改为true
        the_one.hp = 1000
        opposite = [Role(Actor('pokemon2s', rand_pos()))
                    for _ in range(randint(3, 5))]
        add_opst = [Role(choice(all_actors)) for _ in range(3)]
        opposite.extend(add_opst)


def draw_main_info():
    pass


def main_update():
    pass


def update2_confront(dt):
    if game.raining:
        rain.update_rain(dt)


def update_preparation():
    pass


def draw_preparation(screen):
    # screen.draw.filled_circle((WIDTH//5,HEIGHT//4),100,u_color[0])
    ix, iy = WIDTH//5, HEIGHT//4
    for i, v in zip(range(len(vortex)), vortex):
        v.x = (i % 3)*222 + ix
        v.y = (i/3)*222 + iy
        v.draw()
        if v.image == 'check1':
            clicked = True
            if i == 0:
                screen.draw.text('you will have a more colorful life\n(more powerful when use skills)', midtop=(
                    WIDTH*2//3, HEIGHT // 10), fontsize=30, color=randcolors[i])
            elif i == 1:
                screen.draw.text('you will be full of courage to explore your life.\n(the moving speed increased)', midtop=(
                    WIDTH*2//3, HEIGHT // 2), fontsize=30, color=randcolors[i])
            elif i == 2:
                screen.draw.text('you will be full of courage to explore your life.\n(the moving speed increased)', midtop=(WIDTH*2//3, 2*HEIGHT // 5), fontsize=30, color =randcolors[i])
            elif i == 3:
                screen.draw.text('you will be full of courage to explore your life.\n(the moving speed increased)', midtop=(
                    WIDTH*3//7, 3*HEIGHT // 5), fontsize=30, color=randcolors[i])
            elif i == 4:
                screen.draw.text('you will be full of courage to explore your life.\n(the moving speed increased)', midtop=(
                    WIDTH*5//7, 4*HEIGHT // 5), fontsize=30, color=randcolors[i])

            screen.draw.filled_circle(rand_pos(), 10, rand_color())
    screen.draw.text('Please click on the Phalanx on the left.\nYou have three chances.', midtop=(
        WIDTH*3//4, HEIGHT // 5), fontsize=30, color='maroon')


def update(dt):
    if not game.on:
        update_stars(dt)
        pos_update()
        return
    if game.preparing:
        update_preparation()
        update_stars(dt)
    if game.confronting:
        update2_confront(dt)
        # update_confront() 在这里调用不能draw
        return
    # 游戏主界面
    main_update()
    # 展示信息
    draw_main_info()


def draw_info(screen):
    cur_row = 0
    btn = Button(screen, f'wyl hp = {the_one.hp}', (0, 0), the_one.hp, 22)
    btn.draw_button()
    cur_row += 23
    btn = Button(screen, f'wyl mp = {the_one.mp}',
                 (0, cur_row), the_one.mp, 22)
    btn.draw_button()
    cur_row += 13
    for p in opposite:
        cur_row += 18
        btn2 = Button(
            screen, f'{p.name}[{cur_row//25}] hp = {p.hp}', (0, cur_row), p.hp/6, 15)
        btn2.draw_button(15)


def draw_confront():
    bg = confront_BackGround(Actor('bg6'))
    # bg = confront_BackGround(Actor('confrontbg4a'),Actor('confrontbg4b'))
    # bg.shake()
    bg.draw()
    the_one.draw()
    the_one.smooth_walk(keyboard[keys.SPACE], keyboard[keys.UP] or keyboard[keys.W], keyboard[keys.DOWN] or keyboard[keys.S],
                        keyboard[keys.LEFT]or keyboard[keys.A], keyboard[keys.RIGHT]or keyboard[keys.D], keyboard[keys.B], keyboard[keys.E], keyboard[keys.Q])
    for p in opposite + this_part:
        p.draw()
        p.random_walk()
    if game.raining:
        rain.draw_rain(screen)
    draw_info(screen)

    # screen.draw.filled_circle(rand_pos(),10,rand_color())
    # screen.draw.text('asdf',midtop = rand_pos())


def main_draw():
    game.confronting = True
    pass

def draw_start(screen):
    for i,pos in zip(range(10),randposes[:10]):
        # screen.draw.text(f'wyl{pos}',midtop = pos)
        screen.draw.text(f'{randtexts[i]}',midtop = pos,color = randcolors[i+2])
    start_pic.draw()
    text = Actor('text1s',midtop = (WIDTH//2+120,HEIGHT//5-99))
    text.angle += randint(-3,3) 
    text.draw() 
def draw():
    global TITLE
    screen.clear()
    if not game.on:
        draw_start(screen)
        draw_stars()
        # screen.fill('red')
        # screen.blit('background',(0,0))
        #
        return
    if game.preparing:
        draw_preparation(screen)
        draw_stars()
        return
    if game.confronting:
        TITLE = 'nothing can be done now..'
        draw_confront()
        update_confront()
        return
    main_draw()
    # 下面写游戏开始后的内容


def on_mouse_down(pos):
    print(f"you just click{pos}")
    if not game.on:
        if start_pic.collidepoint(pos):
            game.preparing = True
            game.on = True
        return
    if game.preparing:
        if game.click_cnt >= 3:
            game.preparing = False
            return
        for v in vortex:
            if v.collidepoint(pos):
                v.image = 'check1'
                game.click_cnt += 1
    #

# def move_key_board(key):
#     if game.confronting:
#         if key == keys.J:
#             game.raining = True
#         else :
#             game.raining = False


def on_mouse_move(pos):
    global centerx, centery
    if not game.on:
        if start_pic.collidepoint(pos):
            start_pic.angle = randint(-13, 13)
        else:
            start_pic.angle = 0
            centerx, centery = pos
        return
    if game.preparing:
        centerx, centery = pos
        return

    #


def confront_one_key_down(key):
    if key is keys.P:
        a = Skill(screen)
        game.show_text_pos = a.purify(opposite, this_part)
        game.show_text = True


def on_key_down(key):
    if game.confronting:
        confront_one_key_down(key)
        if key == keys.J and the_one.mp >= 100:
            game.raining = True
        return


def on_key_up(key):
    if game.confronting:
        if key == keys.J:
            game.raining = False
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


def shuttext():
    game.show_text = False


def cnter():
    global cnt
    print(cnt)
    cnt += 1
    if game.show_text:
        clock.schedule(shuttext, 1)


clock.schedule_interval(cnter, 1.0)
pgzrun.go()
