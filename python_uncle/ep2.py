# Today I've learned about builtin module in python call turtle use for render graphic in python.
# And learn how to combine it with a for loop to draw a simple graphic.
# Document about this module: https://docs.python.org/3/library/turtle.html
# Norawee: 27/3/2024

import turtle 
import random 

# Use for start running GUI(Graphical user interface)
tao = turtle.Turtle()

# Set shape of icon to turtle.
tao.shape('turtle')

tao.pensize(3)

tao.speed(5)

# Define a list of colors for changing turtle color.
colors = ['red', 'green', 'blue', 'yellow']

# Create square using tao and for loop.
for color in colors:
    tao.color(color)
    print('the color of turtle is: ' + color)
    tao.forward(100)
    tao.left(90)

tao.goto(-200,-200)

# Create circle with random color using turtle and random module.
for i in range(10):
    count = i + 1 
    print("rotate count : " + str(count))
    color = random.choice(colors)
    tao.color(color)
    tao.circle(50) # In the parenthesis the argument circle function needed is radius.
    tao.left(36)
    tao.pensize(random.randint(1,10)) # random size of pen using random function inside argument for pensize function.

tao.goto(200,-100)
tao.pensize(3)

# Create circle with random color and size.
for i in range(10):
    color = random.choice(colors)
    size = random.randint(50,100)
    print('color: ' + color)
    print('radius of circle: ' + str(size) + ' px')
    tao.color(color)
    tao.circle(size)
    tao.left(36)

# Keep screen still as long as program running.
turtle.mainloop()

