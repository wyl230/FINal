
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
from role import * 
from skills import * 
keyboard: Keyboard  # 类型标注
screen: Screen  # 类型标注

class Skill:
    def __init__(self, screen, name='uncertain', consume=1, power=5):
        self.name = name
        self.screen = screen
        self.consume = consume
        self.power = power

    def act(self):
        self.screen.draw.filled_circle(rand_pos(), 100, rand_color())
        self.screen.draw.filled_circle(rand_pos(), 10, rand_color())
        self.screen.draw.filled_circle(rand_pos(), 10, rand_color())

    def scherm(self, ac, pos=rand_pos(), power=100):
        self.screen.draw.filled_circle(pos, 150, 'DarkCyan')
        ac.hp = min(ac.hp + power, ac.maxHP)
        ac.mp = min(ac.mp + power, ac.maxMP)

    def table_turn(self, others, this_part):
        o = choice(others)
        others.remove(o)
        this_part.append(o)

    def purify(self, others, this_part):
        if not others:
            return (0, 0)
        o = choice(others)
        others.remove(o)
        this_part.append(o)
        return o.pos()

    def drift(self, me, other, e, cur_time,cnt2, another=True):
        # 单次攻击
        f, t = me.ac.pos, other.ac.pos
        # print(f, t)
        e.show_effects(f, t, cur_time,cnt2, another)
        e.real_effects(me, other, self)

