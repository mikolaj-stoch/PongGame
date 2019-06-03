import turtle


class Paddle:
    def __init__(self):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("black")

    def set_down(self, size):
        if size[0] > 900:
            self.paddle.shapesize(stretch_wid=1, stretch_len=6)
        else:
            self.paddle.shapesize(stretch_wid=1, stretch_len=4)
        self.paddle.penup()
        self.paddle.goto(0, -0.85 * size[1]/2)

    def set_up(self, size):
        if size[0] > 900:
            self.paddle.shapesize(stretch_wid=1, stretch_len=6)
        else:
            self.paddle.shapesize(stretch_wid=1, stretch_len=4)
        self.paddle.penup()
        self.paddle.goto(0, 0.85 * size[1]/2)

    def move_left(self):
        self.paddle.setx(self.paddle.xcor() - 10)

    def move_right(self):
        self.paddle.setx(self.paddle.xcor() + 10)


class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("black")
        self.ball.penup()
        self.ball.goto(0,0)