#print("hello world!")
import sys
import  pygame
import  random
import  time
from settings import *
from piece import Piece
from gamewall import GameWall
from gamedisplay import GameDisplay
from gamestate import GameState
from  gameresource import GameResource

def main():
    pygame.init()#初始化
    #创建屏幕对象
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("俄罗斯方块")
    pygame.key.set_repeat(10,100)   #按下按键超过10ms触发下一次按键
    bg_color = BG_COLOR
    #建立方块对象
    #piece = Piece('J',screen)
    random.seed(int(time.time()))   #产生不同的随机序列

    #定义一个二维数组，且全部初始化为'_'
    #game_wall = GameWall(screen)
    # random.choice(range)在范围内随机选取一个作为返回值
    #piece = Piece(random.choice(PIECE_TYPES), screen,game_wall)
    game_state = GameState(screen)
    game_resource = GameResource()

    #pygame.event.get():从事件队列中取出所有事件对象，
    #得到待处理事件列表
    while True:
        #当前方块触底
        if game_state.piece and game_state.piece.is_on_botton:
            #将当前方块标记为wall
            game_state.wall.add_to_wall(game_state.piece)
            game_state.add_score(game_state.wall.eliminate_lines())


            #生成新的方块在游戏区域最上
            #piece = Piece(random.choice(PIECE_TYPES),screen,game_state.wall)
            game_state.piece = Piece(random.choice(PIECE_TYPES),screen,
                                     game_state.wall)
        #监视键盘和鼠标事件
        check_events(game_state.piece)

        #填充屏幕背景颜色
        screen.fill(bg_color)
        #绘制游戏区域
        GameDisplay.draw_game_area(screen,game_state,game_resource)
        #绘制小方块
        #draw_cell(screen,GAME_AREA_LEFT+GAME_AREA_WIDTH//2,GAME_AREA_TOP)
        if game_state.piece:
            game_state.piece.paint()
        #让最近绘制的屏幕可见
        pygame.display.flip()

def check_events(game_state):
    '''捕捉和处理键盘按键事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            on_key_down(event,game_state)
        elif event.type == pygame.USEREVENT:
            game_state.piece.move_down()

def on_key_down(event,game_state):
    if event.key == pygame.K_DOWN:
        print("向下方向键被按下")
        if game_state.piece:
            game_state.piece.move_down()
    elif event.key == pygame.K_UP:
        print("向上方向键被按下")
        if game_state.piece:
            game_state.piece.turn()
    elif event.key == pygame.K_RIGHT:
        print("向右方向键被按下")
        if game_state.piece:
            game_state.piece.move_right()
    elif event.key == pygame.K_LEFT:
        print("向左方向键被按下")
        if game_state.piece:
            game_state.piece.move_left()
    elif event.key == pygame.K_f:
        if game_state.piece:
            game_state.piece.fall_down()
    elif event.key == pygame.K_s and game_state.stopped:
        game_state.start_game()

main()
