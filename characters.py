import graphics

class Moth():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.path = 'assets/moth.gif'
        self.image = graphics.Image(graphics.Point(self.x, self.y), self.path)
        self.framesSinceFlap = 0

    def update(self, window, click):
        self.listen(click)
        self.undraw()
        self.accelerate()
        self.move()
        self.draw(window)

        self.framesSinceFlap += 1
        return

    def listen(self, click):
        if click:
            self.flap()
        return

    def flap(self):
        self.framesSinceFlap = 0
        self.velocity -= 5
        return

    def undraw(self):
        self.image.undraw()
        return

    def accelerate(self):
        dy = int(self.framesSinceFlap / 3)
        self.velocity += dy
        return

    def move(self):
        self.y += self.velocity
        return

    def draw(self, window):
        self.image = graphics.Image(graphics.Point(self.x, self.y), self.path)
        self.image.draw(window)
        return