class Game():
    
    
    score = 0
    rolls = [0] * 21
    currRoll = 0

    def roll(self, pins):
        self.score += pins
        self.rolls[++self.currRoll] = pins

    #called at the end of the game and returns total score
    def getScore(self):
        self.score = 0
        for i in self.rolls:
            self.score += self.rolls[i]
        return self.score