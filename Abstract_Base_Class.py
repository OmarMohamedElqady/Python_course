# ----------------------------------------------------------------
# -- Object Oriented Programming => ABCs => Abstract Base Class --
# ----------------------------------------------------------------
# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class
# --------------------------------------------------------------------

from abc import ABCMeta, abstractmethod

class Programming(metaclass=ABCMeta):

  @abstractmethod
  def has_oop(self):

    pass

  @abstractmethod
  def has_name(self):

    pass

class Python(Programming):

  def has_oop(self):

    return "Yes"
  
  def has_name(self):

    return "Python"
  

class Pascal(Programming):

  def has_oop(self):

    return "No"

  def has_name(self):

    return "Pascal"

one = Pascal()

print(one.has_oop())
print(one.has_name())

####################

two = Python()

print(two.has_oop())
print(two.has_name())
##############################################



# Python program showing 
# abstract base class work 

from abc import ABC, abstractmethod 


class Polygon(ABC): 

	@abstractmethod
	def noofsides(self): 
		pass


class Triangle(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 3 sides") 


class Pentagon(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 5 sides") 


class Hexagon(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 6 sides") 


class Quadrilateral(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 4 sides") 


# Driver code 
R = Triangle() 
R.noofsides() 

K = Quadrilateral() 
K.noofsides() 

R = Pentagon() 
R.noofsides() 

K = Hexagon() 
K.noofsides() 
