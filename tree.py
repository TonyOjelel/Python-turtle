import turtle

t = turtle.Turtle()
t.speed(0)
t.left(90)

def branch(length, t):

    if length <= 5:
        return
    t.forward(length)
    t.right(20)
    branch(length - 15, t)
    t.left(40)
    branch(length - 15, t)
    t.right(20)
    t.backward(length)

branch(100, t)
turtle.mainloop()