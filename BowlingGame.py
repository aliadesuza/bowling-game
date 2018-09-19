class Game():
    
    
    score = 0

    def roll(self, pins):
        self.score += pins

    #called at the end of the game and returns total score
    def getScore(self):
        return self.score