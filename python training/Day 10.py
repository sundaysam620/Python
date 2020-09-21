def SumSquare(n):
    i=0
    x=0
    y=0
    while i<=n:
        x+=pow(i,2)
        y+=i

        i+=1

    return pow(y,2)-x
test=SumSquare(40)
print(test)
####
##
##def is_prime(n):
##   
##
####    # Every composite (non-prime) number is evenly divisble
####    # by at least one prime less than itself
##
####    # A function can *access* a name dedined outside itself i.e 'primes'
##
##    for p in primes:
##        if not n % p:
####            # n is not prime
##            return False
##    else:
####        # n is prime
##        primes.append(n)
##        return True
##
##def largest_prime_factor(num):
##    """Returns the largest prime factor of 'num'"""
##
##    if not num % 2:
####            # the only and largest prime factor of any even number is 2
##        while not num % 2:
##            num //= 2
##        if num == 1:
##            return 2
##        n = 1
##        while num > 1:
####            # With 2 aside, Only odd numbers can be prime
##
####            n += 2  # next odd number
##
####            # it takes less time to check for divisibility than to check for primality
####            # so check for divisibility first
####            # It's just like the normal process to get prime factors in maths.
####            # Keep dividing num by n until num is no longer evenly divisible by n.
##            while not num % n:
##                num //= n
##
##            if not num % n and is_prime(n):
####                # Keep dividing num by n until num is no longer evenly divisible by n.
##                while not num % n:
##                    num //= n
##    return n
##    return n  # The number to finish dividing num is the largest
##
##primes = []
##num = 600851475143
##
##n = largest_prime_factor(num)
##print("%d is the largest prime factor of %d" % (n, num))

##x = 2**4- 2**2
##print (x)

##def sumSquares(n):
##    i=0
##    x=0
##    while i<=n:
##        x+=pow(i,2)
##    return sumSquare(n)
##    
##test = sumSquare(60)
##print(test)
