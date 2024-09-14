import turtle

# create a Turtle Screen object
screen = turtle.Screen()
# set the window title and background color
screen.title("Azerbaijan!")
screen.bgcolor("black") 

# create a turtle object
flag = turtle.Turtle()
flag.speed(0)

# flag dimensions
flag_height = 600
flag_width = flag_height*2
stripe_height = flag_height/3

# flag colours
flag_colours = ['#00B5E2','#EF3340','#509E2F']

# draw function for stripe
def draw_stripe(colour, y):
    flag.penup()
    flag.goto(-flag_width/2, y)
    flag.pendown()
    flag.color(colour)
    flag.begin_fill()
    flag.forward(flag_width)
    flag.right(90)
    flag.forward(stripe_height)
    flag.right(90)
    flag.forward(flag_width)
    flag.right(90)
    flag.forward(stripe_height)
    flag.right(90)
    flag.end_fill()

# draw function for star
def draw_star2():
    # Adjust the starting position to center the star
    flag.goto(flag_height / 30 *2, 0)
    flag.setheading(45/2)  # This rotates the entire star by 45 degrees
    flag.pendown()
    flag.color('white')
    flag.begin_fill()
    n = 4  # An 8-pointed star has 8 points
    angle = 180 - 180/n
    for i in range(2 * n):  # This loop will cover the entire star twice
        flag.forward(flag_height / 8)  # The length of each star's arm
        flag.right(angle)
    flag.end_fill()

    flag.penup()
    flag.goto(flag_height / 30 *4.5, -flag_height / 26)
    flag.pendown()
    flag.color('white')
    flag.begin_fill()
    flag.circle(flag_height / 25)
    flag.end_fill()


# draw function for crescent
def draw_crescent():
    # Draw the white part of the crescent
    flag.penup()
    flag.goto(-flag_height/30,-flag_height/10*3/2)
    flag.pendown()
    flag.color('white')
    flag.begin_fill()
    flag.circle(flag_height/10*3/2)
    flag.end_fill()

    # draw the red part of the crescent
    flag.penup()
    flag.goto(0,-flag_height/4/2)
    flag.pendown()
    flag.color('#EF3340')
    flag.begin_fill()
    flag.circle(flag_height/4/2)
    flag.end_fill()

# execute functions
start_y = stripe_height*1.5
for colour in flag_colours:
    draw_stripe(colour,start_y)
    start_y -= stripe_height
draw_crescent()
draw_star2()


flag.hideturtle()
screen.mainloop()