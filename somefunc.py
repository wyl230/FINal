from random import *
import numpy as np
WIDTH = 1000
HEIGHT = 562  # 1000 * 9 // 16


def percent(x):
    return randint(1, 100) < x


def cal_dist(f, t):
    a = np.array(f)
    b = np.array(t)
    return np.sqrt(np.sum(np.square(a - b)))


def elapse_pos(t, p=100, q=10):
    return int(t*q) % p
# gap 越小 越冒险 攻击力越强


def around_pos(pos, gap=50):
    def f(): return randint(-300, 300)
    x, y = map(int, pos)
    return [(i, j) for i in range(x + f(), max(x + f(), x + f()))[::gap]
            for j in range(y + f(), max(y + f(), y + f()))[::gap]]


def rand_color():
    def f(): return randint(1, 255)
    return f(), f(), f()


def rand_pos(x=WIDTH, y=HEIGHT):
    def h(): return randint(1, x)
    def g(): return randint(1, y)
    return h(), g()


def swing(*a):
    u = 100
    return [v + randint(-u, u) for v in a]


def is_in(x, y):
    return 0 < x < HEIGHT and 0 < y < WIDTH

# def change_v(*ac):
#     p1, p2 = ac
#     dx = p1.x - p2.x
#     dy = p1.y - p2.y
#     rr = dx**2 + dy ** 2
#     v1,v2 = p1.v,p2.v
#     a =  p2.m / rr
#     ax = a*dx/(rr**0.5)
#     ay = a*dy/(rr**0.5)
#     v1[0] += ax
#     v1[1] += ay
#     a =  p1.m / rr
#     ax = a*dx/(rr**0.5)
#     ay = a*dy/(rr**0.5)
#     v2[0] += ax
#     v2[1] += ay
#     return v1,v2

# def v_caused_change(p,q):
#     ca = lambda s:( s.x - s.v[0],s.y - s.v[1] )
#     cb = lambda s:( s.x + s.v[0],s.y + s.v[1] )
#     return   ca(p),cb(q)
