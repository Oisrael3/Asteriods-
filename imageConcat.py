"""
    Name:  Byron Dowling
    Class: 5443 2D Python Gaming

    Description:
        - Program is used to concatenate images together since our sprite
          ship animations are separated into different parts
"""

import os
from PIL import Image, ImageDraw


ShipBody = "Assets\Sprites\Spaceships\Spaceship_cropped.png"
Engine = "Assets\Sprites\Spaceships\SpaceshipEngine_cropped.png"
Effect = r"Assets\Sprites\Spaceships\Idle\3.png"
LeftRockets = "Assets\Sprites\Left_Rockets.png"
RightRockets = "Assets\Sprites\Right_Rockets.png"

spaceship_ImgLink = ""

image1 = Image.open(ShipBody)
image2 = Image.open(Engine)
image3 = Image.open(Effect)
LR = Image.open(LeftRockets)
RR = Image.open(RightRockets)

image1 = image1.resize((125,125))
image2 = image2.resize((50,50))
image3 = image3.resize((100,20))

LR = LR.resize((38,38))
RR = RR.resize((38,38))


image1_size = image1.size
image2_size = image2.size
image3_size = image3.size

LR_size = LR.size
RR_size = RR.size


new_image = Image.new('RGB', (image1_size[0], image1_size[1] + image2_size[1] + image3_size[1]), (0,0,0))
new_image.paste(image2,(int(image1_size[0]/3.35), image1_size[1]))
new_image.paste(image1, (0,10))
new_image.paste(LR, (0,32))
new_image.paste(RR, (90,32))
new_image.paste(image3, (int(new_image.size[0]/8) ,new_image.size[1] - 20))
new_image.save("Spaceship_Weaponized.png", "PNG")
new_image.show()

