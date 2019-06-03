import turtle


class Window:
    def __init__(self, size):
        self.window = turtle.Screen()
        self.window.title("Pong Game for AGH")
        self.window.bgcolor("white")
        self.window.setup(width=size[0], height=size[1])
        self.window.tracer(0)

    def update(self):
        self.window.update()


def file_to_list(conf_file):
    window_size = conf_file.readline()
    window_size = window_size.split(':')
    window_size = window_size[1].split('x')
    window_size = list(map(int, window_size))
    return window_size




