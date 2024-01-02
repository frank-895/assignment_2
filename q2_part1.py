# This program changes the pixel values of an image, and finds the sum of all red
# pixel values of the altered image.

import time
import PIL
from PIL import Image

image = Image.open("chapter1.jpg")
img = image.load() # opening image for alteration


## THIS SECTION IS TAKEN FROM THE TASK SHEET
## ___________________________________________________
current_time = int(time.time())

generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10
## _________________________________________________


for x in range(0, image.size[0]): # iterate through rows
    for y in range(0, image.size[1]): # iterate through columns
        # change each pixel by adding generated number
        img[x,y] = (img[x,y][0] + generated_number, img[x,y][1] + generated_number, img[x,y][2] + generated_number)


image.save("chapter1out.png") # save image

image = Image.open("chapter1out.png") # reopen altered image
img = image.load()

sum = 0
for x in range(0, image.size[0]): # iterate through rows
    for y in range(0, image.size[1]): # iterate through columns
        sum += img[x,y][0] # adding only red pixel values to sum 

print(sum)