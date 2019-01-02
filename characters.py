import graphics

class Moth():
    def __init__(self, window):
        self.x = window.getWidth() / 2
        self.y = window.getHeight() / 2
        self.velocity = 0
        self.speedLimit = 40
        self.inertia = 3
        self.path = 'assets/moth.gif'
        self.image = graphics.Image(graphics.Point(self.x, self.y), self.path)
        self.width = self.image.getWidth()
        self.height = self.image.getHeight()
        self.framesSinceFlap = 0
        self.isAlive = True

    def update(self, window, click):
        self.listen(click)
        self.undraw()
        self.accelerate()
        self.move()
        self.draw(window)

        if self.detect_edges(window):
            self.isAlive = False
            quit()

        self.framesSinceFlap += 1
        return

    def listen(self, click):
        if click:
            self.flap()
        return

    def flap(self):
        self.framesSinceFlap = 0
        self.velocity -= 10
        return

    def undraw(self):
        self.image.undraw()
        return

    def accelerate(self):
        dy = int(self.framesSinceFlap / self.inertia)
        self.velocity += dy
        if self.velocity > self.speedLimit:
            self.velocity = self.speedLimit
        elif self.velocity < -self.speedLimit:
            self.velocity = -self.speedLimit
        return

    def move(self):
        self.y += self.velocity
        return

    def draw(self, window):
        self.image = graphics.Image(graphics.Point(self.x, self.y), self.path)
        self.image.draw(window)
        return

    def detect_edges(self, window):
        minHeight = 50 + (self.height / 2)
        maxHeight = window.height - (self.height / 2)
        if minHeight < self.y < maxHeight:
            return False
        return True