import turtle
import random


def static_tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        static_tree(branchLen - 15, t)
        t.left(40)
        static_tree(branchLen - 15, t)
        t.right(20)
        t.backward(branchLen)


def random_tree(branchLen, t):
    if branchLen > 5:
        angle = branchAngle()
        t.color(branchColor(branchLen))
        t.pensize(branchThickness(branchLen))
        t.forward(branchLen)
        t.right(angle)
        random_tree(branchLength(branchLen), t)
        t.color(branchColor(branchLen))
        t.pensize(branchThickness(branchLen))
        t.left(angle * 2)
        random_tree(branchLength(branchLen), t)
        t.color(branchColor(branchLen))
        t.pensize(branchThickness(branchLen))
        t.right(angle)
        t.penup()
        t.backward(branchLen)
        t.pendown()


def branchLength(branchLen):
    return branchLen - random.randint(4, 16)


def branchAngle():
    return random.randint(12, 36)


def branchThickness(branchLen):
    thick = 0
    if branchLen > 50:
        thick = 6
    elif branchLen > 25:
        thick = 5
    else:
        thick = 3
    return thick


def branchColor(branchLen):
    color = ''
    if branchLen > 50:
        color = '#CD853F'  # Peru brown
    elif branchLen > 25:
        color = '#D2B48C'  # Tun brown
    else:
        color = '#ADFF2F'  # GreenYellow
    return color


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(250)
    t.down()
    t.color("green")
    # static_tree(75, t)
    random_tree(85, t)
    t.speed(speed="fastest")
    myWin.exitonclick()


main()
