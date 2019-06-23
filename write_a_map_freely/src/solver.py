import math


def unAki(arr1):
    arr = [0] * len(arr1)
    arr2 = [116, 104, 105, 115, 95, 105, 115, 95, 116, 104, 51, 95, 98, 114,
            117, 102, 95, 116, 51, 120, 116, 95, 102, 48, 114, 95, 121, 48,
            117, 114, 95, 102, 108, 97, 103, 37]

    for i in range(len(arr1)):
        arr[i] = arr1[i] - arr2[i]

    return arr


def unKanako(arr):
    arr_int = [int(n) for n in arr]

    for i in range(len(arr)):
        if arr_int[i] % 3 == 0:
            arr_int[i] -= 9

    return arr_int


def unAsuka(arr):
    arr_int = [int(n) for n in arr]

    for i in range(len(arr)):
        if arr_int[i] % 2 == 0:
            arr_int[i] = math.floor(arr_int[i] / 2)

    return arr_int


def decrypt():
    flag = '199198192364179175476417345441163400416217424210156233332180211388412200448405453143174441380217168222436333'

    arr = [flag[i: i + 3] for i in range(0, len(flag), 3)]
    print(arr)

    arr = unKanako(arr)
    print(arr)

    arr = unAsuka(arr)
    print(arr)

    arr = unAki(arr)
    print(arr)

    dec_flag = ''

    for i in arr:
        chr_str = chr(i)
        dec_flag += chr_str

    return dec_flag


if __name__ == '__main__':
    dec_flag = decrypt()
    print(dec_flag)
