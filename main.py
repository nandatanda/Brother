import graphics
import characters
import gui
import time

window = graphics.GraphWin('Bröther', 525, 700)
moth = characters.Moth(window)
ui = gui.MainUI(window)

moth.draw(window)
ui.display_main_menu(window)

run = True
while run:
    click = window.checkMouse()
    moth.update(window, click)
    time.sleep(.05)