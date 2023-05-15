"""
    Name:  Byron Dowling
    Class: 5443 2D Python Gaming

    Description:
        - Program is used to crop and derive the sprites from a single
          sprite sheet into multiple individual images.
"""

from PIL import Image
from os import mkdir

mkdir("Assets/Sprites/Shields")
sheet = Image.open("Assets\Sprites\Shields.png")
count = 0

width, height = sheet.size

## Height: 360 Width = 5760
print(f'Height: {height}, Width: {width}')

strideLength = width/12

left = 0
right = strideLength
top = 0
bottom = height

for x in range(12):
    icon = sheet.crop((left, top, right, bottom))
    icon.save("Assets/Sprites/Shields/{}.png".format(count))
    count += 1
    right = right + strideLength
    left += strideLength