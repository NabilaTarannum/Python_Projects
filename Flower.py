from turtle import circle, left, mainloop


def flower():
    for i in range(300):
        circle(190 - i, 90)
        left(90)
        circle(190 - i, 90)
        left(18)


flower()
mainloop()
