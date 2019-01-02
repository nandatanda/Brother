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
obstaclesList.append(obstacles.Stalagmite(window))

moth.draw(window)
for obstacle in obstaclesList:
    obstacle.draw(window)
ui.run_menu(window)
ui.draw_ingame(window)

run = True
while run:
    click = window.checkMouse()
    moth.update(window, click)
    for obstacle in obstaclesList:
        obstacle.update(window, moth)
    ui.update_ingame_score(window)
    ui.update_ingame_banner(window)
    time.sleep(.05)