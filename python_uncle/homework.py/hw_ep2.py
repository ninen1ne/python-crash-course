# Requirement for homework: draw 10 squares with random position
# for each one and random sizes, colors too.

# Norawee- 27/3/2024 :D

import turtle 
import random 

# create a list of colors for random.
colors = ['black', 'green', 'blue', 'orange', 'crimson', 'pink', 'violet', 'gold']
tao = turtle.Turtle()
tao.shape('turtle')
tao.speed(8)

# loop for create 10 squares 
# We will set random value for each variable here.
for square in range(10):
    count = square + 1 
    length = random.randint(30,100)
    square_width = random.randint(1,10)
    x_position= random.randint(-300,300)
    y_position = random.randint(-300,300)
    tao.penup()
    # .penup() tell tao to pen up before move to new position
    # so it will didn't draw when move to new position.
    tao.goto(x_position, y_position)
    tao.pendown()
    # .pendown() tell tao to start drawing square.
    print(f'square count: {count}')
    

    # create each individual square.
    # same square should have same side width.
    for side in range(4):
        color = random.choice(colors)
        tao.color(color) # Random color each side.
        tao.pensize(square_width)
        tao.forward(length)
        tao.left(90)
    
    
turtle.mainloop()
