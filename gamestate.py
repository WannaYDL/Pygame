import random
from settings import *
from piece import Piece
from gamewall import GameWall
import pygame
class GameState():
    def __init__(self,screen):
        self.screen = screen
        self.wall = GameWall(screen)
        self.piece = Piece(random.choice(PIECE_TYPES)   #当前方块
                           ,screen,self.wall)
        #定时时间设初值
        self.timer_interval = TIMER_INTERVAL
        #启动定时器
        self.set_timer(self.timer_interval)

    def set_timer(self,timer_interval):
        #time.set_timer()第一个参数是事件类型编号，第二个是定时器时间间隔
        self.game_timer = pygame.time.set_timer(pygame.USEREVENT,
                                                timer_interval)
