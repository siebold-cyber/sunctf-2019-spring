import base64
import random
from Crypto.Cipher import AES
from config import FLAG, BOB_PRIVATE_INT

x = 3
p = 2147483647

block_size = 32

ALICE_PRIVATE_INT = 37749631


def pad64(text):
    if len(text) % 64 == 0:
        return ''
    return '%' * (64 - len(text) % 64)


def alice_calc_id():
    return x ^ ALICE_PRIVATE_INT % p


def bob_calc_id():
    return x ^ BOB_PRIVATE_INT % p


def alice_calc_key(bob_identify):
    return bob_identify ^ ALICE_PRIVATE_INT % p


def bob_calc_key(alice_identify):
    return alice_identify ^ BOB_PRIVATE_INT % p


def encrypt(key):
    flag = FLAG + pad64(FLAG)

    iv = 'ALICE_LOVES_BOB%'.encode()
    key = str(key) + str(key)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    return base64.b64encode(iv + cipher.encrypt(flag))


def main():
    alice_identify = alice_calc_id()
    bob_identify = bob_calc_id()

    alice_key = alice_calc_key(bob_identify)
    bob_key = bob_calc_key(alice_identify)

    if (random.randrange(0, 1)):
        enc_flag = encrypt(alice_key)
    else:
        enc_flag = encrypt(bob_key)

    hex_enc_flag = enc_flag.decode(encoding='UTF-8')

    with open('result.txt', mode='w') as f:
        f.write('Alice\'s identify: ' + str(alice_identify) + '\n'
                'Bob\'s identify: ' + str(bob_identify) + '\n'
                'Encrypted flag: ' + str(hex_enc_flag) + '\n')


if __name__ == '__main__':
    main()
