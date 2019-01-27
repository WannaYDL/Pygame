#print("hello world!")
import sys
import  pygame
from settings import *
from piece import *

def main():
    pygame.init()#初始化
    #创建屏幕对象
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("俄罗斯方块")
    bg_color = BG_COLOR
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #填充屏幕背景颜色
        screen.fill(bg_color)
        #绘制游戏区域
        draw_game_area(screen)
        #绘制小方块
        draw_cell(screen,GAME_AREA_LEFT+GAME_AREA_WIDTH//2,GAME_AREA_TOP)
        pygame.display.flip()
def draw_game_area(screen):
    '''
    原型：pygame.draw.line(Surface, color, start_pos, end_pos, width=1): return Rect
　　用途：绘制直线段，start_pos 和 end_pos 分别表示起始点和终止点，用坐标表示。
        width为线条宽度，默认为1. 线条两端自然结束，没有明显的端点（如实心黑点
    '''
    #绘制顶部边界
    pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT,GAME_AREA_TOP),(GAME_AREA_LEFT+GAME_AREA_WIDTH,GAME_AREA_TOP))
    #绘制底部边界
    pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT,GAME_AREA_TOP+15*CELL_WIDTH),(GAME_AREA_LEFT+10*CELL_WIDTH,GAME_AREA_TOP+15*CELL_WIDTH))
    #绘制左侧边界
    pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT,GAME_AREA_TOP),(GAME_AREA_LEFT,GAME_AREA_TOP+15*CELL_WIDTH))
    #绘制右侧边界线
    pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT+GAME_AREA_WIDTH,GAME_AREA_TOP),(GAME_AREA_LEFT+GAME_AREA_WIDTH,GAME_AREA_TOP+GAME_AREA_HEIGTH))
    #绘制网格
    for num in range(1,15):
        pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT,GAME_AREA_TOP+num*CELL_WIDTH),(GAME_AREA_LEFT+GAME_AREA_WIDTH,GAME_AREA_TOP+num*CELL_WIDTH))
    for num in range(1,10):
        pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT+num*CELL_WIDTH,GAME_AREA_TOP),(GAME_AREA_LEFT+num*CELL_WIDTH,GAME_AREA_TOP+GAME_AREA_HEIGTH))
def draw_cell(screen,left,top):
    '''
    绘制单元格和小方格
    left：单元格离窗口左边界距离，单位是像素
    top ：单元格离窗口上边界的距离
    '''
    cell_left_top = (left,top)                      #小方格左上角坐标点
    cell_width_height = (CELL_WIDTH,CELL_WIDTH)     #小方格的宽度和高度
    #生成由左上坐标和宽度高度生成的矩形
    cell_rect = pygame.Rect(cell_left_top,cell_width_height)
    pygame.draw.rect(screen,CELL_COLOR,cell_rect)   #绘制正方形


main()