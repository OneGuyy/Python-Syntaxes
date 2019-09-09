import random
import sys
import os

#WHILE LOOP :
random_num = random.randrange(0,100)

while(random_num != 15):
	random_num = random.randrange(0,100)
	print(random_num, end=";")

i = 0

while(i <= 20):
	if(i%2==0):
		print(i)
	elif(i == 9):
		break
	else:
		i += 1
		continue

	i += 1