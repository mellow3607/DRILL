import turtle

turtle.penup()
turtle.goto(-200,-200)
#turtle.pendown()
#turtle.forward(500)
count = 0
x = -200
y = -200

while (count < 6 ) :
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    y = y +100
    turtle.goto(x,y)

    count = count + 1

turtle.left(90)
turtle.penup()
turtle.goto(-200,-200)
y = -200
count = 0

while (count < 6 ) :
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    x = x +100
    turtle.goto(x,y)

    count = count + 1



turtle.exitonclick()
            

      
        
		
