# -*- coding: utf-8 -*-
"""
Created on Tue May 14 18:01:33 2019

@author: macabre
"""

import concurrent.futures
import math

#Es una tarea CPU-bound, va process
PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
        #Si pongo la opcion map_workers=4
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            #ZIP genera pares de parametros
            print('%d is prime: %s' % (number, prime))

if __name__ == '__main__':
    main()