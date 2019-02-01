import random
from settings import *
from piece import Piece
from gamewall import GameWall
import pygame
class GameState():
    def __init__(self,screen):
        self.screen = screen
        self.wall = GameWall(screen)
        #self.piece = Piece(random.choice(PIECE_TYPES),screen,self.wall)
        self.piece = None
        #定时时间设初值
        self.timer_interval = TIMER_INTERVAL
        #启动定时器
        #self.set_timer(self.timer_interval)
        self.game_score = 0
        self.stopped = True     #游戏是否停止

    def set_timer(self,timer_interval):
        #time.set_timer()第一个参数是事件类型编号，第二个是定时器时间间隔
        self.game_timer = pygame.time.set_timer(pygame.USEREVENT,
                                                timer_interval)

    def add_score(self,score):
        self.game_score += score

    def start_game(self):
        self.stopped = False
        self.set_timer(TIMER_INTERVAL)
        self.timer_interval = TIMER_INTERVAL
        self.piece = Piece(random.choice(PIECE_TYPES),self.screen,self.wall)
