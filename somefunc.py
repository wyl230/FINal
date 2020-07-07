from random import *


def rand_color():
    def f(): return randint(1, 255)
    return f(), f(), f()


def swing(*a):
    u = 100
    return [v + randint(-u, u) for v in a]


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
    

