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