class Player(object):

    def __init__ (self, name):
        self.name = name
        self._lives = 3
        self.level = 1
        self.score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self,lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("lives can not be negative")
            self.lives = 0
    
    lives = property(_get_lives, _set_lives)

    def __str__(self):
        return "Name: {0.name}, lives: {0.lives}, level: {0.level}, Score{0.score}".format(self)
    