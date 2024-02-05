import turtle

def draw_car_body():
    turtle.color("blue")
    turtle.penup()
    turtle.goto(-50, -20)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(100)
        turtle.circle(20, 180)
    turtle.end_fill()

def draw_car_roof():
    turtle.color("blue")
    turtle.penup()
    turtle.goto(-50, 55)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(100)
    turtle.end_fill()

def draw_wheels():
    turtle.color("black")
    turtle.penup()
    turtle.goto(-30, -20)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(20)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(40, -20)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(20)
    turtle.end_fill()

def draw_car():
    draw_car_body()
    draw_car_roof()
    draw_wheels()

turtle.speed(2)
turtle.hideturtle()
turtle.bgcolor("white")

draw_car()

turtle.done()
