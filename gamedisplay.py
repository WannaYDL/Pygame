#TetrisGame/display.py
from  settings import *
import  pygame

class GameDisplay():
    @staticmethod
    def draw_cell(screen,row,column,color):
        #在row行colum列的格子里填充color颜色
        cell_position = (column*CELL_WIDTH+GAME_AREA_LEFT + 1,
                         row*CELL_WIDTH+GAME_AREA_TOP + 1)

        cell_width_height = (CELL_WIDTH - 2,CELL_WIDTH - 2)
        cell_rect = pygame.Rect(cell_position,cell_width_height)
        pygame.draw.rect(screen,color,cell_rect)

    @staticmethod
    def draw_game_area(screen,game_state,game_resource):
        '''
        # 原型：pygame.draw.line(Surface, color, start_pos, end_pos, width=1): return Rect
        # 用途：绘制直线段，start_pos 和 end_pos 分别表示起始点和终止点，用坐标表示。
        # width为线条宽度，默认为1. 线条两端自然结束，没有明显的端点（如实心黑点
        # 绘制顶部边界
        pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP),
                         (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP))
        # 绘制底部边界
        pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP + 15 * CELL_WIDTH),
                         (GAME_AREA_LEFT + 10 * CELL_WIDTH, GAME_AREA_TOP + 15 * CELL_WIDTH))
        # 绘制左侧边界
        pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP),
                         (GAME_AREA_LEFT, GAME_AREA_TOP + 15 * CELL_WIDTH))
        # 绘制右侧边界线
        pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP),
                         (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP + GAME_AREA_HEIGHT))
        '''
        # 绘制网格
        for num in range(16):
            pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP + num * CELL_WIDTH),
                             (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP + num * CELL_WIDTH))
        for num in range(11):
            pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT + num * CELL_WIDTH, GAME_AREA_TOP),
                             (GAME_AREA_LEFT + num * CELL_WIDTH, GAME_AREA_TOP + GAME_AREA_HEIGHT))

        GameDisplay.draw_wall(game_state.wall)
        GameDisplay.draw_score(screen,game_state.game_score)
        if game_state.stopped:
            GameDisplay.draw_start_prompt(screen,game_resource)



    @staticmethod
    #根据game_wall.area绘制墙体
    def draw_wall(game_wall):
        for r in range(LINE_NUM):
            for c in range(COLUMN_NUM):
                if game_wall.area[r][c] != WALL_BLANK_LABEL:
                    GameDisplay.draw_cell(game_wall.screen,r,c,
                                          PIECE_COLORS[game_wall.area[r][c]])

    @staticmethod
    #绘制游戏得分
    def draw_score(screen,score):
        # 换成'arial',无法显示中文
        #‘simhei’即黑体，SysFont():生成一个字体对象，参数一为字体，参数二为字体大小
        score_label_font = pygame.font.SysFont('simhei',28)
        #调用render()函数生成图元对象，render 方法的第一个参数指定要绘制的文字,单引号前面的
        # u 字母表示这是 Unicode 型字符串。字符串内有中文的话,建议你用 u 字母标示出来。
        # 第二个参数是指是否启用反显效果。False 是指不启用。第三个参数是指文字的颜色。
        # SCORE_LABEL_COLOR 常量定义为 (0, 0, 0) ,即黑色
        score_label_surface = score_label_font.render('Score:',False,SCORE_LABEL_COLOR)
        #设定显示位置

        score_label_position = (GAME_AREA_LEFT + COLUMN_NUM *
                                CELL_WIDTH + 40,GAME_AREA_TOP)
        #显示文字图元
        screen.blit(score_label_surface,score_label_position)
        #显示分数
        score_font = pygame.font.SysFont('simhei',36)
        score_surface = score_font.render(str(score),False,SCORE_COLOR)
        score_label_width = score_label_surface.get_width()
        score_position = (score_label_position[0]
                          + score_label_width + 20,score_label_position[1])
        screen.blit(score_surface,score_position)

    @staticmethod
    def draw_start_prompt(screen,game_resource):
        start_tip_position = (GAME_AREA_LEFT + 2 *
                              CELL_WIDTH,GAME_AREA_TOP + 10*CELL_WIDTH)
        screen.blit(game_resource.load_newgame_img(),start_tip_position)




