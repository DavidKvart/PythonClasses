import turtle

# Set up the screen
wn = turtle.Screen()
wn.setup(width=600, height=300)

# Create turtle for drawing the flag
flag = turtle.Turtle()
flag.speed(0)

# Function to draw a rectangle with a given color and size
def draw_rectangle(color, width, height):
    flag.begin_fill()
    flag.fillcolor(color)
    for _ in range(2):
        flag.forward(width)
        flag.left(90)
        flag.forward(height)
        flag.left(90)
    flag.end_fill()

# Function to draw the crescent
def draw_crescent(position, radius):
    flag.penup()
    flag.goto(position)
    flag.pendown()
    flag.color('white')
    flag.begin_fill()
    flag.circle(radius)
    flag.end_fill()

# Function to draw the eight-pointed star
def draw_star(position, size):
    flag.penup()
    flag.goto(position)
    flag.setheading(0)
    flag.pendown()
    flag.color('white')
    flag.begin_fill()
    for _ in range(8):
        flag.forward(size)
        flag.left(135)
    flag.end_fill()

# Draw the blue rectangle
flag.penup()
flag.goto(-300, 50)
flag.pendown()
draw_rectangle("#00b9e4", 600, 100)

# Draw the red rectangle
flag.penup()
flag.goto(-300, -50)
flag.pendown()
draw_rectangle("#ed2939", 600, 100)

# Draw the green rectangle
flag.penup()
flag.goto(-300, -150)
flag.pendown()
draw_rectangle("#00a651", 600, 100)

# Draw the crescent moon
draw_crescent((-80, -35), 40)

# Draw the eight-pointed star
draw_star((-40, 15), 80)

# Hide the turtle and display the result
flag.hideturtle()

# Keep the window open until closed by the user
wn.mainloop()
