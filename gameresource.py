#TetrisGame/gameresource
import pygame

class GameResource():
    def __init__(self):
        self.img_path = '//home/yuandl/PycharmProjects/TetrisGame/images/'
        self.newgame_img = None
    #加载"提示游戏开始图片"
    def load_newgame_img(self):
        if not self.newgame_img:
            self.newgame_img = pygame.image.load\
                (self.img_path + "press-newgame.jpg").convert_alpha()
        return  self.newgame_img