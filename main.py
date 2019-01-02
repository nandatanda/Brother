import graphics
import characters
import obstacles
import gui
import time

window = graphics.GraphWin('Bröther', 525, 700, autoflush=False)
moth = characters.Moth(window)
ui = gui.MainUI(window)
obstaclesList = list()
obstaclesList.append(obstacles.Stalagtite(window))

moth.draw(window)
for obstacle in obstaclesList:
    obstacle.draw(window)
ui.display_main_menu(window)

run = True
while run:
    click = window.checkMouse()
    moth.update(window, click)
    for obstacle in obstaclesList:
        obstacle.update(window, moth)
    time.sleep(.05)