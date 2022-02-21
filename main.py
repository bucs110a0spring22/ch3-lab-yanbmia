import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
#Race 1
steps = random.randrange(1,100)

michelangelo.forward(steps)
leonardo.forward(steps)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

#Race 2
for _ in range(10):
  steps = random.randrange(1,10)
  michelangelo.forward(steps)

  steps = random.randrange(1,10)
  leonardo.forward(steps)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here
leonardo.pd()
sides = [3,4,6,9,12]

for shape in sides:
  angles = 360 / shape
  for i in range(shape):
    leonardo.forward(20)
    leonardo.right(angles)
  else:
    leonardo.clear()

  
window.exitonclick()
