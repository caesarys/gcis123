"""
Students: Meera Alshara, Syed Hossain, Caesar Al Shdaifat
contribution of Syed: hexagon function & set pos function
contribution of Caesar: square function & main
contribution of Meera: circle function, comment/docstring & pattern function
Description: this program will draw three different shapes hoxagon, circle, and square
using the turtle module, and further prompts the user to choose whichever color to be filled 
for each shape ,these three shapes are specificily programmed with different coordinates 

Repository Links:
Syed : https://github.com/LagSpikeee/GCIS-123/blob/main/group8-activity1.py
Meera : https://github.com/meeralshara/gcis123/blob/main/group8-activity1.py
Caesar : https://github.com/caesarys/gcis123/blob/main/group8-activity1.py
"""

import turtle
'''
the following functions below are used to  make three different shapes
with specified colors given by the users input
'''
turtle.bgcolor('Light Blue')
turta = turtle.Turtle()


def setPos(turta, x, y):
    '''
    this function sets the cursor to the starting point/position in every function
    in different coordinates without having to repeat commands multiple times
    '''
    turta.penup()          
    turta.goto(x, y)    
    turta.pendown()     
    #turta.speed(0) #sets the fastest speed to cursor

def hexagon(turta, hexa_color, border_color):
    """
    this function (hexagon) will use turta to draw a hexagon three times on 50 units
    and uses the set pos function to draw on different coordinates
    on the canvas window, the user will be able to input the color wanted for this shape
    """

    setPos(turta, -210, 70)
    turta.pencolor(border_color)
    turta.setheading(0)
    turta.fillcolor(hexa_color)
    turta.begin_fill()
    turta.forward(50)
    turta.left(360/6)
    turta.forward(50)
    turta.left(360/6) 
    turta.forward(50)
    turta.left(360/6) 
    turta.forward(50)
    turta.left(360/6) 
    turta.forward(50)
    turta.left(360/6) 
    turta.forward(50)
    turta.left(360/6) 
    turta.end_fill()
    setPos(turta, -150, -40)
    turta.setheading(0)
    turta.begin_fill()
    turta.forward(50)
    turta.left(360/6)
    turta.forward(50)
    turta.left(360/6)
    turta.forward(50)
    turta.left(360/6)
    turta.forward(50)
    turta.left(360/6)
    turta.forward(50)
    turta.left(360/6)
    turta.forward(50)
    turta.left(360/6)
    turta.end_fill()
    setPos(turta, -90, -150)
    turta.setheading(0)
    turta.begin_fill()
    turta.forward(50)
    turta.left(360/6)
    turta.forward(50)
    turta.left(360/6)
    turta.forward(50)
    turta.left(360/6)
    turta.forward(50)
    turta.left(360/6)
    turta.forward(50)
    turta.left(360/6)
    turta.forward(50)
    turta.left(360/6) 
    turta.end_fill()

def circle(turta, circle_color, border_color):
    """
    this function (circle) will draw a circle three times by passing in setpos 
    inside the function to create different coordinates, 
    the user will be able to input the color wanted
    """
    setPos(turta, -50, 170) 
    turta.pencolor(border_color)
    turta.fillcolor(circle_color)
    turta.begin_fill()
    turta.circle(-50)
    turta.end_fill()
    setPos(turta, 10, 60)
    turta.begin_fill()
    turta.circle(-50)
    turta.end_fill()
    setPos(turta, 70, -50)
    turta.begin_fill()
    turta.circle(-50)
    turta.end_fill()

def square(turta, square_color, border_color):
    """
    the function (square) will draw a 90 unit square and passes setpos function 
    with different coordinates ,the user will be able to input the color 
    wanted for this shape
    """
    turta.penup()
    turta.goto(0, 0)
    turta.pendown()
    setPos(turta, 40, 75) 
    turta.pencolor(border_color)
    turta.fillcolor(square_color)
    turta.begin_fill()
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.end_fill()
    turta.left(90)
    setPos(turta, 100, -35)
    turta.begin_fill()
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.end_fill()
    turta.left(90)
    setPos(turta, 160, -145)
    turta.begin_fill()
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.end_fill()
    turta.left(90)

'''this function (pattern) organizes how turtle draws the shapes starting from the 
    drawing to the color of the shape and pen used'''
def pattern(turta, hexa_color, circle_color, square_color, border_color):
    hexagon(turta, hexa_color, border_color)
    circle(turta, circle_color, border_color)
    square(turta, square_color, border_color)

def main():
    """
    the main function will call the functions (hexagon, square, circle, pattern) with 
    variables that assign the user to input colors in
    """
    pattern (turtle, input("Enter the color of hexagon: "),
    input("Enter the color for the circle: "),
    input("Enter the color for the square: "),
    input("Enter the color for borders of the shapes: "))
    turtle.done()

main()
