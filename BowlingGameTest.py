from BowlingGame import Game
import unittest

class TestBowlingGame(unittest.TestCase):
    game = Game()

    def setUp(self):
        self.game = Game()

    def test_guttergame(self):
        # for i in range(20):
        #     self.game.rolls(0)
        assert self.game.score == 0