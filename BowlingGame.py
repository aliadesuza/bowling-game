class Game():
    
    
    score = 0
    rolls = [0] * 21
    currRoll = 0

    def roll(self, pins):
        self.rolls[self.currRoll] = pins
        self.currRoll += 1

    #called at the end of the game and returns total score
    def getScore(self):
        self.score = 0
        for i in self.rolls:
            self.score += self.rolls[i]
            if self.rolls[i] + self.rolls[i+1] == 10:
                self.score += self.rolls[i+2]        
        return self.score