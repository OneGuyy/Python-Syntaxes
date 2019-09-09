import random
import sys
import os

#FOR LOOP :
for x in range(0,10):
	print(x, ' ', end="")

print(" ")

grocery_list = ["Eggs", "Tomatoes", "Soda", "Sugar"]
for y in grocery_list:
	print(y, " ; ", end="")

print(" ")

for x in [2,4,6,8,10]:
	print(x, ' ',end="")

print('\n')

new_list = [[1,2,3],[10,20,30],[100,200,300]]
for x in range(0,3):
	for y in range(0,3):
		print(new_list[x][y])

