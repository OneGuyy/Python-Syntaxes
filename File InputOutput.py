import random
import sys
import os

test_file = open("test.txt", "wb")

print(test_file.mode)
print(test_file.name)

test_file.write(bytes("I'm a sentence in a file\n", 'UTF-8'))
test_file.close()

test_file = open("test.txt", "r+")

text_in_file = test_file.read()
print(text_in_file)
os.remove("test.txt")



