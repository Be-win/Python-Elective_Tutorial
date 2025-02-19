import turtle

def draw_star(t, size):
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def draw_stars(t, count, star_size, distance):
    center = (0, 0)
    for i in range(count):
        t.penup()
        t.goto(center)
        angle = i * (360 / count)
        t.setheading(angle)
        t.forward(distance)
        t.setheading(t.heading() - 36)
        t.pendown()
        draw_star(t, star_size)
        t.penup()

tur = turtle.Turtle()
tur.shape("turtle")
tur.speed(2)
tur.fillcolor("yellow")
tur.pencolor("black")


draw_stars(tur, 5, 100, 200)

tur.hideturtle()
turtle.done()
