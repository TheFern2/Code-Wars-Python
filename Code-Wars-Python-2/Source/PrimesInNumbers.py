from math import sqrt
import functools

def factors(n):
    return set(functools.reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def isPrime(a):
    if a < 2: return False
    for x in range(2, int(sqrt(a)) + 1):
        if a % x == 0:
            return False
    return True

def nextPrime(n):
    while not isPrime(n+1):
        n += 1
    return n + 1

def primeFactors(nmbr):
    out = []
    result = -1
    currentPrimeResult = nmbr
    p = 1
    n = 0

    if isPrime(nmbr):
        return "(%d)" % nmbr

    while result != 1:
        p = nextPrime(p)
        while currentPrimeResult % p == 0:
            currentPrimeResult = currentPrimeResult / p
            n += 1
        if n >= 2:
            out.append("(%d**%d)" % (p,n))
        elif n == 1:
            out.append("(%d)" % p)
        n = 0
        result = currentPrimeResult

    return "".join(out)

def primeFactors2(nmbr):
    out = []
    result = -1
    currentPrimeResult = nmbr
    i = 1
    p = 1
    n = 0
    factorList = sorted(factors(nmbr))

    if isPrime(nmbr):
        return "(%d)" % nmbr

    while result != 1:
        p = factorList[i]
        while currentPrimeResult % p == 0:
            currentPrimeResult = currentPrimeResult / p
            n += 1
        if n >= 2:
            out.append("(%d**%d)" % (p,n))
        elif n == 1:
            out.append("(%d)" % p)
        n = 0
        result = currentPrimeResult
        i += 1

    return "".join(out)