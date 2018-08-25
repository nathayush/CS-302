from random import randrange, getrandbits, randint
from numpy.random import uniform
from math import floor
from base64 import b64encode
from sys import argv

def main():
    p = generatePrime()
    while not isPrime(2*p+1):
        p = generatePrime()
    q = 2*p+1
    g = getQuadraticResidue(q)
    a = int(floor(uniform(2, (q-3)/2)))
    h = squareAndMultiply(g, a, q)
    with open("pk.pem", 'w') as f:
        f.write("-----BEGIN PUBLIC KEY-----\n")
        f.write(b64encode(str(q) + '$' + str(g) + '$' + str(h)))
        f.write("\n-----END PUBLIC KEY-----")
    with open("sk.txt", 'w') as f:
        f.write("-----BEGIN PRIVATE KEY-----\n")
        f.write(b64encode(str(a)))
        f.write("\n-----END PRIVATE KEY-----")
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

def getQuadraticResidue(q):
    q_1 = q-1
    g = randint(2, q_1)
    power = (q_1)/2
    while squareAndMultiply(g, power, q) != 1:
        g = randint(2, q_1)
    return g

def calculateLegendre(a, p):
    if a >= p or a < 0:
        return calculateLegendre(a % p, p)
    elif a == 0 or a == 1:
        return a
    elif a == 2:
        if p % 8 == 1 or p % 8 == 7:
            return 1
        else:
            return -1
    elif a == p-1:
        if p % 4 == 1:
            return 1
        else:
            return -1
    elif not isPrime(a):
        factors = factorize(a)
        product = 1
        for pi in factors:
            product *= calculateLegendre(pi, p)
        return product
    else:
        if ((p-1)/2) % 2==0 or ((a-1)/2) % 2==0:
            return calculateLegendre(p, a)
        else:
            return (-1)*calculateLegendre(p, a)

def factorize(n):
    factors = []
    p = 2
    while True:
        while(n % p == 0 and n > 0):
            factors.append(p)
            n = n / p
        p += 1
        if p > n / p:
            break
    if n > 1:
        factors.append(n)
    return factors

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def isPrime(n, num_tests = 100):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    for _ in range(num_tests):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

def generatePrime(length = 300):
    p = 4
    while not isPrime(p):
        p = getrandbits(length)
        p |= (1 << length - 1) | 1
    return p

if __name__ == "__main__":
    main()
