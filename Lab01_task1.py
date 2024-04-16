from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random
a=0
b=0
h_red=0
h_green=0
h_blue=0
h_alpha=0
bg_red=1
bg_blue=1
bg_green=1
bg_alpha=1

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def draw_Lines(x, y, a,b):
    glLineWidth(8) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    glVertex2f(x,y) #jekhane show korbe pixel
    glVertex2f(a,b)
    glEnd()

def draw_WD_Lines(x, y, a,b):
    glLineWidth(1) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    glVertex2f(x,y) #jekhane show korbe pixel
    glVertex2f(a,b)
    glEnd()


def draw_raindrop(x, y):
    global b
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(x, y+b)
    glVertex2f(x-a, (y-15+b))  
    glEnd()

def area (x1,y1,x2,y2,x3,y3):
    area=0.5* abs(x1*(y2-y3) + x2* (y3-y1)+ x3* (y1-y2))
    return area 

def draw_rain():
    global a
    # for x in range(0, 501, 25): 
    #    for y in range(500, 251, -25):
    for i in range(150):  #num of raindrops
        x = random.randint(0,500) % 500; 
        y = random.randint(0,500) % 500; 
        if RainNotInRoof(x,y) and RainNotInHouse(x, y) :
            draw_raindrop(x, y)
   
    

def RainNotInRoof(x,y):
    flag=False
    # a=area(250,400,100,300,400,300)
    # a1= area(x,y,250,400,100,300)
    # a2= area(x,y,100,300,400,300)
    # a3= area(x,y,400,300, 250,400)
    a=area(250,420,80,300,420,300)
    a1= area(x,y,250,420,80,300)
    a2= area(x,y,80,300,420,300)
    a3= area(x,y,420,300, 250,420)
  


    if (a1+a2+a3)!=a:
        flag=True
    return flag

def RainNotInHouse(x, y):
    flag = False

    house_left = 110 #110
    house_right = 390 #390
    house_bottom = 100
    house_top = 300

    if x < house_left or x > house_right or y < house_bottom or y > house_top:
        flag = True

    return flag

def specialKeyListener(key, x, y):
    global a, h_red, h_green ,h_blue, bg_blue, bg_red, bg_green, bg_alpha,h_alpha
    if key==GLUT_KEY_LEFT:
        a+=1
        print("wind_left")
    if key==GLUT_KEY_RIGHT:
        a-=1
        print('wind_right')
    if key==GLUT_KEY_DOWN:
        house= h_red
        if house >=0:
            h_red-=0.1
            h_blue-=0.1
            h_green-=0.1
            h_alpha-=0.1
        bg=bg_red
        if bg<=1:
            bg_red+=0.1
            bg_blue+=0.1
            bg_green+=0.1
            bg_alpha+=0.1
    if key==GLUT_KEY_UP:
        house=h_red
        if house <= 1:
            h_red+=0.1
            h_blue+=0.1
            h_green+=0.1
            h_alpha+=0.1
        bg=bg_red
        if bg>=0:
            bg_red-=0.1
            bg_blue-=0.1
            bg_green-=0.1
            bg_alpha-=0.1

      
    

    glutPostRedisplay()





def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()



def showScreen():
    global h_red, h_blue, h_green ,bg_red, bg_blue, bg_green, bg_alpha
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # glColor3f(1.0, 1.0, 1.0) #kono kichur color set (RGB)
    glClearColor(bg_red,bg_blue, bg_green, bg_alpha)
    glColor3f(h_red,h_blue,h_green) 
    draw_rain()
  
    #call the draw methods here
    draw_points(220, 160)
    #Roof
    draw_Lines(100,300, 400,300)
    draw_Lines(100,300, 250,400)
    draw_Lines(250,400, 400,300)
    #House
    draw_Lines(110,300, 110,100)
    draw_Lines(110,100, 390,100)
    draw_Lines(390,100, 390,300)
    #door
    draw_WD_Lines(180,100, 180,210)
    draw_WD_Lines(180,210, 240,210)
    draw_WD_Lines( 240,210,240,100)
    #Window
    draw_WD_Lines(290,220, 350,220)
    draw_WD_Lines(290,220, 290,280)
    draw_WD_Lines(290,280, 350,280)
    draw_WD_Lines(350,280,350,220)
    draw_WD_Lines(290,250, 350,250)
    draw_WD_Lines(320,280, 320,220)
   
    glutPostRedisplay()
    glutSwapBuffers()
    
def animate():
   
    global b
    b=(b+1)%15  

    glutPostRedisplay()

    
def init():
    global bg_red, bg_blue, bg_green, bg_alpha
    #//clear the screen
    glClearColor(bg_red,bg_blue, bg_green, bg_alpha)
   
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)

glutInit()
glutInitDisplayMode(GLUT_RGBA )
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Assignment_1 Task1") #window name
init()
glutDisplayFunc(showScreen)
# glutIdleFunc(animate)

glutSpecialFunc(specialKeyListener)


glutMainLoop()
