from numpy import array


# I manually solved for the key because it never occurred to me to check for ubiquitous English words in the plaintext
def main():
    key = 'exp'
    with open('external_files/cipher.txt', 'r') as f:
        cipher = array(list(map(int, f.read().split(','))))
        key_list = []
        for _ in range(len(cipher)//3):
            key_list.extend([ord(key[0]), ord(key[1]), ord(key[2])])
        key_array = array(key_list)

        plaintext = [i for i in cipher ^ key_array]
        print(''.join(chr(x) for x in plaintext))
        print(sum(plaintext))

    f.close()


if __name__ == '__main__':
    main()
