from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from midpoint import draw_circle, draw_line, draw_pixel

# window
width, height = 500, 500


def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, 0, 1)
    glMatrixMode(GL_MODELVIEW)


def display():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glPointSize(2)
    glColor3f(1, 1, 1)
    # glBegin(GL_POINTS)
    draw_pixel(250, 250)
    draw_circle(250, 250, 50)
    draw_line(150, 250, 350, 250)
    # glEnd()
    glutSwapBuffers()
    glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(width, height)
wind = glutCreateWindow(b"circle drawing stuff")
init()

glutDisplayFunc(display)


glEnable(GL_DEPTH_TEST)
glutMainLoop()
