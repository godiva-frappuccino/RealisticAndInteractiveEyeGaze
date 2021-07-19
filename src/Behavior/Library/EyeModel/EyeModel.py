class Eye:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

    def getEyeAngle(self):
        return self.x, self.y

    def update(self, x=None, y=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
