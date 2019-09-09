import random
import sys
import os

print("Hello World!")

name = "Jean"
print(name)
name = 15

#There are 5 variables types : Numbers / Strings / Lists / Tuples / Dictionaries

print('\n')
'''
Mathematics operator :
Addition : +
Soustraction : -
Multiplication : *
Division : /
Modulo : %
Exponantiel : **
Div.Euclidienne	: //
'''

#EXEMPLE :
print("7 + 4 =", 7+4)
print("7 - 4 =", 7-4)
print("7 * 4 =", 7*4)
print("7 / 4 =", 7/4)
print("7 % 4 =", 7%4)
print("7 ** 4 =",7**4)
print("7 // 4 =", 7//4)

print('\n')
'''There also are priorities
Exemple'''
print("1 + 2 - 3 * 2 =",1+2-3*2)
print("(1 + 2 - 3) * 2 =", (1+2-3)*2)


#Some strings !
quote = "\"Always remember you are unique "
multiline_quote = '''Just like
everyone else\"'''

print(quote + multiline_quote)

print('\n')

print("%s %s %s" % ("I like the quote", quote, multiline_quote))

print('\n' * 3)
print("I don't like ", end="")
print("newlines")