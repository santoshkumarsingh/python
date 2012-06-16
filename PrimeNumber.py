# isPrime() takes a positive integer as an argument
# and returns True if that integer is a prime number
# and False if the number is not prime.
# Input:       a positive integer, num
# Output:      either True or False
# Assumptions: num will be an integer > 1
def isPrime(num):

    # try to evenly divide num by all
    # numbers between 2 and num - 1
    for i in range(2, num):
        
        # if num is evenly divisble by this
        # number, then it isn't prime
        if num % i == 0:
            return False

    # if num wasn't divisable by any of
    # those numbers, then it's prime
    return True


def main():

    # print primes from 2 to 11, inclusive
    for i in range (2, 12):
        if isPrime(i):
            print i,

main()

