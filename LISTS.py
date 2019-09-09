import random
import sys
import os

grocery_list = ['Juice', 'Tomatoes', 'Apples', 'Eggs']

print('First Item is', grocery_list[0])

grocery_list[0] = "Soda"
print('First Item is', grocery_list[0])

print(grocery_list[1:3])

other_events = ['Wash Car', 'Cash Check', 'City Tour']

to_do_list = [other_events, grocery_list]
print(to_do_list)

print((to_do_list[1][3]))

grocery_list.append('Candy')
print(to_do_list)

grocery_list.insert(1, 'Video Games')
print(to_do_list)

grocery_list.remove("Video Games")

grocery_list.sort()
grocery_list.reverse()

print(grocery_list)
del grocery_list[4]
print(grocery_list)

to_do_list2 = other_events + grocery_list

print(len(to_do_list2))
print(min(to_do_list2))
print(max(to_do_list2))

