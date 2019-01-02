import graphics
import os

class MainUI():
    def __init__(self,window):
        self.width = window.width
        self.height = window.height
        self.isPlayButtonPressed = False
        self.isScoreButtonPressed = False
        self.isDisplayingScores = False

        # menu ui
        self.titleImage = graphics.Image(graphics.Point(self.width/2,self.height/2 - 200),'assets/UI/title.png')
        self.backgroundImage = graphics.Image(graphics.Point(self.width/2,self.height/2),'assets/backgrounds/backgroundGame.png')
        self.highScoresBackgroundImage = graphics.Image(graphics.Point(self.width/2,self.height/2+100),'assets/backgrounds/backgroundHighscore.png')
        self.highScoresText = graphics.Text(graphics.Point(self.width/2,self.height/2+100),'')

        self.playButton = graphics.Image(graphics.Point(self.width/2,self.height/2),'assets/UI/buttons/playBtn.png') 
        self.highScoresButton = graphics.Image(graphics.Point(self.width/2,self.height/2+100),'assets/UI/buttons/highscoreBtn.png')
        self.quitButton = graphics.Image(graphics.Point(self.width/2,self.height/2 + 200),'assets/UI/buttons/quitBtn.png')

        self.playButtonAnchor = self.playButton.getAnchor()
        self.highScoresButtonCenter = self.highScoresButton.getAnchor()
        self.quitButtonCenter = self.quitButton.getAnchor()
        self.buttonWidth = self.playButton.getWidth()/2
        self.buttonHeight = self.playButton.getHeight()/2

        # ingame ui
        self.highScoreBanner = graphics.Image(graphics.Point(self.width/2,self.height/self.height+20),'assets/UI/banner.png')
        self.highscoreBannerText = graphics.Text(graphics.Point(self.width/2,self.height/self.height+20),"HIGH SCORE:")
        self.highscoreBannerNumberText = graphics.Text(graphics.Point(self.width/2+100,self.height/self.height+20),'')
        self.currentScoreText = graphics.Text(graphics.Point(self.width/2,self.height/self.height+100),'')


    def draw_menu(self,window):
        self.titleImage.draw(window)
        self.playButton.draw(window)
        self.highScoresButton.draw(window)
        self.quitButton.draw(window)
        return

    def undraw_menu(self):
        self.titleImage.undraw()
        self.playButton.undraw()
        self.highScoresButton.undraw()
        self.quitButton.undraw()
        return

    def draw_scores(self):
        self.highScoresBackgroundImage.draw(window)
        self.highScoresText.setFill(graphics.color_rgb(255, 0, 128))
        self.highScoresText.setSize(36)
        self.highScoresText.draw(window)
        return

    def undraw_scores(self):
        self.highScoresBackgroundImage.undraw()
        self.highS
        return

    def run_menu(self, window):
        self.backgroundImage.draw(window)
        self.draw_menu(window)
        run = True
        while run:
            click = window.getMouse()
            if self.get_button_press(window, click) == 'play':
                self.getScore()
                self.update_score(20)
                self.undraw_menu()
                self.draw_menu(window)
                run = False
            elif self.get_button_press(window, click) == 'scores':
                self.getScore()
                self.undraw_menu()
                self.draw_menu(window)

        return

    def draw_ingame_ui(self, window):
        self.highScoreBanner.draw(window)
        self.highscoreBannerText.setFill(graphics.color_rgb(255,255,255))
        self.highscoreBannerText.setSize(15)
        self.highscoreBannerText.draw(window)
        self.highscoreBannerNumberText.setFill(graphics.color_rgb(255,255,255))
        self.highscoreBannerNumberText.setSize(20)
        self.highscoreBannerNumberText.draw(window)
        self.currentScoreText.setFill(graphics.color_rgb(255,255,0))
        self.currentScoreText.setSize(36)
        self.currentScoreText.draw(window)
        return
    

    def get_button_press(self, window, mouse):
        dxPlay = abs(self.playButtonAnchor.x - mouse.x)
        dyPlay = abs(self.playButtonAnchor.y - mouse.y)
        dxScores = abs(self.highScoresButtonCenter.x - mouse.x)
        dyScores = abs(self.highScoresButtonCenter.y - mouse.y)
        dxQuit = abs(self.quitButtonCenter.x - mouse.x)
        dyQuit = abs(self.quitButtonCenter.y - mouse.y)

        if self.isDisplayingScores == False:
            if dxPlay <= self.buttonWidth and dyPlay <= self.buttonHeight:
                self.isPlayButtonPressed = True
                return 'play'
            elif dxScores <= self.buttonWidth and dyScores <= self.buttonHeight:
                self.isScoreButtonPressed = True
                return 'scores'
            elif dxQuit <= self.buttonWidth and dyQuit <= self.buttonHeight:
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
            self.highScoresText.setText(myHighscore)
            self.highscoreBannerNumberText.setText(myHighscore)
            print('highscore.txt exists! Hightscore: ' + myHighscore)
        else:
            self.scoreFile = open('HighScore.txt', 'a')
            self.scoreFile.write('scores' + '\t' + str(0) + '\n')
            self.scoreFile.close()
            self.highScoresText.setText(0)
            self.highscoreBannerNumberText.setText(0)
            print('no highscore.txt, i just created new!')
        return
    
    def update_score(self, currentScore):
        self.currentScoreText.setText(currentScore)
        return

