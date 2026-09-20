import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)  # Fastest speed

# Define a list of bright colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


# Define a reusable petal function using two arcs
def draw_petal(t, radius):
  t.begin_fill()
  for _ in range(2):
    t.circle(radius, 60)
    t.left(120)
  t.end_fill()


# Repeat the petal with color rotation to build the pattern
num_petals = 36
for i in range(num_petals):
  pen.color(colors[i % len(colors)])
  draw_petal(pen, 100)
  pen.left(360 / num_petals)

# Finish up
turtle.done()
