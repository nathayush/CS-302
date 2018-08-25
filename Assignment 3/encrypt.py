from random import randint
from base64 import b64decode

def main():
    with open("pk.pem", 'r') as f:
        f.readline()
        q, g, h = b64decode(f.readline().rstrip()).split("$")
        q = int(q)
        g = int(g)
        h = int(h)
    with open("message.txt", 'r') as f:
        m = int(f.readline().rstrip())
    r = randint(2, q-1)
    c1 = squareAndMultiply(g, r, q)
    c2 = (squareAndMultiply(h, r, q)*m) % q
    with open("ciphertext.txt", 'w') as f:
        f.write(str(c1) + '\n' + str(c2))
    print "done."

def squareAndMultiply(x, c, n):
    z = 1
    C = bin(c).replace("0b", '', 1)
    i = len(C) - 1
    while i >= 0:
        z = pow(z, 2, n)
        if C[-(i+1)] == '1':
            z = (z*x) % n
        i -= 1
    return z

if __name__ == '__main__':
    main()
