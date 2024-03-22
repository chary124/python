import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
for i in range(5):
    for colours in ["red","green","indigo","orange","blue","purple","violet"]:
        turtle.color(colours)
        turtle.circle(90)
        turtle.right(145)
        
turtle.hideturtle()        