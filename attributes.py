from dataclasses import dataclass


@dataclass
class COLORS:
    WHITE: tuple = (255, 255, 255)
    BLACK: tuple = (0, 0, 0)
    GRAY: tuple = (31, 31, 31)
    RED: tuple = (225, 49, 34)
    ORANGE: tuple = (240, 147, 54)
    YELLOW: tuple = (251, 255, 83)
    GREEN: tuple = (125, 183, 66)
    BLUE: tuple = (104, 224, 251)
    PURPLE: tuple = (145, 28, 145)
    PINK: tuple = (236, 94, 184)


@dataclass
class GRID:
    WIDTH: int = 1
    COLOR: int = COLORS.WHITE


@dataclass
class GAME_ATTR:
    HEIGHT: int = 800
    WIDTH: int = HEIGHT // 2
    TICK: int = 60
    NUM_ROW: int = 20
    NUM_COL: int = 10
    BLOCK_SIZE: int = WIDTH // NUM_COL
    SPEED: int = 3
    WAITING_THRESHOLD: float = TICK / SPEED
