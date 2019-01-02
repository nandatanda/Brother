import graphics
import characters
import time

window = graphics.GraphWin('Bröther', 525, 700)
moth = characters.Moth(100, 400)

moth.draw(window)
run = True
while run:
    click = window.checkMouse()
    moth.update(window, click)
    time.sleep(.05)