from __future__ import print_function

# fib function
def fib(n):
	if n <= 2:
		return 1
	elif memo[n] != None:
		return memo[n]
	else:
		memo[n] = fib(n - 1) + fib(n - 2)
		return memo[n]

print('Which fibonaci number do you want me to caclulate?: ', end = '')
n = int(input())


global memo
memo = [None] * (n + 1)

print(str(fib(n)))