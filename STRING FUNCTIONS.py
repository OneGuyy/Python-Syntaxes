import random
import sys
import os

long_string = "My name's Blurryface and I care what you think"

print(long_string[0:9])
print(long_string[-5:])
print(long_string[:-5])
print(long_string[:9] +  " Jean Durgeaud")
print("%c is my %s letter and my number %d is %.5f"%
	  ('L', 'favourite', 1, 20))
print('\n')
print(long_string.capitalize())
print(long_string.find("Blurryface"))
print(long_string.isalpha())
print(long_string.isalnum())
print(len(long_string))
print(long_string.replace("Blurryface", "Jean Durgeaud"))
print(long_string.strip())
quote_list = long_string.split(" ")
print(quote_list)