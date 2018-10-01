class Game():
    
    def __init__(self):
        self.rolls = []
        self.score = 0
        self.currRoll = 0

    def roll(self, pins):
        # self.rolls[self.currRoll] = pins
        # self.currRoll += 1
        self.rolls.append(pins)

    #called at the end of the game and returns total score
    def getScore(self):
        self.score = 0
        for i in range(len(self.rolls)):
            self.score += self.rolls[i]
            # if len(self.rolls) < i + 1 or len(self.rolls) < i + 2:
            if self.rolls[i] + self.rolls[i+1] == 10:
                   self.score += self.rolls[i+2]        
        return self.score