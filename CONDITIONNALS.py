import random
import sys
import os

age = 30

if age >= 18:
	print("You are old enough to drive")
else:
	print("You aren't old enough to drive")

if age >= 18:
	print("You are an adult in France")
elif age >= 16:
	print("You will be an adult soon !")
else:
	print("You are a child !")

game_score = 1300

if((game_score >= 0) and (game_score <= 1000)):
	print('Bad game_score !')
elif((game_score > 1000) and (game_score <=2000)):
	print('Not Bad !')
else:
	print('WOW ! What a great score !')

if((age>=1) and (age<=18)):
	print("You cannot drive !")
elif((age==18) or (age>=65)):
	print("You get a birthday !")
elif not(age == 30):
	print("You are not 30yo !")
else:
	print("You get a birthday party yeah !")