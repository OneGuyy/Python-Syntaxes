import random
import sys
import os

secret_names = {'Voldemort' : 'Tom Jedusor',
			  'Øne Guy' : 'Jean Durgeaud',
			  'Dumbledore' : 'Ron Weasley',
			  'Batman' : 'Bruce Wayne'}

print(secret_names['Øne Guy'])

del secret_names['Dumbledore']

secret_names['Øne Guy'] = 'Gui de GRRRRL'

print(len(secret_names))

print(secret_names.get("Voldemort"))

print(secret_names.keys()) #VALEURS DE GAUCHE !

print(secret_names.values()) #VALEURS DE DROITE !