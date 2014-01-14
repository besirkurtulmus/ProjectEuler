#!/usr/bin/python

# Create variables for the last two values of the fibo series
term1 = 0
term2 = 1

# Create a variable for keeping the sum of the even fibo values
seqSum = 0

# A temp variable
termTmp = 0

# Calculate until you hit a fibo value above 4 million
while termTmp < 4000000:
	termTmp = term1 + term2
	term1 = term2
	term2 = termTmp
	if(term2 % 2 == 0):
		seqSum = seqSum + term2
print seqSum