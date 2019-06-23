from config import FLAG


def gen_hash(text):
    hash = 0
    text_list = list(text)

    for i in range(len(text_list)):
        ord_char = ord(text_list[i])
        hash += int(ord_char)

    return hash


def main():
    hash = gen_hash(FLAG)

    with open('result.txt', mode='w') as f:
        f.write('Hash: ' + str(hash))


if __name__ == '__main__':
    main()
