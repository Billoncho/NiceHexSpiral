# NiceHexSpiral.py
# Billy Ridgeway
# Creates a colorful hex spiral.

import turtle               # Import turtle graphics.

# Create a list of colors for the spiral.
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

t = turtle.Pen()            # Creates a new turtle called t.
t.speed(0)                  # Set the pen speed to fast.
turtle.bgcolor('black')     # Set the background to black.

# Create a for loop.
for x in range(360):        # Set the value of x to 360.
    t.pencolor(colors[x%6]) # Cycle through the pen colors.
    t.width(x/100+1)        # Set the width of the pen to the value of x
                            # divided by 100 plus 1.
    t.forward(x)            # Move the pen forward by the value of x.
    t.left(59)              # Move the pen left by 59 degrees.
