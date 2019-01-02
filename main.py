import graphics
import characters
import time

window = graphics.GraphWin('Bröther', 525, 700)
moth = characters.Moth(window)

moth.draw(window)
window.getMouse()   # menu will go here, approximately

run = True
while run:
    click = window.checkMouse()
    moth.update(window, click)
    time.sleep(.05)