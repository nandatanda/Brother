import graphics
from random import randint

class Stalagtite():
    def __init__(self, window):
        self.x = window.getWidth()
        self.y = 0
        self.velocity = 10
        self.image = graphics.Image(graphics.Point(self.x, self.y), 'assets/obstacles/stalagtite01.gif')
        self.width = self.image.getWidth()
        self.height = self.image.getHeight()
        self.x += self.width / 2
        self.randomize()

    def update(self, window, player):
        self.undraw()
        self.move()
        self.draw(window)

    def undraw(self):
        self.image.undraw()
        return

    def randomize(self):
        self.velocity = randint(5, 10)
        self.y += randint(-self.height / 4, self.height / 2)

    def draw(self, window):
        self.image = graphics.Image(graphics.Point(self.x, self.y), 'assets/obstacles/stalagtite01.gif')
        self.image.draw(window)
        return

    def move(self):
        self.x -= self.velocity
        return


class Stalagmite():
    def __init__(self, window):
        self.x = window.getWidth()
        self.y = window.getHeight()
        self.velocity = 10
        self.image = graphics.Image(graphics.Point(self.x, self.y), 'assets/obstacles/stalagmite01.gif')
        self.width = self.image.getWidth()
        self.height = self.image.getHeight()
        self.x += self.width / 2
        self.randomize()

    def update(self, window, player):
        self.undraw()
        self.move()
        self.draw(window)

    def undraw(self):
        self.image.undraw()
        return

    def randomize(self):
        self.velocity = randint(5, 10)
        self.y += randint(-self.height / 2, self.height / 4)

    def draw(self, window):
        self.image = graphics.Image(graphics.Point(self.x, self.y), 'assets/obstacles/stalagmite01.gif')
        self.image.draw(window)
        return

    def move(self):
        self.x -= self.velocity
        return