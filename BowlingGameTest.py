from BowlingGame import Game
import unittest

class TestBowlingGame(unittest.TestCase):
    game = Game()

    def setUp(self):
        self.game = Game()

    def testGutterGame():