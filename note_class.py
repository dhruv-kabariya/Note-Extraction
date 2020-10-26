from math import trunc


class Note:

    def __init__(self, note, time, x, y):

        self.note = note
        self.time = time
        self.x = x
        self.y = y
        self.display = True

    def updateX(self):
        self.x -= 0.15
        if(self.x < 0):
            self.display = False
