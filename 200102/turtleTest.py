# import turtle
#
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
#
# turtle.done()

from turtle import *

# speed(10)
# width(2)
# color("red")

# forward(100)
# left(90)
# forward(100)
#
# done()

# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
#
# for i in range(500): # this "for" loop will repeat these functions 500 times
#     forward(i)
#     left(91)

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

penup()
left(90)
forward(30)
write("Momo <3 Heechul")
backward(30)
pendown()

for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(59)

done()
# https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md
