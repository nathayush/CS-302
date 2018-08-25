import sys
import numpy as np

def decode(cipher_file ,key_file):
    ciphertext = []
    key = []
    # read ciphertext
    with open(cipher_file, 'rU') as f:
        ciphertext = [int(num) for num in f.readline().split(" ")]
    size = len(ciphertext)
    # read key
    with open(key_file, 'rU') as f:
        for line in f:
            temp = [int(num) for num in line.split(" ")]
            key.append(temp)
    key_size = len(key)

    # modular inverse of determinant of original key
    det = modInverse(int(round(float(np.linalg.det(np.asmatrix(key))))), 26)
    # adjoint matrix
    key = adjoint(key)
    # inverse of key = adj(A) * |A|^-1
    for i in range(len(key)):
        for j in range(len(key)):
            key[i][j] *= det
    print key
    result = []
    start = 0
    # split ciphertext into equal parts of key_size and decrypt individually
    for i in range(size/key_size):
        result += matrixProd(ciphertext[start: start + key_size], key, key_size)
        start += key_size

    with open("output.txt", 'w') as f:
        for i in range(len(result)):
            result[i] = chr(int(result[i] % 26) + 97)
            f.write(str(result[i]))

    print result

# product of a row matrix and a square matrix
def matrixProd(a, b, size):
    result = [0] * size
    for i in range(size):
            for j in range(size):
                result[i] += a[j] * b[j][i]
    return result

# modular inverse of a number 'a' in Z(m)
def modInverse(a, m) :
    a = a % m;
    for i in range(1, m) :
        if ((a * i) % m == 1) :
            return i
    return 1

# adjoint of a matrix
def adjoint(a):
    size = len(a)
    adj = [[0] * size for i in range(size)]
    # base case of 2x2
    if (size == 2):
        adj[0][0] = int(a[1][1])
        adj[1][1] = int(a[0][0])
        adj[1][0] = -1 * int(a[1][0])
        adj[0][1] = -1 * int(a[0][1])
    else:
        for i in range(size):
            for j in range(size):
                # remove row
                cof = a[:i] + a[i+1:]
                # remove column
                for k in range(len(cof)):
                    cof[k] = cof[k][:j] + cof[k][j+1:]
                # multiply with appropriate power of -1
                adj[i][j] = pow(-1, i+j) * int(round(float(np.linalg.det(np.asmatrix(cof)))))
        # transpose of the cofactor matrix
        adj = transpose(adj)
    return adj

# transpose of a matrix
def transpose(a):
    trans = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
    return trans

# determinant of a matrix; using numpy library instead
# def getdet(a):
#         if(len(a) == 2):
#             return (a[0][0]*a[1][1] - a[0][1]*a[1][0])
#         else:
#             term_list = []
#             for i in range(len(a)):
#                 cof = a[1:]
#                 for j in range(len(cof)):
#                     cof[j] = cof[j][:i] + cof[j][i+1:]
#                 mult = a[0][i] * pow(-1, 2+i) * getdet(cof)
#                 term_list.append(mult)
#             return(sum(term_list))

# run
if (len(sys.argv) == 3):
    decode(str(sys.argv[1]), str(sys.argv[2]))
else:
    print "usage: python decode.py <ciphertext.txt> <key.txt>"
