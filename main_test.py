import unittest
from parameterized import parameterized
import main
import attributes

GAME_ATTR = attributes.GAME_ATTR


class MainTest(unittest.TestCase):
    @parameterized.expand(
        [
            [[[0, 0]], 0, 0, False],
            [[[5, 5]], 1, 1, False],
            [[[5, 5]], -1, -1, False],
            [[[0, 0]], GAME_ATTR.NUM_ROW, GAME_ATTR.NUM_COL, True],
            [[[GAME_ATTR.NUM_ROW, 0]], 0, 0, True],
            [[[0, GAME_ATTR.NUM_COL]], 0, 0, True],
            [[[GAME_ATTR.NUM_ROW, GAME_ATTR.NUM_COL]], 0, 0, True],
        ]
    )
    def test_is_cause_out_of_boundary(
        self,
        shape_pos: list[list[int]],
        x_offset: int,
        y_offset: int,
        expected_result: bool,
    ):
        class MockGame(main.Game):
            def __init__(self):
                pass

        game = MockGame()
        self.assertEqual(
            game.is_cause_out_of_boundary(shape_pos, x_offset, y_offset),
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
