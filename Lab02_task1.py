from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

w_height=600
w_weight=200



def drawPixel(x,y):
    glPointSize(1)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glFlush()

def findZone(x, y):
    zone = 0
    dx = abs(x[1] - x[0])
    dy = abs(y[1] - y[0])

    if dx >= dy:
        if x[0] <= x[1]:
            if y[0] <= y[1]:
                zone = 0
            else:
                zone = 7
        else:
            if y[0] <= y[1]:
                zone = 3
            else:
                zone = 4
    else:
        if y[0] <= y[1]:
            if x[0] <= x[1]:
                zone = 1
            else:
                zone = 2
        else:
            if x[0] <= x[1]:
                zone = 6
            else:
                zone = 5
    return zone

def convertToZone0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y
    
def convertFromZone0(x ,y ,zone):
    if zone==0:
        return x ,y
    elif zone==1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y
    
def drawLine(x1, y1, x2, y2):
    zone= findZone((x1,x2),(y1,y2))
    x1, y1 = convertToZone0(x1, y1, zone)
    x2, y2 = convertToZone0(x2, y2, zone)
    dx =x2-x1
    dy =y2-y1
    delE =2*dy
    delNE = 2 * (dy - dx)
    d = 2 * dy - dx
    y=y1
    x1= int(x1)
    x2=int(x2)
    for x in range(x1, x2+1):
        x_og, y_og= convertFromZone0(x,y,zone)
        drawPixel(x_og, y_og)
        if d<0:
            d=d+ delE
            
        else:
            d=d+delNE
            y+=1



a=random.randrange(-200, 201,10) 
b=0
dcolor1=0.0
dcolor2=1.0
dcolor3=1.0

def drawDiamond():
    global a , b, dcolor1, dcolor2 ,dcolor3
    glColor3f(dcolor1, dcolor2, dcolor3)
    drawLine(200 + a, 560 + b, 190 + a, 540 + b)
    drawLine(190 + a, 540 + b, 200 + a, 520 + b)
    drawLine(200 + a, 520 + b, 210 + a, 540 + b)
    drawLine(210 + a, 540 + b, 200 + a, 560 + b)
    


def drawCross():
    glColor3f(1, 0, 0)
    drawLine(390, 600, 350, 560)
    drawLine(390, 560, 350, 600)


def drawPauseBtn():
    glColor3f(1.0, 1.0, 0.0)
    drawLine(190,600, 190, 560)
    drawLine(210,600, 210,560)

def drawPlaybtn():
    glColor3f(1.0, 1.0 , 0.0)
    drawLine(210, 580, 190, 600)
    drawLine(190, 560, 210, 580)
    drawLine(190, 600, 190, 560)


def drawStartOver():
    glColor3f(0.0, 1.0 , 1.0)
    drawLine(10, 580, 50, 580)
    drawLine(30, 560, 10, 580)
    drawLine(10, 580, 30, 600)
 

c=0
ccolor1=1.0
ccolor2=1.0
ccolor3=1.0
def drawCatcher():
    global ccolor1 ,ccolor2, ccolor3, c
    glColor3f(ccolor1, ccolor2, ccolor3)
    drawLine(120+c, 30, 250+c, 30)
    drawLine(140+c, 5, 230+c, 5)
    drawLine(140+c, 5 , 120+c, 30)
    drawLine(230+c, 5, 250+c, 30)

status="play" # or pause
count=0
speed=0
points=0
 
def specialKeyListener(key ,x, y):
    global c ,status
    if status=="play":
        if c > -120:
            if key==GLUT_KEY_LEFT:
                c-=20
        if c < 140:
            if key== GLUT_KEY_RIGHT:
                c+=20
    glutPostRedisplay()


def mouseListener(button, state, x, y ):
    
    global  w_height , status, b, points, a, c, ccolor1, ccolor2, ccolor3, dcolor1, dcolor2, dcolor3, speed, count
    y=w_height-y
    if x > 180 and x < 220 and y < 600 and y > 540:
        if button==GLUT_LEFT_BUTTON:
            if (state== GLUT_DOWN):
                if status=="play":
                    status="pause"
                    print("Pause")
                else:
                    ccolor1=1.0
                    ccolor2=1.0
                    ccolor3=1.0
                    if b==0:
                        dcolor1= random.random()
                        dcolor2= random.random()
                        dcolor3= random.random()
                    status="play"
                    print("play")

    if x > 0 and x < 55 and y < 600 and y > 540:
        if button==GLUT_LEFT_BUTTON:
            if(state == GLUT_DOWN):
                print('Starting Over')
                status = "play"
                a = random.randrange(-190, 190, 10)
                b = 0
                c = 0
                points = 0
                speed = 0
                count = 0
                dcolor1 = random.random()
                dcolor2 = random.random()
                dcolor3 = random.random()
                ccolor1=1.0
                ccolor2=1.0
                ccolor3=1.0
    
    glutPostRedisplay()

    if x > 330 and x < 400 and y < 600 and y > 540:
        if button==GLUT_LEFT_BUTTON:
            if(state == GLUT_DOWN):
                print("Goodbye! Final Score:", points)
                glutDestroyWindow(wind)


def collison_check():
    global status , a,b,c, points, dcolor1, dcolor2, dcolor3, color1,ccolor2, ccolor3, count, speed
    dmd_leftx=190+a
    dmd_rightx= 210+a
    dmd_bottomy=520+b
    cth_leftx=120+c
    cth_rightx= 250+c
    cth_topy= 30
    if status=="play":
        drawPauseBtn()
        if dmd_bottomy <= cth_topy:
            if dmd_leftx >= cth_rightx or dmd_rightx <= cth_leftx:
                status="pause"
                a=0
                b=0
                c=0
                dcolor1=0
                dcolor2=0
                dcolor3=0
                ccolor1=1.0
                ccolor2=0.0
                ccolor3=0.0
                print("Game Over! Final Score: ",points)
                speed=0
                points=0
                count=0
            else:
                b=0
                a=random.randrange(-190, 190, 10 )
                points+=1
                dcolor1=random.random()
                dcolor2=random.random()
                dcolor3=random.random()
                print("Score:",points)
                count+=1
                if count==2:
                    speed+=4
                    count=0
    else:
        drawPlaybtn()

def animation():
    global b, speed
    if status=="play":
        ran=random.randrange(-190,190,10)
        if b>- 560:
            b-=(speed+2)

    

                
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    drawDiamond()
    drawCross()
    # drawPauseBtn()
    # drawPlaybtn()
    drawStartOver()
    drawCatcher()
    animation()
    collison_check()
    glutSwapBuffers()
    glutPostRedisplay()


def init():
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,400,0,600,0,1)
    glMatrixMode(GL_MODELVIEW)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(400, 600)
wind = glutCreateWindow(b"Catch the Diamonds!")
init()
glutDisplayFunc(display)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glEnable(GL_DEPTH_TEST)
glutMainLoop()

