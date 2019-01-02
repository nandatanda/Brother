import graphics

class MainUI():
    def __init__(self,window):
        self.width = window.width
        self.height = window.height
        self.bgPos = (graphics.Point(self.width/2,self.height/2))
        self.titlePos = (graphics.Point(self.width/2,self.height/2 - 200))
        self.playBtnPos = (graphics.Point(self.width/2,self.height/2))
        self.hsBtnPos = (graphics.Point(self.width/2,self.height/2 + 100))
        self.quitBtnPos = (graphics.Point(self.width/2,self.height/2 + 200))
        self.highScoreBoardPos = (graphics.Point(self.width/2,self.height/2 + 100))

        self.bgImg = 'assets/backgrounds/backgroundGame.png'
        self.titleImg = 'assets/UI/buttons/playBtn.png'
        self.playImg = 'assets/UI/buttons/playBtn.png'
        self.highScoreImg = 'assets/UI/buttons/highscoreBtn.png'
        self.quitImg = 'assets/UI/buttons/quitBtn.png'
        self.highScoreBoardImg = 'assets/backgrounds/backgroundHighscore.png'

        self.mainBackground = graphics.Image(self.bgPos,self.bgImg)
        #self.title = graphics.Image(self.titlePos,self.titleImg) this will have it's own image etc
        self.playBtn = graphics.Image(self.playBtnPos,self.playImg) 
        self.highScoreBtn = graphics.Image(self.hsBtnPos,self.highScoreImg)
        self.quitBtn = graphics.Image(self.quitBtnPos,self.quitImg)
        self.highScoreBoard = graphics.Image(self.highScoreBoardPos,self.highScoreBoardImg)
        #self.highScoreTitle = graphics.Image(self.highScoreBoardPos,self.image) this will draw HIGHSCORE on top of the highscore board

        self.buttonWidth = self.playBtn.getWidth()/2
        self.buttonHeight = self.playBtn.getHeight()/2
        
        self.playBtnCenter = self.playBtn.getAnchor()
        self.highscoreBtnCenter = self.highScoreBtn.getAnchor()
        self.quitBtnCenter = self.quitBtn.getAnchor()

        self.isScoreButtonPressed = False

    def draw(self,window):
        self.mainBackground.draw(window)
        self.playBtn.draw(window)
        self.highScoreBtn.draw(window)
        self.quitBtn.draw(window)
        if self.isScoreButtonPressed:
            self.highScoreBoard.draw(window)
        return
    
    def undraw(self):
        self.mainBackground.undraw()
        self.playBtn.undraw()
        self.highScoreBtn.undraw()
        self.quitBtn.undraw()
        return
    
    def returnButton(self, window, mouse):
        playAbsX = abs(self.playBtnCenter.x - mouse.x)
        playAbsY = abs(self.playBtnCenter.y - mouse.y)

        highScoreAbsX = abs(self.highscoreBtnCenter.x - mouse.x)
        highScoreAbsY = abs(self.highscoreBtnCenter.y - mouse.y)

        quitAbsX = abs(self.quitBtnCenter.x - mouse.x)
        quitAbsY = abs(self.quitBtnCenter.y - mouse.y)

        if playAbsX <= self.buttonWidth and playAbsY <= self.buttonHeight:
            print('play')
            return 'play'
        elif highScoreAbsX <= self.buttonWidth and highScoreAbsY <= self.buttonHeight:
            self.isScoreButtonPressed = True
            return 'score'
        elif quitAbsX <= self.buttonWidth and quitAbsY <= self.buttonHeight:
            quit()


    def display_main_menu(self, window):
        self.draw(window)
        run = True
        while run:
            click = window.getMouse()
            if self.returnButton(window, click) == 'score':
                self.undraw()
                self.draw(window)
                # do score stuff
                pass
            elif self.returnButton(window, click) == 'play':
                self.undraw()
                run = False
        return
