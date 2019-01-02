import graphics
import os

class MainUI():
    def __init__(self,window):
        self.width = window.width
        self.height = window.height
        self.isScoreButtonPressed = False

        self.mainBackground = graphics.Image(graphics.Point(self.width/2,self.height/2),'assets/backgrounds/backgroundGame.png')
        self.title = graphics.Image(graphics.Point(self.width/2,self.height/2 - 200),'assets/UI/title.png')
        self.playBtn = graphics.Image(graphics.Point(self.width/2,self.height/2),'assets/UI/buttons/playBtn.png') 
        self.highScoreBtn = graphics.Image(graphics.Point(self.width/2,self.height/2+100),'assets/UI/buttons/highscoreBtn.png')
        self.quitBtn = graphics.Image(graphics.Point(self.width/2,self.height/2 + 200),'assets/UI/buttons/quitBtn.png')
        self.highScoreBoard = graphics.Image(graphics.Point(self.width/2,self.height/2+100),'assets/backgrounds/backgroundHighscore.png')
        self.scoreTxt = graphics.Text(graphics.Point(self.width/2,self.height/2+100),'')

        self.buttonWidth = self.playBtn.getWidth()/2
        self.buttonHeight = self.playBtn.getHeight()/2
        self.playBtnCenter = self.playBtn.getAnchor()
        self.highscoreBtnCenter = self.highScoreBtn.getAnchor()
        self.quitBtnCenter = self.quitBtn.getAnchor()

    def draw(self,window):
        self.title.draw(window)
        self.playBtn.draw(window)
        self.highScoreBtn.draw(window)
        self.quitBtn.draw(window)
        if self.isScoreButtonPressed:
            self.highScoreBoard.draw(window)
            self.scoreTxt.setFill(graphics.color_rgb(255, 0, 128))
            self.scoreTxt.setSize(36)
            self.scoreTxt.draw(window)
        return
    
    def undraw(self):
        self.title.undraw()
        self.playBtn.undraw()
        self.highScoreBtn.undraw()
        self.quitBtn.undraw()
        self.highScoreBoard.undraw()
        self.scoreTxt.undraw()
        return
    
    def returnButton(self, window, mouse):
        playAbsX = abs(self.playBtnCenter.x - mouse.x)
        playAbsY = abs(self.playBtnCenter.y - mouse.y)

        highScoreAbsX = abs(self.highscoreBtnCenter.x - mouse.x)
        highScoreAbsY = abs(self.highscoreBtnCenter.y - mouse.y)

        quitAbsX = abs(self.quitBtnCenter.x - mouse.x)
        quitAbsY = abs(self.quitBtnCenter.y - mouse.y)

        if playAbsX <= self.buttonWidth and playAbsY <= self.buttonHeight:
            return 'play'
        elif highScoreAbsX <= self.buttonWidth and highScoreAbsY <= self.buttonHeight:
            self.isScoreButtonPressed = True
            self.getScore()
            return 'score'
        elif quitAbsX <= self.buttonWidth and quitAbsY <= self.buttonHeight:
            quit()
    
    def getScore(self):
        scores = []
        if os.path.isfile('HighScore.txt'):
            self.scoreFile = open('HighScore.txt', 'r')
            for i in self.scoreFile:
                dataline = i.split('\t')
                datalineNum = dataline[1]
                num = datalineNum.split('\n')
                number = int(num[0])

                scores.append(number)

            myHighscore = (max(scores))
            myHighscore = str(myHighscore)
            self.scoreFile.close()
            self.scoreTxt.setText(myHighscore)
            print('highscore.txt exists! Hightscore: ' + myHighscore)
        else:
            self.scoreFile = open('HighScore.txt', 'a')
            self.scoreFile.write('Score' + '\t' + str(0) + '\n')
            self.scoreFile.close()
            self.scoreTxt.setText(0)
            print('no highscore.txt, i just created new!')
        return

    def display_main_menu(self, window):
        self.mainBackground.draw(window)
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
            else:
                self.isScoreButtonPressed = False
                self.undraw()
                self.draw(window)
        return
