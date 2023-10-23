
#!/usr/bin/env python3
from itertools import islice
#from time import time
"""
def time_generator(func, n=500000):
  generator = func()
  start     = time()
  islice(generator, n)
  elapsed   = time() - start

  print("[%s] %0.9fs (%d iterations): " % (func.__name__, elapsed, n))
"""
def is_palindrome(n):
    m = int(str(n)[::-1])
    if m == n: return True
    return False

def prime_generator_pseudotest():
  """ A pseudo-prime testing trick in a generator expression """
  small_primes = (2, 3, 5, 7, 11)
  p = 2
  while True:
    if 0 not in (pow(w,p-1,p)==1 for w in small_primes if p > w):
      yield p
    p += 1

def is_prime(n):
    if (n <= 1):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False

    i = 3
    while i <= n**.5+1:
        if n % i == 0:
            return False
        i = i + 2

    return True
    
"""
def prime_generator():
  # Yields the sequence of prime numbers via the Sieve of Eratosthenes. 
  D = {}  # map composite integers to primes witnessing their compositeness
  q = 2   # first integer to test for primality
  while 1:
    if q not in D:
      yield q        # not marked composite, must be prime
      D[q*q] = [q]   # first multiple of q not already marked

    else:
      for p in D[q]: # move each witness to its next multiple
        D.setdefault(p+q,[]).append(p)
      del D[q]       # no longer need D[q], free memory

    q += 1

time_generator(prime_generator)
time_generator(prime_generator_pseudotest)
"""

values=[]

def check(n):
    back=int(str(n*n)[::-1])
    root=back**.5
    if root == int(root):
        if not is_prime(root): return False
        if is_palindrome(n*n): return False
        return True
    return False
        #print(n,n*n, int(back**.5))


values=[]
counter=0
generator = prime_generator_pseudotest()
for i in islice(generator,100000000):
    if check(i):
        if i*i in values: continue
        values.append(i*i)
        values.append(int(str(i*i)[::-1]))
        counter+=2
        print(counter,i,i*i)    
    if counter == 50: break
print(sum(values))
