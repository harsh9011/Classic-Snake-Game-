from turtle import Turtle
ALIGNMENT = "center"
FONT_SCORE = ("Courier",24,"normal")




class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.write(f"score: {self.score}", align=ALIGNMENT,font=FONT_SCORE)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"score: {self.score}", align=ALIGNMENT,font=FONT_SCORE)

    def game_over(self):
        self.color("white")
        self.goto(x=0,y=0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT_SCORE)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()






