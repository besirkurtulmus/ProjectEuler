#!/usr/bin/python

def findMultiples(M, N):
	"""
	Returns all numbers below N, that is a multiple of M.

	Args:
		M: the multiplier used for find the number(s).
		N: The upper bound for searching the number(s).
	Returns:
		Numbers of are a multiple of M, under N.

	Examples:
		>>> findMultiples(3, 10)
		[3, 6, 9]

		>>> findMultiples(5, 24)
		[5, 10, 15, 20]
	"""
	numbers = []

	for i in range(N):
		if(i + 1 == N):
			break
		if(((i + 1) % M) == 0):
			numbers.append(i+1)

	return numbers

#Upper limit is 100
#Multipliers are 3 and 5
N = 1000
M = [3, 5]
numSum = 0
numbers = []

#Get all number of multiplier of 3
numbers = numbers + findMultiples(M[0], N)
#Get all number of multiplier of 5
numbers = numbers + findMultiples(M[1], N)

#Remove all duplicates from list
properNumbers = list(set(numbers))

for i in properNumbers:
	numSum = numSum + i

print numSum