from PIL import Image
import numpy as np
from config import FLAG

flag_arr = list(FLAG)
asc_flag_arr = []

for i in range(len(flag_arr)):
    asc_char = ord(flag_arr[i])
    asc_flag_arr.append(asc_char)

asc_dec_arr = []

for i in range(len(asc_flag_arr)):
    asc_int = asc_flag_arr[i]
    asc_int_thirds = asc_int // 3
    if asc_int % 3 == 0:
        asc_int_last = asc_int_thirds
    elif asc_int % 3 == 1:
        asc_int_last = asc_int_thirds + 1
    else:
        asc_int_last = asc_int_thirds + 2
    asc_decrement_arr = [asc_int_thirds, asc_int_thirds, asc_int_last]
    asc_dec_arr.append(asc_decrement_arr)

asc_dec_arr = np.array(asc_dec_arr, dtype=np.uint8)

original_arr = [[255, 255, 255]] * len(FLAG)
original_arr = np.array(original_arr, dtype=np.uint8)

arr = original_arr - asc_dec_arr
arr = arr.tolist()

img = Image.new('RGB', (1, len(FLAG)), (255, 255, 255))

for i in range(len(FLAG)):
    img.putpixel((0, i), (arr[i][0], arr[i][1], arr[i][2]))

img.save('problem.png')
