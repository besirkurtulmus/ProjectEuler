#!/usr/bin/python
'''
The MIT License (MIT)

Copyright (c) 2014 Ahmet Besir Kurtulmus

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
def findMultiples(M, N):
	"""
	Returns all numbers below N, that is a multiple of M.

	Args:
		M: the multiplier used for find the number(s).
		N: The upper bound for searching the number(s).
	Returns:
		Numbers that are a multiple of M, under N.

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

#Upper limit is 1000
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