#TetrisGame/piece.py
from settings import *
from pygame import *
import pygame
from  gamedisplay import GameDisplay

class Piece():
    def __init__(self,shape,screen,gamewall):
        self.x = 4
        self.y = 0
        self.shape = shape
        self.turn_times = 0         #翻转了几次决定了方块当前的状态，初始值为0
        self.screen = screen
        self.is_on_botton = False   #标记是否到底
        self.game_wall = gamewall


    #画出形状为piece的方块
    def paint(self):
        shape_template = PIECES[self.shape]
        shape_turn = shape_template[self.turn_times]
        #print(len(shape_template))len(shape_template)为矩阵行数
        #print(len(shape_template[0]))len(shape_template[0])为矩阵列数
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    self.draw_cell(self.y + r,self.x + c)
    #绘制  方格
    def draw_cell(self,row,column):
        # cell_position = (x*CELL_WIDTH+GAME_AREA_LEFT+1,
        #                  y*CELL_WIDTH+GAME_AREA_TOP+1)
        # cell_width_height = (CELL_WIDTH-2,CELL_WIDTH-2)
        # cell_rect = pygame.Rect(cell_position,cell_width_height)
        #pygame.draw.rect(self.screen,PIECE_COLORS[self.shape],cell_rect)
        GameDisplay.draw_cell(self.screen,row,column,PIECE_COLORS[self.shape])

    #判断是否在最右边
    def can_move_right(self):
        #shape_list_len = len(PIECES[self.shape])
        #turn_times = (self.turn_times + 1) % shape_list_len
        #shape_mtx = PIECES[self.shape][turn_times]
        shape_mtx = PIECES[self.shape][self.turn_times]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.x + c >= COLUMN_NUM - 1:
                        return  False
        return  True

    def can_move_left(self):
        shape_mtx = PIECES[self.shape][self.turn_times]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] =='O':
                    if (self.x + c) <= 0:
                        return  False
        return  True

    # 判断是否到底
    def can_move_down(self):
        #shape_list_len = len(PIECES[self.shape])
        #turn_times = (self.turn_times + 1) % shape_list_len
        #shape_mtx = PIECES[self.shape][turn_times]
        shape_mtx = PIECES[self.shape][self.turn_times]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                # self.y+r是组成当前方块的小块所在的单元格的行号，+1就是下方单元格的行号
                # or后的is_wall()函数用来判断该小格下方是否为墙
                if shape_mtx[r][c] == 'O':
                    if self.y + r >= LINE_NUM-1 or \
                            self.game_wall.is_wall(self.y+r+1,self.x+c) :
                        return  False
        return  True

    #判断是否可以旋转
    def can_turn(self):
        shape_list_len = len(PIECES[self.shape])
        turn_times = (self.turn_times + 1) %  shape_list_len
        shape_mtx = PIECES[self.shape][turn_times]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx [0])):
                if shape_mtx[r][c] == 'O':
                    if (self.x + c >= COLUMN_NUM or self.x+c < 0) \
                            or (self.y + r >= LINE_NUM or self.y + r < 0):
                        return  False
        return  True

    def move_right(self):
        #方格向右移动1个单元格
        if self.can_move_right():
            self.x += 1

    def move_left(self):
        #方格向左移动一格
        if self.can_move_left():
            self.x -= 1

    def move_down(self):
         #方块向下移动1格
        if self.can_move_down():
            self.y += 1
        else:
            self.is_on_botton = True

    def fall_down(self):
        while not self.is_on_botton:
            self.move_down()

    def turn(self):
        shape_list_len = len(PIECES[self.shape])
        if self.can_turn():
            self.turn_times = (self.turn_times + 1) % shape_list_len


