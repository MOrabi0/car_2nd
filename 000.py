
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
z = .8*3

def myinit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,1,1,30)
    gluLookAt(8,9,6,
              0,0,0,
              0,1,0)
    glClearColor(0,1,0,1)
    glClear(GL_COLOR_BUFFER_BIT)

#the vertices
def xyz():

    glBegin(GL_LINES)
    glColor(1,0,0)
    glVertex(0,0,0)
    glVertex(10,0,0)
    glColor(0,1,0)
    glVertex(0,0,0)
    glVertex(0, 10, 0)
    glColor(0,0,1)
    glVertex(0,0,0)
    glVertex(0,0,10)
    glEnd()

#variables
wheelangle=0
carmove=0
direction=True
car_z=0
wheeld=4

def arrowkeys(key,x,y):
    global car_z
    if key==GLUT_KEY_LEFT:
        if car_z >-4:
            car_z -= 7
    elif key==GLUT_KEY_RIGHT:
        if car_z <-3:
            car_z += 7
    draw()


def draw():
    global wheeld
    global carmove
    global wheelangle
    global direction
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
#    xyz()
    def cubes(c, x, y, z):
        glColor3f(c, c, c)
        glTranslate(x, y, z)
        glScale(.4, .3, .8)
        glutSolidCube(3)
        glLoadIdentity()
#the road
    glColor(0.6, 0.6, 0.5)
    glLoadIdentity()
    glRotate(90, 1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(6, 400)
    glVertex(6, -400)
    glVertex(-6, -400)
    glVertex(-6, 400)
    glEnd()

# the road spliter
    glLoadIdentity()
    glRotate(90, 1, 0, 0)
    glColor(0, 0, 0)
    glTranslate(1, 0, 0)
    glScale(0.1, 10, 0.1)
    glutSolidCube(10)

    #the ball
    glColor(0,0,1)
    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(-carmove, 0, wheeld)
    glutSolidSphere(0.6,100,100)


    cubes(0, -6.5, 0, -z * 21)
    cubes(1, -6.5, 0, -z * 20)
    cubes(0, -6.5, 0, -z * 19)
    cubes(1, -6.5, 0, -z * 18)
    cubes(0, -6.5, 0, -z * 17)
    cubes(1, -6.5, 0, -z * 16)
    cubes(0, -6.5, 0, -z * 15)
    cubes(1, -6.5, 0, -z * 14)
    cubes(0, -6.5, 0, -z * 13)
    cubes(1, -6.5, 0, -z * 12)
    cubes(0, -6.5, 0, -z * 11)
    cubes(1, -6.5, 0, -z * 10)
    cubes(0, -6.5, 0, -z * 9)
    cubes(1, -6.5, 0, -z * 8)
    cubes(0, -6.5, 0, -z * 7)
    cubes(1, -6.5, 0, -z * 6)
    cubes(0, -6.5, 0, -z * 5)
    cubes(1, -6.5, 0, -z * 4)
    cubes(0, -6.5, 0, -z * 3)
    cubes(1, -6.5, 0, -z * 2)
    cubes(0, -6.5, 0, -z * 1)
    cubes(1, -6.5, 0, -z * 0)
    cubes(0, -6.5, 0, z * 1)
    cubes(1, -6.5, 0, z * 2)
    cubes(0, -6.5, 0, z * 3)
    glLoadIdentity()
    cubes(0, 6.5, 0, -z * 21)
    cubes(1, 6.5, 0, -z * 20)
    cubes(0, 6.5, 0, -z * 19)
    cubes(1, 6.5, 0, -z * 18)
    cubes(0, 6.5, 0, -z * 17)
    cubes(1, 6.5, 0, -z * 16)
    cubes(0, 6.5, 0, -z * 15)
    cubes(1, 6.5, 0, -z * 14)
    cubes(0, 6.5, 0, -z * 13)
    cubes(1, 6.5, 0, -z * 12)
    cubes(0, 6.5, 0, -z * 11)
    cubes(1, 6.5, 0, -z * 10)
    cubes(0, 6.5, 0, -z * 9)
    cubes(1, 6.5, 0, -z * 8)
    cubes(0, 6.5, 0, -z * 7)
    cubes(1, 6.5, 0, -z * 6)
    cubes(0, 6.5, 0, -z * 5)
    cubes(1, 6.5, 0, -z * 4)
    cubes(0, 6.5, 0, -z * 3)
    cubes(1, 6.5, 0, -z * 2)
    cubes(0, 6.5, 0, -z * 1)
    cubes(1, 6.5, 0, -z * 0)
    cubes(0, 6.5, 0, z * 1)
    cubes(1, 6.5, 0, z * 2)
    cubes(0, 6.5, 0, z * 3)
    glLoadIdentity()

#water
    glColor(0,0,1)
    glBegin(GL_TRIANGLES)
    glVertex(-1,5,-20)
    glVertex(-6,5,5)
    glVertex(-4,8,3)
    glEnd()

    # the car
    glLoadIdentity()
    glColor(1, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(carmove, 0, car_z + 4)
    glScale(1, 0.25, 0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(carmove, 0, car_z + 4)
    glTranslate(0, 5 * 0.25, 0)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)

    # the wheels
    glColor(0, 0, 1)
    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(carmove, 0, car_z + 4)
    glTranslate(5 * 0.5, -5 * 0.25 * 0.5, 5 * 0.5 * 0.5)
    glRotate(wheelangle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 10)

    glColor(0, 0, 1)
    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(carmove, 0, car_z + 4)
    glTranslate(5 * 0.5, -5 * 0.25 * 0.5, -5 * 0.5 * 0.5)
    glRotate(wheelangle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 10)

    glColor(0, 0, 1)
    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(carmove, 0, car_z + 4)
    glTranslate(-5 * 0.5, -5 * 0.25 * 0.5, -5 * 0.5 * 0.5)
    glRotate(wheelangle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 10)

    glColor(0, 0, 1)
    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(carmove, 0, car_z + 4)
    glTranslate(-5 * 0.5, -5 * 0.25 * 0.5, 5 * 0.5 * 0.5)
    glRotate(wheelangle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 10)

    glutSwapBuffers()

    if direction:
        wheeld=4
        wheelangle += 2
        carmove += 0.009
        if carmove >10 :
            direction=False
    else:
        wheeld=-4
        wheelangle -=2
        carmove -=0.009
        if carmove<-10 :
            direction=True





glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Moving Car ")
myinit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(arrowkeys)
glutMainLoop()