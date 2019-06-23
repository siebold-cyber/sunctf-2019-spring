import base64


def decrypt(dec_flag_list, shift_int):
    dec_flag = ''

    for i in range(len(dec_flag_list)):
        ord_num = ord(dec_flag_list[i]) + shift_int
        char = chr(ord_num)
        dec_flag += char

    return dec_flag


def main():
    enc_flag = 'R0lCN0g6byRiU1dcKGJTXWdTKFNkJGRpJShmU2EoZ1ckK1MkWlM8KzZx'

    enc_flag = base64.b64decode(enc_flag.encode('utf-8'))
    enc_flag_arr = list(enc_flag.decode())

    for i in range(16):
        dec_flag = decrypt(enc_flag_arr, i + 1)
        print('Case ' + str(i + 1) + ': ' + dec_flag)


if __name__ == '__main__':
    main()
