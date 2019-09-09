import random
import sys
import os

class Animal:
	__name = None #__ means variable is in private !
	__height = 0
	__weight = 0
	__sound = 0

	def __init__(self, name, height, weight, sound):
		self.__name = name
		self.__height = height
		self.__weight = weight
		self.__sound = sound

	def SetName(self, name):
		self.__name = name

	def SetHeight(self, height):
		self.__height = height

	def SetWeight(self, weight):
		self.__weight = weight

	def SetSound(self, sound):
		self.__sound = sound

	def GetName(self):
		return self.__name

	def GetHeight(self):
		return str(self.__height)

	def GetWeight(self):
		return str(self.__weight)

	def GetSound(self):
		return self.__sound

	def GetType(self):
		print("Animal")

	def toString(self):
		return "{} is {} cm tall and {} kilograms and say {}".format(self.__name,
																	 self.__height,
																	 self.__weight,
																	 self.__sound)
cat = Animal("Felix", 33, 6, "Meow")

print(cat.toString())	

#THIS IS INHERITANCE !!
class Dog(Animal):
	__owner = ""	
	def __init__(self, name, height, weight, sound, owner):
		self.__owner = owner															 
		super(Dog, self).__init__(name, height, weight, sound)
	def SetOwner(self, owner):
		self.__owner = owner
	def GetOwner(self):
		return self.__owner
	def GetType(self):
		print("Dog")	
	def toString(self):
		return "{} is {} cm tall and {} kilograms and say {}. His owner is {}.".format(self.GetName(),
																						self.GetHeight(),
																	 					self.GetWeight(),
																	 					self.GetSound(),
																	 					self.__owner)
	def multiple_sounds(self, how_many=None):
		if(how_many is None):
			print(self.GetSound())
		else:
			print(self.GetSound() * how_many)	

dog = Dog("Spot", 75, 27, "Woof", "Jean")
print(dog.toString())

dog.multiple_sounds()

class AnimalTesting:
	def GetType(self, Animal):
		Animal.GetType()

test_animal = AnimalTesting()
test_animal.GetType(dog)
test_animal.GetType(cat)

dog.multiple_sounds(4)
dog.multiple_sounds()