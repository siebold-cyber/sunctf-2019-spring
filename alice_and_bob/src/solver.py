import base64
from Crypto.Cipher import AES

x = 3
p = 2147483647

block_size = 32

ALICE_PRIVATE_INT = 37749631
ALICE_IDENTIFY = 37749628
BOB_IDENTIFY = 55628524

iv = 'ALICE_LOVES_BOB%'.encode()

hex_enc_flag = 'QUxJQ0VfTE9WRVNfQk9CJdLq31w1QYpG0LgHRMmUh2lplnnO7UN2qnRGKG4NjQ/BVIpmL/dGJtGtOQMT8+r67gatVLn2JlMzQjOVglcwFUg='


def decode(enc_flag):
    int_key = BOB_IDENTIFY ^ ALICE_PRIVATE_INT % p
    key = str(int_key) + str(int_key)

    print('key: ' + key)

    hex_enc_flag = base64.b64decode(enc_flag)

    print('hex_enc_flag: ' + str(hex_enc_flag))

    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(hex_enc_flag[AES.block_size:])


def main():
    dec_flag = decode(hex_enc_flag)
    print('dec_flag: ' + dec_flag.decode(encoding='UTF-8'))


if __name__ == '__main__':
    main()
