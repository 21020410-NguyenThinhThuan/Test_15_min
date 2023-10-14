import random

def generateLargePrime(keysize):
    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if (isPrime(num)):
            return num

def rabinMiller(n, d):
    a = random.randint(2, (n - 2) - 2)
    x = pow(a, int(d), n)  
    if x == 1 or x == n - 1:
        return True

    
    while d != n - 1:
        x = pow(x, 2, n)
        d *= 2

        if x == 1:
            return False
        elif x == n - 1:
            return True

    return False


def isPrime(n):
    if n < 2:
        return False

    if n in lowPrimes:
        return True

    for prime in lowPrimes:
        if n % prime == 0:
            return False

    c = n - 1  
    while c % 2 == 0:
        c /= 2  


    for i in range(128):
        if not rabinMiller(n, c):
            return False

    return True


def generateKeys(keysize=1024):
    e = d = N = 0
    p = 56463568746442945939
    q = 28254268158958937761

    N = p * q  
    phiN = (p - 1) * (q - 1)  

    e = 5024058009893548070322641845573

    d = modularInv(e, phiN)

    return p, q, e, d, N


def isCoPrime(p, q):
    return gcd(p, q) == 1


def gcd(p, q):
    while q:
        p, q = q, p % q
    return p


def egcd(a, b):
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def modularInv(a, b):
    gcd, x, y = egcd(a, b)

    if x < 0:
        x += b

    return x


class RSA(object):

    def __init__(self, keysize=1024):
        self.keysize = keysize
        self.p, self.q, self.e, self.d, self.N = generateKeys(self.keysize)

    def encrypt(self, msg):
        cipher = ""

        for c in msg:
            m = ord(c)
            cipher += str(pow(m, self.e, self.N)) + " "

        return cipher

    def decrypt(self, cipher):
        msg = ""

        parts = cipher.split()
        for part in parts:
            if part:
                c = int(part)
                msg += chr(pow(c, self.d, self.N))

        return msg


if __name__ == "__main__":
    msg = input("Nhập message: ")
    rsa = RSA(keysize=32)
    enc = rsa.encrypt(msg=msg)
    dec = rsa.decrypt(cipher=enc)

    print(f"e: {rsa.e}")
    print(f"d: {rsa.d}")
    print(f"N: {rsa.N}")
    print(f"p: {rsa.p}")
    print(f"q: {rsa.q}") 
    print(f"mã hóa: {enc}")
    print(f"giải mã: {dec}")