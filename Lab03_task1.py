from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random 



width= 400
height = 600 
#shooter
shooter_cx=200
shooter_cy=30
shooter_r =10
shooter_shift=0
shooter_incr = 0
#Nubble shot
shotBubble_cx=0
shotBubble_cy=0
shotBubble_r = 5

# bubbles
radius = []
cx = []
cy = []
bubble_decr = []

status = "hold"
bubble_status = []

pause = False
point = 0
life = 3
dead = False


def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, 0, 1)
    glMatrixMode(GL_MODELVIEW)

def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def draw_restart():
    glColor3f(0.0, 0.5, 0.8)
    draw_line(10, 580, 50, 580)
    draw_line(30, 560, 10, 580)
    draw_line(10, 580, 30, 600)


def draw_cross():
    glColor3f(1.0, 0.0, 0.0)
    draw_line(390, 600, 350, 560)
    draw_line(390, 560, 350, 600)


def draw_pause():
    global pause
    glColor3f(1.0, 1.0, 0.0)
    if pause == True:
        draw_line(210, 580, 190, 600)
        draw_line(190, 560, 210, 580)
        draw_line(190, 600, 190, 560)
    else:
        draw_line(190,600, 190, 560)
        draw_line(210,600, 210,560)


def draw_circ_points(x, y, cx, cy):
    glVertex2f(x + cx, y + cy)
    glVertex2f(y + cx, x + cy)

    glVertex2f(y + cx, -x + cy)
    glVertex2f(x + cx, -y + cy)

    glVertex2f(-x + cx, -y + cy)
    glVertex2f(-y + cx, -x + cy)

    glVertex2f(-y + cx, x + cy)
    glVertex2f(-x + cx, y + cy)


def midPointCircle(cx, cy, radius):
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
        draw_circ_points(x, y, cx, cy)




def draw_shooter():
    global shooter_cx, shooter_cy, shooter_r, shooter_shift
    midPointCircle(shooter_cx + shooter_shift, shooter_cy, shooter_r)


def draw_bubbles():
    global cx, cy, bubble_decr, radius, bubble_status
    if len(radius) >= 0:
        for i in range(len(radius)):
            if bubble_status[i] == "fall":
                midPointCircle(cx[i], cy[i] - bubble_decr[i], radius[i])
            else:
                continue

    glutPostRedisplay()


def display():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    draw_restart()
    draw_cross()
    draw_pause()
    glPointSize(2)
    glColor3f(1, 1, 1)
    glBegin(GL_POINTS)
    draw_shooter()
    draw_bubbles()
    animate()
    glEnd()
    glutSwapBuffers()
    glutPostRedisplay()

def create_random_bubbles(n=0):
    global pause, dead, radius, cx, cy, bubble_status, bubble_decr
    if not pause and not dead:
        if bubble_status.count("fall") <= 4:
            radius.append(random.randrange(10, 25, 5))
            cx.append(random.randrange(20, 430, 20))
            cy.append(random.randrange(300, 500, 20))
            bubble_status.append("fall")
            bubble_decr.append(0.1)
        glutTimerFunc(1000, create_random_bubbles, 0)


def mouseListener(button, state, x, y):
    global height, width, pause, point, dead ,life, cx, cy, radius, bubble_decr, bubble_status, shooter_shift, shooter_incr
    y = height - y

    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            #pause
            if x > 180 and x < 220 and y > 540 and y < 600:
                pause = not pause
            #reset
            elif x > 0 and x < 55 and y> 540 and y < 600:
                pause= False
                dead = False
                point= 0
                life = 3
                cx=[]
                cy=[]
                radius=[]
                bubble_decr=[]
                bubble_status = []
                shooter_shift=0
                shooter_incr = 0
                create_random_bubbles()
            
            #cross
            elif x > 330 and x < 400 and y > 540 and y < 600:
                print("Goodbye")
                print(f"Score: {point}")
                glutDestroyWindow(wind)




def keyboardListener(key, x, y):
    global shooter_shift, pause, dead, shooter_cx, shotBubble_cx, status
    if not pause and not dead:
        if shooter_shift < 140:
            if key == b'a':
                shooter_shift += 20
                # print("right")
        if shooter_shift > -230:
            if key == b'd':
                shooter_shift -= 20
                # print("left")
    if status == "hold" and key == b" ":

        status = "shoot"
        shotBubble_cx = shooter_cx + shooter_shift




def collision(i):
    global cx, cy, shotBubble_cx, shotBubble_cy, radius, shotBubble_r,status
    global bubble_status, shooter_incr, bubble_decr
    global point, life
    global shooter_cx, shooter_cy, shooter_shift, shooter_r
   
    bleft= cx[i]-radius[i]
    bright= cx[i]+radius[i]
    bup= cy[i]+radius[i]- bubble_decr[i]
    bdown= cy[i]- radius[i]- bubble_decr[i]
    sleft= shotBubble_cx- shotBubble_r
    sright=shotBubble_cx+shotBubble_r
    sup= shotBubble_cy+shotBubble_r
    sdown=shotBubble_cy-shotBubble_r
    

    shleft= shooter_cx - shooter_r + shooter_shift
    shright =shooter_cx + shooter_r + shooter_shift 
    shup = shooter_cy + shooter_r

    if shup >= bdown and bubble_status[i] == "fall":
        if (shleft <= bright and shleft >= bleft) or (shright <= bright and shright >= bleft):
            life = 0

    if sup >= bdown and bubble_status[i] == "fall":
        if (sleft <= bright and sleft >= bleft) or (sright <= bright and sright >= bleft):
            bubble_status[i]="pop"
            status="hold"
            shooter_incr=0
            point += 1
            print("Score is:", point)


def bubble_fall():
    global bubble_decr, cy

    global cx, cy, shotBubble_cx, shotBubble_cy, radius, shooter_r
    global bubble_status, shooter_incr
    global point, life

    if len(bubble_decr) >= 0:
        for i in range(len(bubble_decr)):
            collision(i)
            if  cy[i] + radius[i]-bubble_decr[i]  > radius[i] * 2:
                bubble_decr[i] += 0.01

            else:
                if bubble_status[i] == "fall":
                    life -= 1
                    
                    print("Life remain:", life)
                bubble_status[i]="pop"



def animate():
    global shooter_incr, shooter_shift, shotBubble_cx, shotBubble_cy, shotBubble_r
    global status, pause, dead
    global bubble_decr, life, point, cx, cy, radius, bubble_decr, bubble_status
    if not pause and not dead:
        if status == "shoot":
            if shooter_incr <= 560:
                shooter_incr += 0.1
                shotBubble_cy = shooter_cy + shooter_incr
                shotBubble_r = shooter_r - 5
                midPointCircle(shotBubble_cx, shotBubble_cy, shotBubble_r)
            else:
                #shooterReset
                status="hold"
                shooter_incr=0
        bubble_fall()
        if life == 0:
            print("Game Over. Score:", point)
            cx=[]
            cy=[]
            radius=[]
            bubble_decr=[]
            bubble_status =  []
            dead = True





glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(width, height)
wind = glutCreateWindow(b"circle drawing stuff")
init()
glutInitWindowSize(400, 600)
glutIdleFunc(animate)
glutDisplayFunc(display)
create_random_bubbles()
glutKeyboardFunc(keyboardListener)
# glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glEnable(GL_DEPTH_TEST)
glutMainLoop()

