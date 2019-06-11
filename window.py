from turtle import Turtle, Screen

class Window:
    def __init__(self, size):
        # Some basic stuff.
        self.window = Screen()
        self.window.title("Pong Game for AGH")
        self.window.bgcolor("white")
        self.window.setup(width=size[0], height=size[1]) # Set size from file. (It is converted to tuple before).
        self.window.tracer(0) # Allow draw things immediately.
        self.vertical_margin = 60 # Margin for area.
        self.horizontal_margin = 20
        # Setting our game area - place where ball is moving and paddles.
        self.top = self.window.window_height() / 2 - self.vertical_margin
        self.bottom = -self.window.window_height() / 2 + self.vertical_margin
        self.left = -self.window.window_width() / 2 + self.horizontal_margin
        self.right = self.window.window_width() / 2 - self.horizontal_margin
        # Making (drawing) area.
        self.area = Turtle()
        self.area.hideturtle() # Hide turtle on the screen.
        self.area.penup() # No drawing when moving.
        self.area.goto(self.right, self.top)
        self.area.pendown() # Pull the pen down - start drawing.
        self.area.goto(self.left, self.top)
        self.area.goto(self.left, self.bottom)
        self.area.goto(self.right, self.bottom)
        self.area.goto(self.right, self.top)
        # Initialization of score writing and pause text.
        self.score_turtle = Turtle()
        self.score_turtle.penup()
        self.score_turtle.hideturtle()
        self.pause_text = Turtle()
        self.pause_text.hideturtle()

    def update(self): # Update method for main.
        self.window.update()

    def add_shape(self, shape, str): # Add shape to window.
        self.window.register_shape(str, shape)

    def get_area(self): # Return area size. (Needed for ball and paddles)
        area = []
        area.append(self.top)
        area.append(self.bottom)
        area.append(self.left)
        area.append(self.right)
        return area

    def write_scores(self, score):
        self.score_turtle.clear()
        # Go to above and below paddles and write score.
        self.score_turtle.goto(0, self.window.window_height()/2  - self.vertical_margin)
        self.score_turtle.write(score[0], align="center", font=("Arial", 32, "bold"))
        self.score_turtle.goto(0, -self.window.window_height()/2 + self.vertical_margin/6)
        self.score_turtle.write(score[1], align="center", font=("Arial", 32, "bold"))

    def write_pause(self, pause):
        if pause == True:
            self.pause_text.penup() # No drawing when moving.
            self.pause_text.goto(0, 0) # Go to middle of the screen and write.
            self.pause_text.write("PAUSE. CLICK P AGAIN TO RESUME", align="center", font=("Arial", 18, "bold"))
        if pause == False:
            self.pause_text.undo() # Undo previously written text.


def file_to_list(conf_file):
    window_size = conf_file
    window_size = window_size.split(':') # Split when ":" is used.
    window_size = window_size[1].split('x') # Second part of previous text split to two numbers.
    window_size = list(map(int, window_size)) # Convert to list of integers.
    print(window_size)
    return window_size




