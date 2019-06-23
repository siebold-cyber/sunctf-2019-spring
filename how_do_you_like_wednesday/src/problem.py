import base64
import random
from config import FLAG

flag_arr = list(FLAG)

ord_arr = []
rand_int = random.randint(1, 16)
for i in range(len(flag_arr)):
    char = flag_arr[i]

    ord_char = ord(char) - rand_int
    ord_arr.append(ord_char)

enc_arr = []
for i in range(len(ord_arr)):
    ord_num = ord_arr[i]
    char = chr(ord_num)
    enc_arr.append(char)

enc_flag = ""
for i in range(len(enc_arr)):
    enc_flag += enc_arr[i]

enc_flag = base64.b64encode(enc_flag.encode('utf-8'))

with open('result.txt', 'w') as f:
    f.write('Encrypted flag:\n' + enc_flag.decode())
