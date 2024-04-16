from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_pixel(x, y):

    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def circ_points(x, y, cx, cy):
    glBegin(GL_POINTS)
    glVertex2f(x + cx, y + cy)
    glVertex2f(y + cx, x + cy)

    glVertex2f(y + cx, -x + cy)
    glVertex2f(x + cx, -y + cy)

    glVertex2f(-x + cx, -y + cy)
    glVertex2f(-y + cx, -x + cy)

    glVertex2f(-y + cx, x + cy)
    glVertex2f(-x + cx, y + cy)
    glEnd()


def draw_circle(cx, cy, radius):
    d = 1 - radius
    x = 0
    y = radius

    while x < y:
        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * x - 2 * y + 5
            y = y - 1
        x = x + 1
        circ_points(x, y, cx, cy)


def draw_point(x, y, zone):
    if zone == 0:
        draw_pixel(x, y)
    elif zone == 1:
        draw_pixel(y, x)
    elif zone == 2:
        draw_pixel(-y, x)
    elif zone == 3:
        draw_pixel(-x, y)
    elif zone == 4:
        draw_pixel(-x, -y)
    elif zone == 5:
        draw_pixel(-y, -x)
    elif zone == 6:
        draw_pixel(y, -x)
    elif zone == 7:
        draw_pixel(x, -y)


def findZone_convertToZero(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) >= abs(dy):  # zone 0, 3, 4, and 7
        if x2 >= x1:
            if y2 >= y1:
                return 0, x1, y1, x2, y2
            else:
                return 7, x1, -y1, x2, -y2
        else:
            if y2 >= y1:
                return 3, -x1, y1, -x2, y2
            else:
                return 4, -x1, -y1, -x2, -y2
    else:  # zone 1, 2, 5, and 6
        if x2 >= x1:
            if y2 >= y1:
                return 1, y1, x1, y2, x2
            else:
                return 6, -y1, x1, -y2, x2

        else:
            if y2 >= y1:
                return 2, y1, -x1, y2, -x2
            else:
                return 5, -y1, -x1, -y2, -x2


def midpoint_line_algo(x1, y1, x2, y2, zone):

    dx = x2 - x1
    dy = y2 - y1

    d = 2 * dy - dx

    incr_NE = dy - dx
    incr_E = dy

    start = int(x1)
    end = int(x2)
    y = y1

    for x in range(start, end + 1):
        draw_point(x, y, zone)

        if d > 0:
            d = d + incr_NE
            y += 1
        else:
            d += incr_E


def draw_line(a1, b1, a2, b2):

    zone, x1, y1, x2, y2 = findZone_convertToZero(a1, b1, a2, b2)
    midpoint_line_algo(x1, y1, x2, y2, zone)
