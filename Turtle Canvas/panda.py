#Draw a Panda using Turtle Graphics
#Import turtle package
import turtle

#creating a turtle object(pen)
pen = turtle.Turtle()

#defining method to draw a colored circle
#with a dynamic radius
def ring(col, rad):

    #set the fill
    pen.fillcolor(col)

    #start filling the color
    pen.begin_fill()

    #draw the circle
    pen.circle(rad)

    #ending the filling of the color
    pen.end_fill()

#draw ears
# draw first ear
pen.up()
pen.setpos(-35, 95)
pen.down()
ring('black', 15)

#draw second ear
pen.up()
pen.setpos(35, 95)
pen.down()
ring('black', 15)

#draw face
pen.up()
pen.setpos(0,35)
pen.down()
ring('white',40)

#draw eyes black

#draw first eye
pen.up()
pen.setpos(-18,75)
pen.down
ring('black',8)

#draw second eye
pen.up()
pen.setpos(18,75)
pen.down()
ring('black', 8)

#draw nose
pen.up()
pen.setpos(0,55)
pen.down
ring('black',5)

#draw mouth
pen.up()
pen.setpos(0,55)
pen.down()
pen.right(90)
pen.circle(5,180)
pen.up()
pen.setpos(0,55)
pen.down()
pen.left(360)
pen.circle(5,-180)
pen.hideturtle()