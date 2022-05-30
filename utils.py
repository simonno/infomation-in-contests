from math import comb

from config import LIMIT_DOWN, LIMIT_UP


def binom(r, t, p):
    return comb(t, r) * (p ** r) * ((1 - p) ** (t - r))


def F_big(x):
    return x


def f_small(x):
    return 1


def integral(f, a=LIMIT_DOWN, b=LIMIT_UP, N=10000):
    value = 0
    for n in range(N + 1):
        value += f(a + (2 * n - 1) * (b - a) / (2 * N))
    return value * (b - a) / N


def root(f):
    for index in range(LIMIT_DOWN, LIMIT_UP * 100 + 1):
        i1 = index / 100
        i2 = (index + 1) / 100
        try:
            if f(i1) * f(i2) <= 0:
                for index_2 in range(index, (index + 1) * 1000 + 1):
                    i1 = index_2 / 1000
                    i2 = (index_2 + 1) / 1000
                    if f(i1) * f(i2) <= 0:
                        for index_3 in range(index_2, (index_2 + 1) * 10000 + 1):
                            i1 = index_3 / 10000
                            i2 = (index_3 + 1) / 10000
                            if f(i1) * f(i2) <= 0:
                                return i1
        except ZeroDivisionError:
            continue
    raise Exception('root not found')
