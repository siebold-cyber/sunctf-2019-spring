import base64
import zlib
from config import FLAG

text = FLAG.encode('utf-8')

for i in range(64):
    text = zlib.compress(text)
    text = base64.b64encode(text)

with open('result.txt', mode='w') as f:
    f.write('Result:\n' + text.decode('utf-8'))
