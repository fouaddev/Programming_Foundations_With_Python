import turtle

def draw_flower_ball():
    play_ground = turtle.Screen()
    play_ground.bgcolor("gray")
    fred = turtle.Turtle()
    fred.shape("arrow")
    fred.color("blue")
    fred.speed(9)
    for i in range(72):
        fred.circle(100)
        fred.right(5)
    fred.exitonclick()

draw_flower_ball()
