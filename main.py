from attributes import GAME_ATTR
from attributes import COLORS
from attributes import GRID
from shapes import ShapeBase
from typing import Optional, List
import pygame
import sys
import random


class Game:
    row_fixed_colors: dict[int, List[Optional[COLORS]]] = {}
    moving_obj: Optional[ShapeBase]
    _wait_ticks_counter: int = 0

    def __init__(self):
        pygame.init()
        self.bg = pygame.display.set_mode((GAME_ATTR.WIDTH, GAME_ATTR.HEIGHT))
        self.fps = pygame.time.Clock()
        self.moving_obj = None

        for i in range(GAME_ATTR.NUM_ROW):
            self.row_fixed_colors[i] = [None] * GAME_ATTR.NUM_COL

    def is_cause_out_of_boundary(self, shape_pos, x_offset=0, y_offset=0):
        for x, y in shape_pos:
            x = x + x_offset
            y = y + y_offset
            if (x < 0 or x >= GAME_ATTR.NUM_ROW or y < 0 or y >= GAME_ATTR.NUM_COL):
                return True
        return False

    def is_cause_collision(self, shape_pos, x_offset=0, y_offset=0):
        return any(self.row_fixed_colors[x + x_offset][y + y_offset] is not None for x, y in shape_pos)

    def _index_to_pos(self, row: int, col: int):
        return col * GAME_ATTR.BLOCK_SIZE, row * GAME_ATTR.BLOCK_SIZE

    def draw_blocks(self):
        # 如果有下降物體
        if self.moving_obj is not None:
            for _x, _y in self.moving_obj.current_shape_pos:
                _x, _y = self._index_to_pos(_x, _y)

                # 畫背景顏色
                pygame.draw.rect(self.bg, self.moving_obj.color, pygame.Rect(
                    _x, _y, GAME_ATTR.BLOCK_SIZE, GAME_ATTR.BLOCK_SIZE))

        # 畫靜止方塊
        for i in range(GAME_ATTR.NUM_ROW):
            for j in range(GAME_ATTR.NUM_COL):
                if self.row_fixed_colors[i][j]:
                    x, y = self._index_to_pos(i, j)

                    # 畫背景顏色
                    pygame.draw.rect(self.bg, self.row_fixed_colors[i][j], pygame.Rect(
                        x, y, GAME_ATTR.BLOCK_SIZE, GAME_ATTR.BLOCK_SIZE))

    def draw_grid(self):
        for i in range(GAME_ATTR.NUM_ROW):
            for j in range(GAME_ATTR.NUM_COL):
                x, y = self._index_to_pos(i, j)

                # 畫邊界顏色
                pygame.draw.rect(self.bg, GRID.COLOR, pygame.Rect(
                    x, y, GAME_ATTR.BLOCK_SIZE, GAME_ATTR.BLOCK_SIZE), GRID.WIDTH)

    def move(self):
        # 是否碰撞 or 是否越界
        if self.is_cause_out_of_boundary(self.moving_obj.current_shape_pos, x_offset=1) or self.is_cause_collision(self.moving_obj.current_shape_pos, x_offset=1):
            self.moving_obj.fixed = True

            # 將固定的物件的位置跟顏色存起來
            for x, y in self.moving_obj.current_shape_pos:
                self.row_fixed_colors[x][y] = self.moving_obj.color
            self.moving_obj = None
        else:
            # 往下移動一格
            self.moving_obj.x_offset += 1

    def get_next_block(self):
        return random.choice(ShapeBase.__subclasses__())()

    def start(self):
        while True:
            # 設定FPS
            self.fps.tick(GAME_ATTR.TICK)

            # 畫背景黑色
            self.bg.fill(COLORS.BLACK)

            # 如果沒有正在下降的方塊 => 隨機產生新方塊
            if self.moving_obj is None:
                self.moving_obj = self.get_next_block()

            # 讀取使用者指令
            for event in pygame.event.get():
                # 關閉視窗
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # 使用者按下按鈕
                if event.type == pygame.KEYDOWN:
                    # 按下左
                    if event.key == pygame.K_LEFT and \
                            not self.is_cause_out_of_boundary(self.moving_obj.current_shape_pos, y_offset=-1) and \
                            not self.is_cause_collision(self.moving_obj.current_shape_pos, y_offset=-1):
                        self.moving_obj.y_offset -= 1
                    # 按下右
                    if event.key == pygame.K_RIGHT and \
                            not self.is_cause_out_of_boundary(self.moving_obj.current_shape_pos, y_offset=1) and \
                            not self.is_cause_collision(self.moving_obj.current_shape_pos, y_offset=1):
                        self.moving_obj.y_offset += 1
                    # 按下space, 旋轉方塊
                    if event.key == pygame.K_SPACE:
                        # 如果超出邊界或碰撞 就不能轉
                        if not self.is_cause_out_of_boundary(self.moving_obj.next_shape_pos) and \
                                not self.is_cause_collision(self.moving_obj.next_shape_pos):
                            self.moving_obj.twist()
                # TODO: 迅速往下

            # 移動方塊
            self._wait_ticks_counter += 1
            if self._wait_ticks_counter >= GAME_ATTR.WAITING_THRESHOLD:
                self.move()
                self._wait_ticks_counter = 0

            # 檢查有幾條要刪除
            i = GAME_ATTR.NUM_ROW
            for j in range(GAME_ATTR.NUM_ROW - 1, -1, -1):
                if any(color is None for color in self.row_fixed_colors[j]):
                    i -= 1
                self.row_fixed_colors[i] = self.row_fixed_colors[j]

            # 把剩下的清空
            while i > 0:
                self.row_fixed_colors[i] = [None] * GAME_ATTR.NUM_COL
                i -= 1

            # 畫所有方塊
            self.draw_blocks()

            # 畫背景網格
            self.draw_grid()

            # 更新畫面
            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.start()
