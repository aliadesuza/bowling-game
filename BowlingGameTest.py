from BowlingGame import Game
import unittest

class BowlingGameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_guttergame(self):
        for i in range(20):
            self.game.roll(0)
        
        assert self.game.getScore() == 0

    def test_all_ones(self):
        for i in range(20):
            self.game.roll(1)
        
        assert self.game.getScore() == 20

if __name__ == '__main__':
    unittest.main()