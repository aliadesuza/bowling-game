from BowlingGame import Game
import unittest

class TestBowlingGame(unittest.TestCase):
    game = Game()

    def setUp(self):
        self.game = Game()

    def testGutterGame():
        for i in range(20):
            game.roll(0)
        assert game.score == 0