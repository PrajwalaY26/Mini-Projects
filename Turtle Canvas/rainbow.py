import turtle

sc = turtle.Screen()

pen = turtle.Turtle()

def semi_circle(col, rad, val):
    pen.color(col)
    pen.circle(rad, -180)
    pen.up()
    pen.setpos(val, 0)
    pen.down()
    pen.right(180)

#set the colors for drawing
col = ['violet', 'indigo', 'blue',
       'green', 'yellow','orange',
       'red']

#setup the screen features 
sc.setup(600,600)
sc.bgcolor('black')   

#setup the turtle features
pen.right(90)
pen.width(10)
pen.speed(7)

#loop to draw 7 semicircles
for i in range(7):
    semi_circle(col[i], 10*(i+8), 
                -10*(i+1))
    
#Hide the turtle
pen.hideturtle()    