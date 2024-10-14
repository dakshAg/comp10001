# Note that this code has severe code quality issues.
# It is only meant to be a simple example of how to use the PIL library.
# The code is not meant to be used in a production environment.

from PIL import Image

BLOCK_SIZE = 100
IMAGE_FORMAT = "RGBA"
GREEN_COLOUR = (0, 255, 0, 255)

lawnmower_icon = Image.open('lawnmower.png')
lawnmower_icon = lawnmower_icon.resize((100, 100))

backyard = [
    ["-", "+", "-", "+"],
    ["-", "-", "-", "+"],
    ["-", "+", "+", "+"]
]
lawnmower = [0, 3]

bar = Image.new(IMAGE_FORMAT, (len(backyard[0]) * BLOCK_SIZE,
                               len(backyard) * BLOCK_SIZE), (255, 255, 255, 255)
                )


def fill_with_colour(x_start, y_start, x_end, y_end, color):
    for i in range(x_start, x_end):
        for j in range(y_start, y_end):
            bar.putpixel((i, j), color)


def put_image(x_start, y_start, image):
    for i in range(image.width):
        for j in range(image.height):
            if image.getpixel((i, j))[3] != 0:
                bar.putpixel((x_start + i, y_start + j), image.getpixel((i, j)))


for i in range(len(backyard)):
    for j in range(len(backyard[i])):
        if backyard[i][j] == "+":
            fill_with_colour(j * 100, i * 100, j * 100 + 100, i * 100 + 100, GREEN_COLOUR)
        else:
            fill_with_colour(j * 100, i * 100, j * 100 + 100, i * 100 + 100, (255, 255, 255))

        if i == lawnmower[0] and j == lawnmower[1]:
            put_image(j * 100, i * 100, lawnmower_icon)

bar.save('backyard.png')
