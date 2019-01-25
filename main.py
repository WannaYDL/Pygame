#print("hello world!")
import sys
import  pygame
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
CELL_WIDTH = 40
GAME_AREA_WIDTH = CELL_WIDTH*10
GAME_AREA_HEIGTH = CELL_WIDTH*20
GAME_AREA_LEFT = (SCREEN_WIDTH-GAME_AREA_WIDTH)//2
GAME_AREA_TOP = SCREEN_HEIGHT-GAME_AREA_HEIGTH
EDGE_COLOR = (0,0,0)
CELL_COLOR = (100,100,100)
BG_COLOR = (200,200,200)

def main():
    #初始化pygame。启用Pygame必不可少的一步，在程序开始阶段执行
    pygame.init()
    # 创建屏幕对象（也即窗口对象）
    scree = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)#分辨率是1200*900
    pygame.display.set_caption("俄罗斯方块") #设置窗口标题
    #设置屏幕背景颜色
    bg_color = BG_COLOR
    #游戏主循环
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #关闭窗口的事件
                sys.exit() #退出程序
            screen.fill(bg_color)
            #绘制直线
            draw_area(screen)
            #刷新屏幕
            pygame.display.flip()
def draw_area(screen):
    '''绘制游戏区域'''
    pygame.draw.line(screen,EDGE_COLOR,)

main()