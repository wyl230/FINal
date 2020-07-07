
from somefunc import *
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
from pgzero.builtins import keymods 
from pgzero.constants import mouse
from pgzero.animation import animate
from pgzero.keyboard import keys, Keyboard
from pgzero.screen import Screen
keyboard: Keyboard  # 类型标注
screen: Screen  # 类型标注
# x width 
# y height 
class Button():
    def __init__(self,screen,msg,midtop,width = 330,height = 440):
        self.msg = msg 
        self.screen = screen 
        self.width,self.height = width,height 
        self.button_color = (123,12,44) 
        self.text_color = (11,222,12)
        self.midtop = midtop 
        x,y = midtop 
        self.rect =Rect(x,y,width,height)

        # self.prep_msg(msg) 
    # def prep_msg(self,msg):
    #     pass 

    def draw_button(self):
        self.screen.draw.filled_rect(self.rect,self.button_color)
        self.screen.draw.text(self.msg,self.midtop,fontsize = 28)