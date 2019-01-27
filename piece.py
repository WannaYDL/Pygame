#TetrisGame/piece.py

from settings import *
import pygame
class Piece():
    def __init__(self,shape,screen):
        self.x = 3
        self.y = 0
        self.shape = shape
        self.screen = screen

    #画出形状为piece的方块
    def paint(self):
        shape_template = PIECES[self.shape]

        for r in range(len(shape_template)):
            for c in range(len(shape_template[0])):
                if shape_template[r][c] == 'O':
                    self.draw_cell(self.x+c,self.y+r)
    #绘制  方格
    def draw_cell(self,x,y):
        cell_position = (x*CELL_WIDTH+GAME_AREA_LEFT+1,
                         y*CELL_WIDTH+GAME_AREA_TOP+1)
        cell_width_height = (CELL_WIDTH-2,CELL_WIDTH-2)
        cell_rect = pygame.Rect(cell_position,cell_width_height)
        pygame.draw.rect(self.screen,CELL_COLOR,cell_rect)
    def move_right(self):
        #方格向右移动1个单元格
        self.x += 1
    def move_left(self):
        #方格向左移动一格
        self.x -= 1

    def move_down(self):
        '''方块向下移动1格'''
        self.y += 1