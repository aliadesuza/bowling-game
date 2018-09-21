from BowlingGame import Game
import unittest

class BowlingGameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def rollMany(self, n, pins):
        for i in range(n):
            self.game.roll(pins)

    def test_guttergame(self):
        for i in range(20):
            self.game.roll(0)
        
        assert self.game.getScore() == 0

    def test_all_ones(self):
        for i in range(20):
            self.game.roll(1)
        
        assert self.game.getScore() == 20

    def test_roll_many(self):
        self.rollMany(20, 1)
        assert self.game.getScore() == 20
    
    def test_one_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(17,0)
        assert 13 == self.game.getScore()

if __name__ == '__main__':
    unittest.main()