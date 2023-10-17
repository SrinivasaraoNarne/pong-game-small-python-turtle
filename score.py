from turtle import Turtle

L_SCORE = 0
R_SCORE = 0


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.writing()

    def writing(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def pointl(self):
        self.l_score += 1
        self.writing()

    def pointr(self):
        self.r_score += 1
        self.writing()
