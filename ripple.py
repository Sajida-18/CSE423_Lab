from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

W_Width, W_Height = 700,700
radius = []
cx = []
cy = []
max_rad_list = []

def init():
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,W_Width,0,W_Height,0,1)
    glMatrixMode(GL_MODELVIEW)


def circ_points(x, y, cx, cy):
    glVertex2f(x + cx, y + cy)
    glVertex2f(y + cx, x + cy)

    glVertex2f(y + cx, -x + cy)
    glVertex2f(x + cx, -y + cy)

    glVertex2f(-x + cx, -y + cy)
    glVertex2f(-y + cx, -x + cy)

    glVertex2f(-y + cx, x + cy)
    glVertex2f(-x + cx, y + cy)

    
def mid_circle (cx, cy, radius):
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


def mouseListener(button, state, x, y):	
    global radius, cx, cy, max_rad_list
    if button==GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            print(f'Ripple at ({x},{y})')

            #if list is empty, we need to initialize the list
            max_rad = max([((0 - x)**2 + (W_Height - (W_Height - y))**2 )**(1/2), ((W_Width - x)**2 + (W_Height - (W_Height - y))**2 )**(1/2), ((0 - x)**2 + (0 - (W_Height - y))**2 )**(1/2), ((W_Width-x)**2 + (0 - (W_Height - y))**2 )**(1/2)])
            if radius == []:
                radius = [20]
                cx = [x]
                cy = [W_Height - y]
                max_rad_list=[max_rad]
            else:
                radius.append(20)
                cx.append(x)
                cy.append(W_Height - y)
                max_rad_list.append(max_rad)

            print(f'Number of waves in screen: {len(radius)}')
            mid_circle(x, W_Height - y, 20)

    glutPostRedisplay()


def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glColor3f(0, 0.8, 0.9)
    glPointSize(2)
    glBegin(GL_POINTS)

    for i in range(len(radius)):
        mid_circle(cx[i], cy[i], radius[i])

    glEnd()
    glutSwapBuffers()
    glutPostRedisplay()

def animation():
    global radius, cx, cy, max_rad_list

    if radius != []: 
        if radius[0] > max_rad_list[0]: 
            radius.pop(0)
            cx.pop(0)
            cy.pop(0)
            max_rad_list.pop(0)

    for i in range(len(radius)):
        if radius != []:
            if radius[i] < max_rad_list[i]:
                radius[i] = radius[i] + 2

    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
glutInitWindowSize(700, 700)
wind = glutCreateWindow(b"Ripple")
init()
glutDisplayFunc(display)
glutIdleFunc(animation)
#glutKeyboardFunc(keyboardListener)
#glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glEnable(GL_DEPTH_TEST)
glutMainLoop()