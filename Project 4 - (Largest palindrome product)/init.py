#!/usr/bin/python

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