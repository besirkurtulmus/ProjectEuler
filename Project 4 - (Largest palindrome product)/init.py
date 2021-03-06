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
def isPalindrome(N):
	"""
	Returns a boolean regarding the number N being a palindrome or not

	Args:
		N: The given number
	Returns:
		Returns True if the given number is a palindrome.
		Returns False if the given number is not a palindrome.
	Examples:
		>>> isPalindrome(1221)
		True

		>>> isPalindrome(1241)
		False
	"""
	palindrome = str(N)
	size = len(palindrome)

	for i in range(size):
		if not palindrome[i] == palindrome[size - 1 - i]:
			return False
	return True

# Check the biggest palindrome which is a product of two 3-digit numbers
def biggestPalindrome():
	allPalindromes = []
	for i in xrange(999).__reversed__():
		for j in xrange(999).__reversed__():
			if(isPalindrome(i * j)):
				allPalindromes.append(i*j)
	return max(allPalindromes)

print biggestPalindrome()