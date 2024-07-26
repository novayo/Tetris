from typing_extensions import override, List
from attributes import COLORS
from attributes import GAME_ATTR
import random
import pygame


class ShapeBase:
    fixed: bool = False
    idx_shape: int
    x_offset: int = 0
    y_offset: int = GAME_ATTR.NUM_COL // 2 - 1
    is_show_image: bool = False

    def __init__(self, is_show_image):
        self.idx_shape = random.randint(0, len(self.shapes)-1)
        self.is_show_image = is_show_image

    @override
    @property
    def shapes(self) -> List[List[List[int]]]:
        raise NotImplementedError

    @override
    @property
    def color(self) -> COLORS:
        raise NotImplementedError
    
    @property
    def image(self) -> pygame.Surface:
        raise NotImplementedError

    def normalize_image(self, image) -> pygame.Surface:
        return pygame.transform.scale(image, (GAME_ATTR.BLOCK_SIZE, GAME_ATTR.BLOCK_SIZE))

    @property
    def current_shape_pos(self):
        return [[x + self.x_offset, y + self.y_offset] for x, y in self.shapes[self.idx_shape]]
    
    @property
    def next_shape_pos(self):
        idx = self.idx_shape + 1
        if idx >= len(self.shapes):
            idx = 0
        return [[x + self.x_offset, y + self.y_offset] for x, y in self.shapes[idx]]

    def twist(self):
        self.idx_shape += 1
        if self.idx_shape >= len(self.shapes):
            self.idx_shape = 0


class ShapeO(ShapeBase):
    @property
    def shapes(self):
        return [
            [[0, 0], [0, 1], [1, 0], [1, 1]],
        ]

    @property
    def color(self):
        return COLORS.YELLOW

    @override
    @property
    def image(self):
        return self.normalize_image(pygame.image.load('res/amazon.png').convert_alpha())


class ShapeI(ShapeBase):
    @property
    def shapes(self):
        return [
            [[0, 0], [1, 0], [2, 0], [3, 0]],
            [[0, 0], [0, 1], [0, 2], [0, 3]],
        ]

    @property
    def color(self):
        return COLORS.BLUE

    @override
    @property
    def image(self):
        return self.normalize_image(pygame.image.load('res/apple.png').convert_alpha())


class ShapeS(ShapeBase):
    @property
    def shapes(self):
        return [
            [[1, 0], [1, 1], [0, 1], [0, 2]],
            [[0, 0], [1, 0], [1, 1], [2, 1]],
        ]

    @property
    def color(self):
        return COLORS.GREEN

    @override
    @property
    def image(self):
        return self.normalize_image(pygame.image.load('res/facebook.png').convert_alpha())


class ShapeZ(ShapeBase):
    @property
    def shapes(self):
        return [
            [[0, 0], [0, 1], [1, 1], [1, 2]],
            [[0, 1], [1, 1], [1, 0], [2, 0]],
        ]

    @property
    def color(self):
        return COLORS.RED
    
    @override
    @property
    def image(self):
        return self.normalize_image(pygame.image.load('res/google.png').convert_alpha())


class ShapeL(ShapeBase):
    @property
    def shapes(self):
        return [
            [[0, 0], [1, 0], [2, 0], [2, 1]],
            [[1, 0], [0, 0], [0, 1], [0, 2]],
            [[0, 0], [0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [1, 1], [1, 0]],
        ]

    @property
    def color(self):
        return COLORS.ORANGE
    
    @override
    @property
    def image(self):
        return self.normalize_image(pygame.image.load('res/microsoft.png').convert_alpha())


class ShapeJ(ShapeBase):
    @property
    def shapes(self):
        return [
            [[0, 1], [1, 1], [2, 1], [2, 0]],
            [[0, 0], [1, 0], [1, 1], [1, 2]],
            [[0, 1], [0, 0], [1, 0], [2, 0]],
            [[0, 0], [0, 1], [0, 2], [1, 2]],
        ]

    @property
    def color(self):
        return COLORS.PINK
    
    @override
    @property
    def image(self):
        return self.normalize_image(pygame.image.load('res/netflix.png').convert_alpha())


class ShapeT(ShapeBase):
    @property
    def shapes(self):
        return [
            [[0, 1], [1, 0], [1, 1], [1, 2]],
            [[0, 0], [1, 0], [2, 0], [1, 1]],
            [[0, 0], [0, 1], [0, 2], [1, 1]],
            [[0, 1], [1, 1], [2, 1], [1, 0]],
        ]

    @property
    def color(self):
        return COLORS.PURPLE

    @override
    @property
    def image(self):
        return self.normalize_image(pygame.image.load('res/dino.png').convert_alpha())
