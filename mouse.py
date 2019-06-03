from ctypes import windll, Structure, c_long, byref


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def query_mouse_position():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return pt.x


mouse_sensitiveness = 10


def mouse_check(old_x, paddle):
    if old_x - query_mouse_position() > mouse_sensitiveness:
        paddle.move_left()
        return query_mouse_position()
    elif old_x - query_mouse_position() < -mouse_sensitiveness:
        paddle.move_right()
        return query_mouse_position()
    else:
        return old_x


