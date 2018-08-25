from random import randint
from base64 import b64decode

def main():
    with open("sk.txt", 'r') as f:
        f.readline()
        a = int(b64decode(f.readline().rstrip()))
    with open("pk.pem", 'r') as f:
        f.readline()
        q, g, h = b64decode(f.readline().rstrip()).split("$")
        q = int(q)
        g = int(g)
        h = int(h)
    with open("ciphertext.txt", 'r') as f:
        c1 = int(f.readline().rstrip())
        c2 = int(f.readline().rstrip())
    t1 = squareAndMultiply(c1, a, q)
    t2 = c2*modInverse(t1,q) % q
    with open("plaintext.txt", 'w') as f:
        f.write(str(t2))
    print "done."

def modInverse(a, b):
    a0 = a
    b0 = b
    t0 = 0
    t = 1
    s0 = 1
    s = 0
    q = a0//b0
    r = a0 - q*b0
    while r > 0:
        temp = t0 - q*t
        t0 = t
        t = temp
        temp = s0 - q*s
        s0 = s
        s = temp
        a0 = b0
        b0 = r
        q = a0//b0
        r = a0 - q*b0
    return s

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
