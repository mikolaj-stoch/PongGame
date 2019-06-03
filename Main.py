from window import file_to_list
from window import Window
from gameObjects import Paddle
from gameObjects import Ball
from mouse import mouse_check
from mouse import query_mouse_position
import turtle

conf_file = open("conf.txt", 'r')
window_size = file_to_list(conf_file)
conf_file.close()

game_window = Window(window_size)

paddle_down = Paddle()
paddle_down.set_down(window_size)

paddle_up = Paddle()
paddle_up.set_up(window_size)

ball = Ball()

game_window.window.listen()
game_window.window.onkeypress(paddle_up.move_left, "Left")
game_window.window.onkeypress(paddle_up.move_right, "Right")

x_mouse = query_mouse_position()

# Main
while True:
    game_window.update()
    x_mouse = mouse_check(x_mouse, paddle_down)





