import turtle

# Configuración inicial
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(8)
pen.color("red")

# Dibujar los pétalos
for _ in range(6):
    pen.circle(50)  # Radio del pétalo
    pen.left(60)    # Giro entre pétalos

# Cambiar al centro de la flor
pen.penup()
pen.goto(0, -10)
pen.pendown()
pen.color("yellow")
pen.begin_fill()
pen.circle(20)  # Centro de la flor
pen.end_fill()

# Dibujar el tallo
pen.penup()
pen.goto(0, -70)
pen.pendown()
pen.color("green")
pen.pensize(3)
pen.right(90)
pen.forward(100)

# Ocultar la tortuga y finalizar
pen.hideturtle()
turtle.done()