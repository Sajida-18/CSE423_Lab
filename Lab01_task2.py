from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

window_w, window_h = 500,500

ballx = [] 
bally = []
speed = 2
b_size = 8
color1 = []
color2 = []
color3 = []
random_dir = []
count = 0
counter = 0
blink = False
blink_counter = 0


def convert_coordinate(x,y):
    global window_w, window_h
    a = x - (window_w/2)
    b = (window_h/2) - y 
    return a,b

def draw_points(x, y, b_size, color1, color2, color3):
    glColor3f(color1, color2, color3)
    glPointSize(b_size)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def keyboardListener(key, x, y):

    global b_size, speed, count
    if count%2 == 0:
        if key==b'b':
            b_size+=1
            print("Size Increased")
        if key==b's':
            b_size-=1
            print("Size Decreased")
    if key == b' ':
        if count%2 == 0:
            speed = 0
        else:
            speed = 2
        count+=1

    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global speed, count
    if count%2 == 0:
        if key == GLUT_KEY_UP:
            speed *= 2
            print("Speed Increased")
        if key == GLUT_KEY_DOWN:	
            speed /= 2
            print("Speed Decreased")

    glutPostRedisplay()

def mouseListener(button, state, x, y):	
    global ballx, bally, random_dir, count, blink, counter
    print(x, y)
    if count%2 == 0:
        if button==GLUT_LEFT_BUTTON:
            if(state == GLUT_DOWN):   
                if counter%2 == 0:
                    blink = True
                else:
                    blink = False
                counter+=1
            
        if button==GLUT_RIGHT_BUTTON:
            if state == GLUT_DOWN: 	
                print(x,y)
                c_X, c_y = convert_coordinate(x,y)
                ballx.append(c_X)
                bally.append(c_y)
                color1.append(random.random())
                color2.append(random.random())
                color3.append(random.random())
                random_dir.append(random.randrange(1,5))

    glutPostRedisplay()

def animate():
    global ballx, bally, speed
    for i in range(len(ballx)):
        if random_dir[i] == 1:
            glutPostRedisplay()
            ballx[i] = ballx[i] + (speed)/100
            bally[i] = bally[i] -  (speed)/100

        elif random_dir[i] == 2:
            glutPostRedisplay()
            ballx[i] = ballx[i] + (speed)/100
            bally[i] = bally[i] +  (speed)/100

        elif random_dir[i] == 3:
            glutPostRedisplay()
            ballx[i] = ballx[i] - (speed)/100
            bally[i] = bally[i] +  (speed)/100

        elif random_dir[i] == 4:
            glutPostRedisplay()
            ballx[i] = ballx[i] - (speed)/100
            bally[i] = bally[i] -  (speed)/100
        
        if ballx[i] + b_size > window_w/2 or ballx[i] - b_size < -window_w/2:
            ballx[i] = min(max(ballx[i], -window_w/2 + b_size), window_w/2 - b_size)
            if random_dir[i] == 1:
               random_dir[i] = 3
            else:
               random_dir[i] = 1    

        if bally[i] + b_size > window_h/2 or bally[i] - b_size < -window_h/2:
            bally[i] = min(max(bally[i], -window_h/2 + b_size), window_h/2 - b_size)
            if random_dir[i] == 4:
                random_dir[i] = 2
            else:
                random_dir[i] = 4 
   
def display():
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0);	#//color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)
    global ballx, bally, b_size, color1, color2, color3, blink, blink_counter
    for i in range(len(ballx)):
        if blink == True:
            if blink_counter%20 == 0:
                draw_points(ballx[i], bally[i], b_size, color1[i], color2[i], color3[i])
            else: 
                draw_points(ballx[i], bally[i], b_size, 0.0, 0.0, 0.0)
            blink_counter += 1
        else:
            draw_points(ballx[i], bally[i], b_size, color1[i], color2[i], color3[i])
    animate()
   
    glutSwapBuffers()


def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance


glutInit()
glutInitWindowSize(window_w, window_h)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display)	#display callback function
glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()		#The main loop of OpenGL
