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
    def draw_game_area(screen,game_wall):
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

        GameDisplay.draw_wall(game_wall)

    @staticmethod
    #根据game_wall.area绘制墙体
    def draw_wall(game_wall):
        for r in range(LINE_NUM):
            for c in range(COLUMN_NUM):
                if game_wall.area[r][c] != WALL_BLANK_LABEL:
                    GameDisplay.draw_cell(game_wall.screen,r,c,
                                          PIECE_COLORS[game_wall.area[r][c]])

