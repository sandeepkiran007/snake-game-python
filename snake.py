from turtle import Turtle
START_POSITIONS = [(0, 0), (0, -20), (0, -40)]
SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        self.head.color('violet')

    def move(self):
        for pos in range(len(self.body) - 1, 0, -1):
            xcor, ycor = self.body[pos - 1].pos()
            self.body[pos].goto(xcor, ycor)
        self.body[0].forward(SPEED)

    def create_snake(self):
        for position in START_POSITIONS:
            self.create_body(position)


    def create_body(self, position):
        new_turtle = Turtle()
        new_turtle.setheading(90)
        new_turtle.shape('square')
        new_turtle.color('yellow')
        new_turtle.penup()
        new_turtle.goto(position)
        self.body.append(new_turtle)

    def extend(self):
        self.create_body(self.body[-1].pos())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)