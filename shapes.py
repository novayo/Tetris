from typing_extensions import override, List
from attributes import COLORS
from attributes import GAME_ATTR
import random


class ShapeBase:
    fixed: bool = False
    idx_shape: int
    x_offset: int = 0
    y_offset: int = GAME_ATTR.NUM_COL // 2 - 1

    def __init__(self):
        self.idx_shape = random.randint(0, len(self.shapes)-1)

    @override
    @property
    def shapes(self) -> List[List[List[int]]]:
        raise NotImplementedError

    @override
    @property
    def color(self) -> COLORS:
        raise NotImplementedError

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
