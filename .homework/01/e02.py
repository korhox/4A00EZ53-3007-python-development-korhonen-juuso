import tkinter, turtle
kilpikonna = turtle.Turtle()
kilpikonna.shape("turtle")

print("Mihin suuntaan haluat siirtää kilpikonnaa?")
print("Kirjoita oikea, vasen, ylös tai alas (o, v, y, a)")

while True:
    suunta = input()

    if suunta == "oikea" or suunta == "o":
        kilpikonna.setheading(0)
        kilpikonna.forward(50)

    if suunta == "vasen" or suunta == "v":
        kilpikonna.setheading(180)
        kilpikonna.forward(50)

    if suunta == "ylös" or suunta == "y":
        kilpikonna.setheading(90)
        kilpikonna.forward(50)

    if suunta == "alas" or suunta == "a":
        kilpikonna.setheading(270)
        kilpikonna.forward(50)


tkinter.mainloop()