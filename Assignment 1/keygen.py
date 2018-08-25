import sys
import numpy as np

def keygen(m):
    det = 0
    # create random mxm matrices until the determinant is coprime to 26
    while (gcd(det, 26) != 1):
        A = np.random.randint(26, size=(m,m))
        det = int(round(float(np.linalg.det(np.asmatrix(A)))))
        if (gcd(det, 26) == 1):
            np.savetxt('key.txt', A, fmt='%.1i', delimiter=' ')
            print A
            print "done."
        continue

# gcd of two numbers
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

# determinant of a matrix
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
if (len(sys.argv) == 2):
    keygen(int(sys.argv[1]))
else:
    print "usage: python keygen.py <message_size>"
