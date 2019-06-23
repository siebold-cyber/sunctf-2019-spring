from config import FLAG


def init():
    arr = [FLAG[i: i + 6] for i in range(0, len(FLAG), 6)]
    ord_map = []

    for i in arr:
        ord_arr = []
        for j in i:
            ord_num = ord(j)
            ord_arr.append(ord_num)
            if (len(ord_arr) == 6):
                ord_map.append(ord_arr)

    return ord_map


def aki(m1):
    m = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    m2 = [[116, 104, 105, 115, 95, 105], [115, 95, 116, 104, 51, 95],
          [98, 114, 117, 102, 95, 116], [51, 120, 116, 95, 102, 48],
          [114, 95, 121, 48, 117, 114], [95, 102, 108, 97, 103, 37]]

    for i in range(len(m)):
        for j in range(len(m)):
            m[i][j] = m1[i][j] + m2[i][j]

    return m


def asuka(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] % 2 == 0:
                m[i][j] *= 2

    return m


def kanako(m):
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] % 3 == 0:
                m[i][j] += 9

    return m


def joint(m):
    enc_m = ''

    for i in range(len(m)):
        jointed_str = ''.join(map(str, m[i]))
        enc_m += jointed_str

    return enc_m


def encrypt():
    m = init()
    m = aki(m)
    m = asuka(m)
    m = kanako(m)
    enc_str = joint(m)

    return enc_str


if __name__ == '__main__':
    enc_flag = encrypt()

    with open('result.txt', mode='w') as f:
        f.write('Encrypted flag:\n' + enc_flag + '\n')
