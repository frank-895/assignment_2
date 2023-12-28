import time
import PIL
from PIL import Image

image = Image.open("chapter1.jpg")
img = image.load()

current_time = int(time.time())

generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

for x in range(0, image.size[0]):
    for y in range(0, image.size[1]):
        img[x,y] = (img[x,y][0] + generated_number, img[x,y][1] + generated_number, img[x,y][2] + generated_number)


image.save("chapter1out.png")

image = Image.open("chapter1out.png")
img = image.load()

sum = 0
for x in range(0, image.size[0]):
    for y in range(0, image.size[1]):
        sum += img[x,y][0]

print(sum)