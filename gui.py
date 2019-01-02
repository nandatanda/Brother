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

    def draw_scores(self, window, score):
        self.titleImage.draw(window)
        self.highScoresBackgroundImage.draw(window)
        self.highScoresText.setFill(graphics.color_rgb(255, 0, 128))
        self.highScoresText.setSize(36)
        self.highScoresText.setText(score)
        self.highScoresText.draw(window)
        return

    def undraw_scores(self):
        self.titleImage.undraw()
        self.highScoresBackgroundImage.undraw()
        self.highScoresText.undraw()
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

    def get_high_score(self):
        with open('HighScore.txt', 'r') as f:
            scores = [int(line.strip()) for line in f]
        return str(max(scores))

    def run_menu(self, window):
        self.backgroundImage.draw(window)
        self.draw_menu(window)
        run = True
        while run:
            click = window.getMouse()
            if self.get_button_press(window, click) == 'play':
                run = False
                self.undraw_menu()
            elif self.get_button_press(window, click) == 'scores':
                score = self.get_high_score()
                self.undraw_menu()
                self.draw_scores(window, score)
                window.getMouse()
                self.undraw_scores()
                self.draw_menu(window)
        return

    def draw_ingame(self, window):
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

    def undraw_ingame(self):
        self.highScoreBanner.undraw()
        self.highscoreBannerText.undraw()
        self.highscoreBannerNumberText.undraw()
        self.currentScoreText.undraw()
        return

    def update_ingame_score(self, window, score=0):
        self.currentScoreText.undraw()
        self.currentScoreText.setText(score)
        self.currentScoreText.draw(window)
        return

    def update_ingame_banner(self, window):
        self.highScoreBanner.undraw()
        self.highscoreBannerText.undraw()
        self.highscoreBannerNumberText.undraw()

        self.highscoreBannerNumberText.setText(self.get_high_score())

        self.highScoreBanner.draw(window)
        self.highscoreBannerText.draw(window)
        self.highscoreBannerNumberText.draw(window)
        return
