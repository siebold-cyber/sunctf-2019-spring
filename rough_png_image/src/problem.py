from PIL import Image
from config import HTML

list_html = list(HTML)

asc_list = []

for i in range(len(list_html)):
    asc_char = ord(list_html[i])
    asc_list.append(asc_char)

if len(asc_list) != 8100:
    for i in range(8100 - len(asc_list)):
        asc_list.append(0)

img = Image.new('RGB', (90, 90), (255, 255, 255))

idx = 0
for i in range(90):
    for j in range(90):
        img.putpixel((j, i), (asc_list[idx], 0, 0))
        idx += 1

img.save('problem.png')
