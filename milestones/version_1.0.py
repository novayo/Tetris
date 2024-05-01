import pygame
import sys
import random

########################################################################
############################## Pygame 資源 ##############################
########################################################################
pygame.init()  # pygame一定要寫的
FPS = pygame.time.Clock()
background = pygame.display.set_mode((360, 720))  # 建立背景


########################################################################
############################### 遊戲 資源 ###############################
########################################################################
rect_width = 360 // 12  # row 12格
moving_rect = None  # [x, y]
moving_rect_color = (0, 0, 0)  # (r, g, b)
fixed_rects_set = set()  # [i, j]
fixed_rects_color_mapping_dict = {}

# 產生 index 對應座標
index_mapping = {}
for i in range(360 // rect_width):
    for j in range(720 // rect_width):
        index_mapping[i, j] = (rect_width * i, rect_width * j)


########################################################################
################################# 函數 ##################################
########################################################################
def move_or_generate_rect():
    global moving_rect, moving_rect_color

    if moving_rect is None:
        moving_rect = [4, 0]
        moving_rect_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        return

    # 如果下一格 到底了or有方塊 就停下來
    next_pos = (moving_rect[0], moving_rect[1] + 1)
    if next_pos not in index_mapping or next_pos in fixed_rects_set:
        # 將移動物體變成停止物體
        fixed_rects_set.add((moving_rect[0], moving_rect[1]))
        fixed_rects_color_mapping_dict[moving_rect[0], moving_rect[1]] = (
            moving_rect_color
        )
        moving_rect = moving_rect_color = None

        # 判斷是否要消除一行（因為只有物體，所以只需判斷一行）
        for j in range(720 // rect_width - 1, -1, -1):
            # 判斷是否要消除一行
            is_all_blocks = True
            for i in range(360 // rect_width):
                if (i, j) not in fixed_rects_set:
                    is_all_blocks = False
                    break

            # 如果有，則要刪除這行 並 讓上面的物體都往下一格
            if is_all_blocks:
                # 刪除這行
                for i in range(360 // rect_width):
                    fixed_rects_set.remove((i, j))
                    del fixed_rects_color_mapping_dict[i, j]
                # 讓上面的物體都往下一格
                for _j in range(j - 1, -1, -1):
                    for i in range(360 // rect_width):
                        if (i, _j) in fixed_rects_set:
                            fixed_rects_set.add((i, _j + 1))
                            fixed_rects_set.remove((i, _j))
                            fixed_rects_color_mapping_dict[i, _j + 1] = (
                                fixed_rects_color_mapping_dict[i, _j]
                            )
                            del fixed_rects_color_mapping_dict[i, _j]
                break
        return

    # 移動方塊
    moving_rect[1] += 1


def draw_rect():
    global moving_rect_color
    # 畫移動中的方塊
    if moving_rect is not None:
        x, y = index_mapping[moving_rect[0], moving_rect[1]]
        r, g, b = moving_rect_color
        pygame.draw.rect(
            background, (r, g, b), pygame.Rect(x, y, rect_width, rect_width)
        )  # 畫正方形 實心白色

    # 畫非移動中的方塊
    for i, j in fixed_rects_set:
        x, y = index_mapping[i, j]
        r, g, b = fixed_rects_color_mapping_dict[i, j]
        pygame.draw.rect(
            background, (r, g, b), pygame.Rect(x, y, rect_width, rect_width)
        )  # 畫正方形 實心白色


def move_left():
    if moving_rect is None:
        return
    moving_rect[0] = max(moving_rect[0] - 1, 0)


def move_right():
    if moving_rect is None:
        return
    moving_rect[0] = min(moving_rect[0] + 1, 11)


########################################################################
################################# 本體 ##################################
########################################################################
delay = 0
while True:
    FPS.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 如果點視窗的叉叉
            pygame.quit()  # 離開pygame
            sys.exit()  # 關閉程式
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left()
            elif event.key == pygame.K_RIGHT:
                move_right()

    delay += 1
    background.fill((0, 0, 0))  # 畫背景 黑色
    # 每秒一次
    if delay >= 3:
        move_or_generate_rect()
        delay = 0
    draw_rect()
    pygame.display.flip()  # 更新畫面
