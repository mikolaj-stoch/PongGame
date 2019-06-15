from window import file_to_list
from window import Window
from gameObjects import Paddle
from gameObjects import Ball
import time


# At first we are taking some player preferences - some keyboard inputs to set up game.
'''
print("Welcome to pong game!")
print("First, please told me what mode would you like to play - 1 person vs CPU, or two person vs each other? (Type 1 for one player mode, type 2 for two player mode)")
player_controller = "k"
number_of_players = input()
if number_of_players == "1":
    print("Okey, would you like to play with mouse or keyboard (Type m for mouse, type k for keyboard)")
    player_controller = input()
    print("Choose CPU difficulty (Type 1 for easy, type 2 for hard)")
    difficulty = input()
if number_of_players == "2":
    print("Okey, one player with play with keyboard (up paddle), the second one with mouse (down paddle). Game will strart in five seconds!")
'''


conf_file = open("conf.txt", 'r')  # Reading from file screen size.
lines = conf_file.readlines()
window_size = file_to_list(lines[0]) # Using static method form windows class to convert string to tuple.
# Divide every line by using split with : argument.
# Then, do it again on second element in list (now with space) to get only one symbol.
number_of_players = lines[1]
number_of_players = number_of_players.split(':')
number_of_players = number_of_players[1].split(' ')
number_of_players = number_of_players[1]
number_of_players = number_of_players[0]
player_controller = lines[2]
player_controller = player_controller.split(':')
player_controller = player_controller[1].split(' ')
player_controller = player_controller[1]
player_controller = player_controller[0]
difficulty = lines[3]
difficulty = difficulty.split(':')
difficulty = difficulty[1].split(' ')
difficulty = difficulty[1]
difficulty = difficulty[0]
print(difficulty)
conf_file.close()  # Closing file, as we don't need it anymore.

radius = 0.5

# Setting paddles sizes.
paddle_width_half = 90 / 2
paddle_height_half = 10 / 2
if window_size[0] < 200:
    print("Error - windows size too small. Windows size set to 500 x 500.")
    window_size[0] = 500
    window_size[1] = 500
if window_size[0] != 500:
    paddle_width_half = paddle_width_half + ( window_size[0] - 500 ) / 10
    radius = radius + ( window_size[0] - 500) / 1000


pause = False  # Pause boolean to manage pause.
game_window = Window(window_size) # Initialization of window game.
# We need paddle shape in our window -
# we are doing it by using static method from paddle class and adding shape to our game window.
game_window.add_shape(Paddle.make_paddle_shape(paddle_width_half, paddle_height_half), "paddle")

score = [0,0] # Score tuple stores our score.
game_window.write_scores(score) # Write score on the screen.

# Initialization of paddles, getting area size from window and setting them on the proper place.
paddle_down = Paddle(paddle_width_half, paddle_height_half)
paddle_down.set_area(game_window.get_area())
paddle_down.set_down()

paddle_up = Paddle(paddle_width_half, paddle_height_half)
paddle_up.set_area(game_window.get_area())
paddle_up.set_up()



# Initialization of ball, getting some game elements to ball to optimize code.
# (I don't want to give every element to update methods, so i will give them once in constructor).
ball = Ball(paddle_up, paddle_down, game_window.get_area(),score,game_window, radius)

# Resetting score and ball position.
def reset_score():
    global score
    score[0] = 0
    score[1] = 0
    game_window.write_scores(score)
    ball.reset()
    paddle_down.set_on_the_middle()
    paddle_up.set_on_the_middle()
    time.sleep(1)
    


def write_pause():
    global pause
    if pause == False:
        pause = True # If pause is false, make it true.
        disable_keys() # Disable keys, because they are not needed in pause menu.
        game_window.write_pause(pause) # Write on the screen.
    else:
        pause = False # Analogically as above
        set_keys()
        game_window.write_pause(pause)

# Method to set keys to be listened to.
def set_keys():
    global game_window
    if player_controller == "k" or number_of_players == "2": # Only if we are playing with keyboard. Or two players are playing.
        game_window.window.onkeypress(paddle_up.move_left, "Left")
        game_window.window.onkeypress(paddle_up.move_right, "Right")
    game_window.window.onkeypress(ball.set_speed_01, "1") # Speed for every number key.
    game_window.window.onkeypress(ball.set_speed_02, "2")
    game_window.window.onkeypress(ball.set_speed_03, "3")
    game_window.window.onkeypress(ball.set_speed_04, "4")
    game_window.window.onkeypress(ball.set_speed_05, "5")
    game_window.window.onkeypress(ball.set_speed_06, "6")
    game_window.window.onkeypress(ball.set_speed_07, "7")
    game_window.window.onkeypress(ball.set_speed_08, "8")
    game_window.window.onkeypress(ball.set_speed_09, "9")
    game_window.window.onkeypress(reset_score, "r") # Reset score and ball position.

# Method to be call when pause clicked - to prevent changes during pause.
def disable_keys():
    global game_window
    game_window.window.onkeypress(None, "Left")
    game_window.window.onkeypress(None, "Right")
    game_window.window.onkeypress(None, "1")
    game_window.window.onkeypress(None, "2")
    game_window.window.onkeypress(None, "3")
    game_window.window.onkeypress(None, "4")
    game_window.window.onkeypress(None, "5")
    game_window.window.onkeypress(None, "6")
    game_window.window.onkeypress(None, "7")
    game_window.window.onkeypress(None, "8")
    game_window.window.onkeypress(None, "9")
    game_window.window.onkeypress(None, "r")

# Set listener to pause key.
game_window.window.onkeypress(write_pause, "p")

# Listen to any keyboard input.
game_window.window.listen()
set_keys()

# Setting previous player inputs.
if number_of_players == "2" or player_controller == "m":
    paddle_down.set_mouse()
    paddle_down.mouse_player = True

if number_of_players == "1" and player_controller == "k":
    if difficulty == "2":
        paddle_down.is_hard_difficulty = True
    paddle_down.cpu_player = True

if number_of_players == "1" and player_controller == "m":
    if difficulty == "2":
        paddle_up.is_hard_difficulty = True
    paddle_up.cpu_player = True

# Main method to be called periodically - handle drawing and updating positions.
def run_game():
    if pause == False:
        # Make computer play paddle down.
        # Don't worry - paddle has own attribute which check that it should be play by player or CPU.
        # That function could do nothing.
        paddle_down.computer_playing(ball)
        paddle_up.computer_playing(ball)
        # Control ball movement.
        ball.moving()
        # Control score and write changes.
        ball.check_if_score()
        # Control player mouse movment. Just like computer_playing method could do nothing.
        paddle_down.mouse_playing()

    game_window.window.update() # Update and draw changes.
    game_window.window.ontimer(run_game, framerate_ms) # Set timer to run method periodically.


framerate_ms = 9 # How frequent our function has to be called. In ms.
run_game() # Run game.
game_window.window.mainloop() # Don't close window immediately.







