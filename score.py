from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('red')
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_score()

    def increment_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("Arial", 20, "bold"))


