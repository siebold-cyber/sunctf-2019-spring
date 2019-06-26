from PIL import Image
import numpy as np

img = Image.open('problem.png')
width, height = img.size

img_pixels = []
for y in range(height):
    for x in range(width):
        img_pixels.append(img.getpixel((x, y)))

img_pixels = np.array(img_pixels)
print(img_pixels.tolist())

gen_pixels = np.full((height, 3), 255)

arr = gen_pixels - img_pixels
print(arr.tolist())

num_list = []

for i in range(len(arr)):
    num = arr[i][0] + arr[i][1] + arr[i][2]
    num_list.append(num)

print(num_list)

flag = ""

for i in range(len(num_list)):
    char = chr(num_list[i])
    flag += char

print(flag)
