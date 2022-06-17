#!/bin/python3

print("Set te square height: ", end='')
height = int( input() )
print()

print("Set te square width: ", end='')
width = int( input() )
print()

row = 0
while row < height:
    column = 0
    while column < width:
        print("X ", end='')
        column = column + 1
    print()
    row = row + 1