'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

ret = 0

mult3 = 3

mult5 = 5

while mult3 < 1000 or mult5 < 1000:
	if mult5 == mult3:
		ret = ret + mult3
	else:
		ret = ret + mult3 + mult5

	mult3 = mult3 + 3

	mult5 = mult5 + 5

print(f"The sum of all the multiples of 3 or 5 below 1000 is {ret}")