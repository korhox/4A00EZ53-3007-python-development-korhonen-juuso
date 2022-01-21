import tkinter, turtle
kilpikonna = turtle.Turtle()
kilpikonna.shape("turtle")

sade = 10
while sade < 100:
    kilpikonna.circle(sade)
    sade = sade + 5

tkinter.mainloop()