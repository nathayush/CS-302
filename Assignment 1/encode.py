import sys
import numpy as np

def encode(message_file ,key_file):
    message = []
    key = []
    # read message
    with open(message_file, 'rU') as f:
        chars = []
        map(chars.extend, f.read().rstrip())
        message = [ord(ch) - 97 for ch in chars]
    # read key
    with open(key_file, 'rU') as f:
        for line in f:
            temp = [int(num) for num in line.split(" ")]
            key.append(temp)
    key_size = len(key)
    
    #padding
    if (len(message) % key_size != 0):
        message += [25] * (key_size - (len(message) % key_size))
    result = []
    start = 0
    # split message into equal parts of key_size and encrypt individually
    for i in range(len(message)/key_size):
        result += matrixProd(message[start: start + key_size], key, key_size)
        start += key_size
    # apply mod 26 to the ciphertext
    for i in range(len(result)):
        result[i] = result[i] % 26
    print result
    saveToFile(result)
    print "done."

# product of a row matrix and a square matrix
def matrixProd(a, b, key_size):
    result = [0] * key_size
    for i in range(key_size):
            for j in range(key_size):
                result[i] += a[j] * b[j][i]
    return result

# save a matrix to a file using numpy
def saveToFile(matrix):
    result = np.asmatrix(matrix)
    np.savetxt('ciphertext.txt', result, fmt='%.1i', delimiter=' ')

# run
if (len(sys.argv) == 3):
    encode(str(sys.argv[1]), str(sys.argv[2]))
else:
    print "usage: python encode.py <message.txt> <key.txt>"
