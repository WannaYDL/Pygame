'''
    TetrisGame/gamewall.py
'''
from  settings import*
#游戏区墙体类，记住落到底部的方块组成的‘墙’
class GameWall():
    # 游戏开始时，区域15*10的格子被符号‘—’填充，‘墙’是空的
    def __init__(self,screen):
        self.screen = screen
        self.area = [ ]
        line = [WALL_BLANK_LABEL] * COLUMN_NUM
        #append() 方法用于在列表末尾添加新的对象
        #extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表
        for i in range(LINE_NUM):
            #在are空列表后添加列表line
            #line[:]截取整个line列表
            self.area.append(line[:])

    #打印15*10的二维矩阵self.area的元素值，用于调试
    def print(self):
        print(len(self.area),"rows",len(self.area[0],"colums"))
        for line in self.area:
            print(line)

    #垒墙函数，将当前方块piece砌到墙体内
    def add_to_wall(self,piece):
        shape_turn = PIECES[piece.shape][piece.turn_times]
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    #将当前位置按当前piece.shape的形状标记
                    self.set_cell((piece.x+c,piece.y+r),piece.shape)

    #绘制当前小方格
    #把第r行第c列的方格打上记号
    def set_cell(self,position,shape_label):
        c,r=position;
        self.area[r][c] = shape_label

