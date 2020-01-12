#!/usr/bin/env python
# coding: utf-8

# aufgabe06.py
# find fibonacci number 


def fib(n):
	i = 0
	lst = []
	while i <= n:

		if i == 0:
			lst.append(0)
		elif i == 1 or i == 2:
			lst.append(1)
		elif i > 2:
			f1 = lst[i - 1]
			f2 = lst[i - 2]
			nice = f1 + f2
			lst.append(nice)

		i += 1

	return lst[n]


def iterate(N):
	lst = []
	for i in range(N):
		lst.append(fib(i))

	return lst


if __name__ == '__main__':
	# print(fib(10))
	print(iterate(25))

