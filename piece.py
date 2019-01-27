#TetrisGame/piece.py
from settings import *
import pygame
class Piece():
    def __init__(self,shape,screen):
        self.x = 3
        self.y = 0
        self.shape = shape
        self.screen = screen


    def paint(self):
        shape_template = PIECES[self.shape]

        for r in range(len(shape_template)):
            for c in range(len(shape_template[0])):
                if shape_template[r][c] == 'O':
                    self.draw_cell(self.x+c,self.y+r)

    def draw_cell(self,x,y):
        cell_position = (x*CELL_WIDTH+GAME_AREA_LEFT+1,
                         y*CELL_WIDTH+GAME_AREA_TOP+1)
        cell_width_height = ()
