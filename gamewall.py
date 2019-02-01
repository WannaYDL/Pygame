#TetrisGame/gamewall.py

from  settings import*
from  gamedisplay import GameDisplay

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

    # 打印15*10的二维矩阵self.area的元素值，用于调试
    # def print(self):
    #     print(len(self.area),"rows",len(self.area[0],"colums"))
    #     for line in self.area:
    #         print(line)

    #垒墙函数，将当前方块piece砌到墙体内
    def add_to_wall(self,piece):
        shape_turn = PIECES[piece.shape][piece.turn_times]
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    #将当前位置按当前piece.shape的形状标记
                    self.set_cell(piece.y+r,piece.x+c,piece.shape)
                    #print(piece.shape)

    #绘制当前小方格
    #把第r行第c列的方格打上记号
    def set_cell(self,row , column,shape_label):
        #c,r=position;       #position的第一个元素赋值给c，第二个元素赋值给r
        self.area[row][column] = shape_label   #在area这个二维数组中的(r,c) 位置的'_'改为该方块的形状如's'

    #判断该位置是否有之前的方块
    def is_wall(self,row,column):
        return  self.area[row][column] != WALL_BLANK_LABEL

    #消行，若该行没有空白单元格就消掉该行。返回得分
    #0行0分；1行100分；2行200分；3行400分；4行800分
    def eliminate_lines(self):
        #需要消哪几行，将行号存入lines_eliminated列表
        lines_eliminated = []
        for r in range(LINE_NUM):
            if self.is_full(r):
                lines_eliminated.append(r)

        #消行，更新墙体矩阵
        for r in lines_eliminated:
            self.copy_down(r)       #消行，上面的各行依次下沉一行
            for c in range(COLUMN_NUM):
                self.area[0][c] = WALL_BLANK_LABEL

         #根据消行数，计算得分
        eliminated_numb = len(lines_eliminated)
        #用以检查某一条件是否为True，
        # 若该条件为False则会给出一个AssertionError
        assert(eliminated_numb <= 4 and eliminated_numb >=0)

        if eliminated_numb < 3:
            score = eliminated_numb*100
        elif eliminated_numb ==3:
            score = 400
        else:
            score = 800

        return  score

    #判断row行是否为满
    def is_full(self,row):
        for c in range(COLUMN_NUM):
            if self.area[row][c] == WALL_BLANK_LABEL:
                return False
        return True

    #将第r行上面的各行从下到上依次下沉一行
    def copy_down(self,row):
        #range(start, stop[, step])
        for r in range(row,0,-1):
            for c in range(COLUMN_NUM):
                self.area[r][c] = self.area[r-1][c]


