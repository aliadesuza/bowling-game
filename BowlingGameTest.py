from BowlingGame import Game
import unittest

class BowlingGameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.longMessage = True

    def rollMany(self, n, pins):
        for i in range(n):
            self.game.roll(pins)

    def test_guttergame(self):
        for i in range(20):
            self.game.roll(0)
        expectedScore = 0
        self.assertEqual(expectedScore, self.game.getScore(), 'incorrect score')

    def test_all_ones(self):
        self.rollMany(20, 1)
        expectedScore = 20
        self.assertEqual(expectedScore, self.game.getScore(), 'incorrect score')

    # # def test_roll_many(self):
    # #     self.rollMany(19, 1)
    # #     expectedScore = 20
    # #     self.assertEqual(expectedScore, self.game.getScore(), 'incorrect score')
    
    def test_one_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(17,0)
        expectedScore = 16
        self.assertEqual(expectedScore, self.game.getScore(), 'incorrect score')

if __name__ == '__main__':
    unittest.main()
