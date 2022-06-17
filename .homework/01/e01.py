import tkinter, turtle
kilpikonna = turtle.Turtle()
kilpikonna.shape("turtle")

i = 0
while i < 4:
    kilpikonna.forward(50)
    kilpikonna.left(90)
    i = i + 1

tkinter.mainloop()