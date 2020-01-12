#!/usr/bin/env python
# coding: utf-8

# aufgabe07.py
# guess a random number

import random


def main():
	zahl = random.randint(1, 10)
	while True:
		user_zahl = input("Guess a number between 1 and 10: ")

		try:
			user_zahl = int(user_zahl)

			if user_zahl < zahl:
				print("higher\n")

			elif user_zahl > zahl:
				print("lower\n")

			elif user_zahl == zahl:
				print("correct: {}".format(zahl))
				break

		except:
			print("Please give a whole number.\n")


if __name__ == '__main__':
	main()

