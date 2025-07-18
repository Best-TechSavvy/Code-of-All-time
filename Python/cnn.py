from PIL import Image
import numpy as np
import finnal
import copilot
import cv2

img = Image.open("botter2.png")
pixels = img.load()

width, height = img.size
possible = []
column = []
for y in range(height):
    row = []
    for x in range(width):
        r, g, b, h  = img.getpixel((x, y))
        brightness = (r + g + b) // 3
        if brightness > 70:
            row.append(1)
            pixels[x, y] = (255, 255, 255)
            possible.append((x,y))

        elif brightness < 70:
            row.append(0)
            pixels[x, y] = (0, 0, 0)
    #print(row) 
    #column 2d array of the image that stores the brightness of each pixel
    column.append(row)

img.save("modified.png")

#possible is a list of cordinates of all the pixels that are white
print(possible) 
print(len(possible))
#print(int(len(column)*len(row)))

#contour is a function that takes a list of coordinates and returns a list of groups of coordinates that are touching each other
white = copilot.contour(possible) 
print(white)
copilot.colorize_groups("modified.png", white, "colored.png")
possible = copilot.extract_pixels(possible, white)

for i in possible:
    print(i)
'''
filter = [[0, 1, 0],
          [0, 1, 0],
          [0, 1, 0]]

vertical = finnal.conv(filter, column)
#print(vertical)

filter = [[0, 0, 0],
          [1, 1, 1],
          [0, 0, 0]]
horizontal = finnal.conv(filter, column)
print(horizontal)

filter1 = [[0, 0, 0, 1, 1, 1, 0, 0, 0,],
           [0, 0, 0, 1, 1, 1, 0, 0, 0,],
           [0, 0, 0, 1, 1, 1, 0, 0, 0,],
           [0, 0, 0, 1, 1, 1, 0, 0, 0,],
           [0, 0, 0, 1, 1, 1, 0, 0, 0,],
           [0, 0, 0, 1, 1, 1, 0, 0, 0,],
           [0, 0, 0, 1, 1, 1, 0, 0, 0,],
           [0, 0, 0, 1, 1, 1, 0, 0, 0,],
           [0, 0, 0, 1, 1, 1, 0, 0, 0,]]
'''