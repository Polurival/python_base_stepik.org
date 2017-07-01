import itertools, math

def primes():
    x = 1
    while True:
        x += 1
        if (math.factorial(x - 1) + 1) % x == 0:
            yield x

print(list(itertools.takewhile(lambda x : x <= 31, primes())))