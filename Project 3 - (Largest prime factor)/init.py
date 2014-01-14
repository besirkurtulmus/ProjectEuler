#!/usr/bin/python
import sys
import math
"""
Usage:
	>>> python init.py 13195
	[5, 7, 13, 29]
"""


def isPrime(N):
	"""
	Returns a boolean regarding the number N being prime or not

	Args:
		N: The given number
	Returns:
		Returns True if the given number is prime.
		Returns False if the given number is not a prime.
	Examples:
		>>> isPrime(7)
		True

		>>> isPrime(12)
		False
	"""
	if N == 2:
		return True
	if N % 2 == 0 or N <= 1:
		return False
	sqr = int(math.sqrt(N)) + 1
	for div in xrange(3, sqr, 2):
		if N % div  == 0:
			return False
	return True

def returnPrimeFactors(N):
	"""
	Returns the prime factors of the given number N

	Args:
		N: The given number of which it's primes are being asked.
	Returns:
		The primes of the number N
	Examples:
		>>> returnPrimeFactors(13195)
		[5, 7, 13, 29]
	"""
	primeList = []
	currentNumber = 2
	while currentNumber <= N:
		if( N % currentNumber == 0 ) and isPrime(currentNumber):
			primeList.append(currentNumber)
			N = N / currentNumber
		currentNumber = currentNumber + 1
	return primeList

print returnPrimeFactors(int(sys.argv[1]))