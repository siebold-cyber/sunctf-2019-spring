from config import FLAG


def convert_to_ASCII(arr):
    ord_arr = []

    for i in range(len(arr)):
        char = arr[i]
        ord_char = ord(char)
        ord_arr.append(ord_char)

    return ord_arr


def main():
    enc_flag = ''
    flag_arr = list(FLAG)

    ord_arr = convert_to_ASCII(flag_arr)

    for i in range(len(ord_arr)):
        bin_str = format(ord_arr[i], '08b')
        enc_flag += bin_str

    with open('result.txt', 'w') as f:
        f.write('Encrypted flag:\n' + enc_flag + '\n')


if __name__ == '__main__':
    main()
