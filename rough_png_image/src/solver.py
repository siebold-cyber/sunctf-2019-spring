from PIL import Image

img = Image.open('problem.png')
width, height = img.size

img_pixels = []
for y in range(height):
    for x in range(width):
        img_pixels.append(img.getpixel((x, y)))

num_list = []
for i in range(len(img_pixels)):
    num = img_pixels[i][0]
    num_list.append(num)

print(num_list)

gen_html = ""
for i in range(len(num_list)):
    char = chr(num_list[i])
    gen_html += char

print(gen_html)

with open('output.html', 'w') as f:
    f.write(gen_html)
