#TetrisGame/piece.py

from settings import *
import pygame
class Piece():
    def __init__(self,shape,screen):
        self.x = 3
        self.y = 0
        self.shape = shape
        self.turn_times = 0     #翻转了几次决定了方块当前的状态，初始值为0
        self.screen = screen

    #画出形状为piece的方块
    def paint(self):
        shape_template = PIECES[self.shape]
        shape_turn = shape_template[self.turn_times]
        #print(len(shape_template))len(shape_template)为矩阵行数
        #print(len(shape_template[0]))len(shape_template[0])为矩阵列数
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[1])):
                if shape_turn[r][c] == 'O':
                    self.draw_cell(self.x+c,self.y+r)
    #绘制  方格
    def draw_cell(self,x,y):
        cell_position = (x*CELL_WIDTH+GAME_AREA_LEFT+1,
                         y*CELL_WIDTH+GAME_AREA_TOP+1)
        cell_width_height = (CELL_WIDTH-2,CELL_WIDTH-2)
        cell_rect = pygame.Rect(cell_position,cell_width_height)
        pygame.draw.rect(self.screen,CELL_COLOR,cell_rect)

    #判断是否在最右边
    def can_move_right(self):
        shape_mtx = PIECES[self.shape]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.x + c >= COLUMN_NUM - 1:
                        return  False
        return  True

    def can_move_left(self):
        shape_mtx = PIECES[self.shape]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] =='O':
                    if (self.x + c) == 0:
                        return  False
        return  True

    def can_move_down(self):
        shape_mtx = PIECES[self.shape]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.y + r >= LINE_NUM-1:
                        return  False
        return  True

    #判断是否可以旋转
    def can_turn(self):
        shape_list_len = len(PIECES[self.shape])
        turn_times = (self.turn_times + 1) %  shape_list_len
        shape_mst = PIECES[self.shape][turn_times]
        for r in range(len(shape_mst)):
            for c in range(len(shape_mst[0])):
                if shape_mst[r][c] == 'O':
                    if (self.x + c >= COLUMN_NUM - 1 or self.x+c < 0) \
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
        '''方块向下移动1格'''
        if self.can_move_down():
            self.y += 1

    def turn(self):
        shape_list_len = len(PIECES[self.shape])
        if self.can_turn:
            self.turn_times = (self.turn_times + 1) % shape_list_len
