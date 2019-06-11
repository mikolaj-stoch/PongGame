from turtle import Turtle, Shape
from pynput.mouse import Controller
import random

class Paddle:
    speed_of_moving = 9 # Default speed of moving.
    margin = 10 # Margin to not to collision with area walls.

    def __init__(self, paddle_width_half, paddle_height_half):
        self.paddle = Turtle()
        self.paddle_width_half = paddle_width_half # Set paddle size.
        self.paddle_height_half = paddle_height_half
        self.area = []
        self.cpu_player = False  # Default player controls paddle.
        self.is_hard_difficulty = False  # Default easy difficulty when cpu is playing.
        self.mouse_player = False   # Default no mouse control.

    def set_down(self):
        self.paddle.penup()
        self.paddle.shape("paddle") # Set shape.
        self.paddle.sety(self.area[1] + self.margin)  # Set a little below top of area.

    def set_up(self):
        self.paddle.penup()
        self.paddle.shape("paddle") # Set shape.
        self.paddle.sety(self.area[0] - self.margin) # Set a little above of the bottom of area.

    def get_coordinates(self): # Getter for paddle position.
        coordinates = []
        coordinates.append(self.paddle.xcor())
        coordinates.append(self.paddle.ycor())
        return coordinates

    @staticmethod
    def make_paddle_shape(paddle_width_half, paddle_height_half):
        paddle_shape = Shape("compound") # Compound need to make more complex shape.
        # Add points to new shape.
        paddle_points = ((-paddle_height_half, -paddle_width_half),
                         (-paddle_height_half, paddle_width_half),
                         (paddle_height_half, paddle_width_half),
                         (paddle_height_half, -paddle_width_half))
        # Add points and set color.
        paddle_shape.addcomponent(paddle_points, "black")
        return paddle_shape

    def set_area(self, area): # Setter for game area.
        self.area = area

    # Move to left or right using speed of moving and current position.
    def move_left(self):
        if self.check_if_move_possible():
            self.paddle.setx(self.paddle.xcor() - self.speed_of_moving)

    def move_right(self):
        if self.check_if_move_possible():
            self.paddle.setx(self.paddle.xcor() + self.speed_of_moving)

    def check_if_move_possible(self):
        # Takes paddles x coordinate, half of it's width and margin - to calculate if move is allowed. For both sides.
        if self.paddle.xcor() + self.paddle_width_half + self.margin <= self.area[3] and self.paddle.xcor() - self.paddle_width_half - self.margin >= self.area[2]:
            return True
        # Move back to last allowed position. (Makes "bounce" effect)
        elif self.paddle.xcor() + self.paddle_width_half + self.speed_of_moving + self.margin <= self.area[3]:
            self.paddle.setx(self.paddle.xcor() + self.speed_of_moving)
            return False
        elif self.paddle.xcor() - self.paddle_width_half - self.speed_of_moving - self.margin >= self.area[2]:
            self.paddle.setx(self.paddle.xcor() - self.speed_of_moving)
            return False

    def computer_playing(self, ball):
        if self.cpu_player == True:
            if self.is_hard_difficulty == True:
                # Computer move great and some + / - accurately when has the same speed of moving like dx of ball.
                if self.speed_of_moving != abs(ball.dx): # No to change in every induction.
                    self.speed_of_moving = abs(ball.dx)
            else:
                # Minus one to make bigger error so it will be easier to score.
                if self.speed_of_moving != abs(ball.dx) - 1:
                    self.speed_of_moving = abs(ball.dx) - 1
            # If ball is moving to left, move paddle to left. Vice versa to right.
            if ball.dx < 0:
                self.move_left()
            else:
                self.move_right()

    def set_mouse(self):
        self.mouse = Controller() # Assign mouse to be controller.
        self.x_mouse = self.mouse.position[0] # Mouse x coordinate.

    def mouse_playing(self):
        if self.mouse_player == True:
            # When mouse position is changed by ten, make move.
            if self.mouse.position[0] - self.x_mouse > 10:
                self.move_right()
                self.x_mouse = self.mouse.position[0] # Assign mouse position to be held in x_mouse in integer.
            elif self.mouse.position[0] - self.x_mouse < -10:
                self.move_left()
                self.x_mouse = self.mouse.position[0]


class Ball:
    dx = 3
    dy = dx

    def __init__(self, paddle_up, paddle_down, area, score, window):
        self.ball = Turtle()
        self.ball.speed(0)
        self.ball.shape("circle") # Shape.
        self.ball.shapesize(0.5, 0.5)
        self.ball_radius = 10 * 0.5 # Radius of our ball.
        self.ball.color("black")
        self.ball.penup()
        self.ball.goto(0, 0)
        # Getting paddles in constructor to optimaze code.
        # Avoidance passing the argument in run_game() method in main.
        self.paddle_up = paddle_up
        self.paddle_down = paddle_down
        self.area = area # Get size of game area.
        self.score = score
        self.window = window

    # Setting speed methods. (Needed for clicking keys)
    def set_speed_01(self):
        if self.dx < 0:
            self.dx = - 2
        else:
            self.dx = 2
        if self.dy < 0:
            self.dy = abs(self.dx) * -1
        else:
            self.dy = abs(self.dx)

    def set_speed_02(self):
        if self.dx < 0:
            self.dx = - 2.
        else:
            self.dx = 2.2
        if self.dy < 0:
            self.dy = abs(self.dx) * -1
        else:
            self.dy = abs(self.dx)

    def set_speed_03(self):
        if self.dx < 0:
            self.dx = - 2.5
        else:
            self.dx = 2.5
        if self.dy < 0:
            self.dy = abs(self.dx) * -1
        else:
            self.dy = abs(self.dx)

    def set_speed_04(self):
        if self.dx < 0:
            self.dx = - 3
        else:
            self.dx = 3
        if self.dy < 0:
            self.dy = abs(self.dx) * -1
        else:
            self.dy = abs(self.dx)

    def set_speed_05(self):
        if self.dx < 0:
            self.dx = - 3.5
        else:
            self.dx = 3.5
        if self.dy < 0:
            self.dy = abs(self.dx) * -1
        else:
            self.dy = abs(self.dx)

    def set_speed_06(self):
        if self.dx < 0:
            self.dx = - 3.8
        else:
            self.dx = 3.8
        if self.dy < 0:
            self.dy = abs(self.dx) * -1
        else:
            self.dy = abs(self.dx)

    def set_speed_07(self):
        if self.dx < 0:
            self.dx = - 4
        else:
            self.dx = 4
        if self.dy < 0:
            self.dy = abs(self.dx) * -1
        else:
            self.dy = abs(self.dx)

    def set_speed_08(self):
        if self.dx < 0:
            self.dx = - 4.2
        else:
            self.dx = 4.2
        if self.dy < 0:
            self.dy = abs(self.dx) * -1
        else:
            self.dy = abs(self.dx)

    def set_speed_09(self):
        if self.dx < 0:
            self.dx = - 4.5
        else:
            self.dx = 4.5
        if self.dy < 0:
            self.dy = abs(self.dx) * -1
        else:
            self.dy = abs(self.dx)

    def moving(self):
        # Change x vector if right or left wall is touched.
        if self.ball.xcor() + self.ball_radius >= self.area[3]:
            self.dx = self.dx * -1
        elif self.area[2] >= self.ball.xcor() - self.ball_radius:
            self.dx = self.dx * -1
        # Update coordinates.
        self.ball.setx(self.ball.xcor() + self.dx)
        self.ball.sety(self.ball.ycor() + self.dy)
        # If collision detected, change y vector.
        if self.ball_collision_with_paddle(self.paddle_up) or self.ball_collision_with_paddle(self.paddle_down):
            self.dy = self.dy * -1
            # Change randomly x vector to diversity and make less predictable game.
            if random.randint(1,2) == 1:
                self.dx = self.dx * -1

    def check_if_score(self):
        # If passed the area down and up wall, add the score. Then, reset the ball and write new score.
        if self.ball.ycor() + self.ball_radius >= self.area[0]:
            self.score[1] = self.score[1] + 1
            self.ball.goto(0, 0)
            self.window.write_scores(self.score)
        elif self.area[1] >= self.ball.ycor() - self.ball_radius:
            self.score[0] = self.score[0] + 1
            self.ball.goto(0, 0)
            self.window.write_scores(self.score)

    def ball_collision_with_paddle(self, paddle):
        coordinates = paddle.get_coordinates() # Get paddle coordinates.
        # Detection of the collision. Taking ball as square. Not perfect, but works quite good.
        # When paddle position minus ball posistion is smaller than radius with paddle size.
        collision_horizontal = self.ball_radius + paddle.paddle_width_half >= abs(coordinates[0] - self.ball.xcor())
        collision_vertical = self.ball_radius + paddle.paddle_height_half >= abs(coordinates[1] - self.ball.ycor())
        return collision_horizontal and collision_vertical

    def reset(self):
        self.ball.setpos(0,0)

    def get_ball_coordinates(self):
        coordinates = []
        coordinates.append(self.ball.xcor())
        coordinates.append(self.ball.ycor())
        return coordinates







