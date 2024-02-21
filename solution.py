#!/usr/bin/python3.11

import sys

TEXT_PATH = 'text.txt'
KEY_PATH = 'key.txt'

PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

LSH_TABLE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
IP_INVERSE = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
E_SELECTION = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

S1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], \
      [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], \
      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], \
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

S2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], \
      [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5], \
      [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15], \
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

S3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8], \
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1], \
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7], \
      [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

S4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], \
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9], \
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], \
      [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

S5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9], \
      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6], \
      [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14], \
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

S6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], \
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], \
      [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6], \
      [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

S7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1], \
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6], \
      [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2], \
      [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

S8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], \
      [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2], \
      [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8], \
      [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]



def left_shift(b: list[str], n: int) -> list[str]:
    orig_key = b.copy()
    for i in range(len(b)):
        b[i] = orig_key[(i+n)%len(b)]
    return b



def XOR(x: list[str], y: list[str]) -> list[str]:
    z = list()
    for a, b in zip(x, y):
        if a != b:
            z.append('1')
        else:
            z.append('0')
    return z



def f_function(R: list[str], K: list[str]) -> list[str]:

    # Put R through the E bit selection table
    R_48_bits = [R[E_SELECTION[i]-1] for i in range(len(E_SELECTION))]

    # Do exclusive OR with K
    xor_bits = XOR(R_48_bits, K)

    # Put through S boxes
    s_bits = list()
    Sboxes = [S1, S2, S3, S4, S5, S6, S7, S8]
    for i in range(8):
        sec = xor_bits[i*6:(i+1)*6]
        row = int(sec[0]+sec[5], 2)
        column = int(sec[1]+sec[2]+sec[3]+sec[4], 2)
        part = bin(Sboxes[i][row][column])[2:]
        pad_part = '0'*(4-len(part)) + part
        s_bits += list(pad_part)

    # Do permutation
    ret = [s_bits[P[i]-1] for i in range(32)]
    return ret



if __name__ == '__main__':

    testing = False 

    # Check command line arguments
    if len(sys.argv) != 3:
        print(f'Usage $ ./solution.py [path to cipher file] [path to key file]')
        sys.exit(1)
    TEXT_PATH = sys.argv[1]
    KEY_PATH = sys.argv[2]

    # Create keys
    f = open(TEXT_PATH, 'r')
    CIPHER = list(f.readline().strip())
    f.close()
    f = open(KEY_PATH, 'r')
    KEY = list(f.readline().strip())
    f.close()

    # Check integrity of the cipher and key
    if not all([i == '1' or i == '0' for i in CIPHER]):
        convert = input(f'Your given cipher is not in binary format. Would you like to automatically convert it to binary? (y/n): ')
        while convert != 'y' and convert != 'n':
            convert = input(f'Please enter y or n: ')
        if convert == 'n':
            sys.exit(1)
        # Convert cipher to binary
        new_cipher = ''
        for char in CIPHER:
            ascii_value = ord(char)
            binary = str(bin(ascii_value))[2:]
            while len(binary) < 8:
                binary = '0' + binary
            new_cipher += binary
        CIPHER = list(new_cipher)
        while len(CIPHER) % 64 != 0:
            CIPHER.append('0')
    if not all([i == '1' or i == '0' for i in KEY]):
        print(f'Your given key is not in binary format.')
        sys.exit(1)

    # Check length of cipher and key
    while len(CIPHER) % 64 != 0:
        CIPHER.append('0')
    if len(KEY) != 64:
        print(f'Your given key is not 64 bits long.')
        sys.exit(1)
    
    # Get input from user
    type_coding = input('Are you decrypting or encrypting? (d/e): ')
    while (type_coding != 'd' and type_coding != 'e'):
        type_coding = input('Please enter d or e: ')
    to_prints = {'source': 'Cipher', 'destination': 'Plaintext', 'operation': 'decrypt'} if type_coding == 'd' else {'source': 'Plaintext', 'destination': 'Cipher', 'operation': 'encrypt'}

    print('\n' + to_prints['source'] + ': ' + ''.join(CIPHER))
    print('Key:', ''.join(KEY))

    ROUND_KEYS = [list() for _ in range(16)]
    PC_KEY = [KEY[loc-1] for loc in PC1]

    # Perform these operations 16 times
    print(f'\nRounded Keys:')
    for i in range(16):

        # Create the C0 and D0 keys
        C0 = PC_KEY[:28]
        D0 = PC_KEY[28:]

        # Perform the left shifts
        C0 = left_shift(C0, LSH_TABLE[i])
        D0 = left_shift(D0, LSH_TABLE[i])

        # Combine to make next PC_KEY
        PC_KEY = C0.copy() + D0.copy()

        # Perform permutation
        ROUND_KEYS[i] = [PC_KEY[loc-1] for loc in PC2]
        to_print = ''.join(ROUND_KEYS[i])
        print(f'{i}: {to_print}')

    # Encrypt / decrypt
    OUTPUT = ''
    for idx in range(0, len(CIPHER), 64):

        print(f'\nSolving section {int(idx/64)+1} of cipher...')
        curr_cipher = CIPHER[idx:idx+64]

        # Permutate the cipher
        permutated_cipher = [curr_cipher[IP[i]-1] for i in range(len(IP))]

        # Split the cipher
        L = permutated_cipher[:32]
        R = permutated_cipher[32:]

        # Loop 16 times
        print(f'\n\tFunction outputs:')
        seq = range(0, 16) if type_coding == 'e' else range(15, -1, -1)
        for i in seq:
            # Run key and R between function
            out_function = f_function(R, ROUND_KEYS[i])
            to_print = ''.join(out_function)
            print(f'\tFor key {i}: {to_print}')
            # Put L and function into XOR, make that equal to R
            old_R = R.copy()
            R = XOR(L, out_function)
            # Set L equal to R
            L = old_R.copy()

        # Permutate the keys
        combined_keys = R + L
        output = [combined_keys[IP_INVERSE[i]-1] for i in range(len(IP_INVERSE))]

        # add section to OUTPUT
        OUTPUT += ''.join(output)

    # Output result
    print('\nBinary ' + to_prints['destination'] + ': ' + ''.join(OUTPUT))
    if to_prints['operation'] == 'decrypt':
        plaintext = ''
        for i in range(0, len(OUTPUT), 8):
            sec = OUTPUT[i:i+8]
            plaintext += chr(int(''.join(sec), 2))
        print('ASCII Plaintext:', plaintext)
