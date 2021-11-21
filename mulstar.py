import turtle
a=turtle.Turtle()
a.showturtle()
a.shape("turtle")
a.speed(30)
a.begin_fill()


for x in range(30):
  a.forward(20)
  a.left(5*x)
  a.color("purple")
  a.backward(20)
  a.right(10*x)
  a.color("blue")
a.fillcolor("yellow")
a.end_fill()
a.color("red")
turtle.done()