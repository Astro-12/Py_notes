'''
Abstraction:
  -Process of hiding complex implementation details and showing the only important features of an object or system.
  -Abstraction implementation in python happens through "abc" module.
  -An abstract method is a method declared using the @abstractmethod decorator.
'''
-Example:
  from abc import ABC, abstractmethod

  class Animal(ABC): # Inherits from abstract base class
     @abstractmethod # Abstract method decorator
     def make_sound(self):  # The method subclasses must override
         pass
  
  # Concrete class that will override the abstract method
  class Dog(Animal):
     def make_sound(self):
         print('Woof!')
  
  # Another concrete class that will override the abstract method
  class Cat(Animal):
     def make_sound(self):
         print('Meow!')
  
  # Another concrete class that will override the abstract method
  class Monkey(Animal):
     def make_sound(self):
         print('Ooh ooh aah aah!')
  
  # Create instances of each concrete class
  animals = [Dog(), Cat(), Monkey()]
  
  # Loop through the instances to call the make_sound method
  for animal in animals:
     animal.make_sound()
  
  # Output:
  # Woof!
  # Meow!
  # Ooh ooh aah aah!
'''
Remember that you cannot create an instance of the Animal class. Here's what happens if you try to do that:
'''
  dog = Animal() 
  # TypeError: Can't instantiate abstract class Animal 
  # without an implementation for abstract method 'make_sound'
'''
Another example with instance attribute:
'''
from abc import ABC, abstractmethod

# The blueprint for any toy that can speak
class TalkingToy(ABC):
   def __init__(self, name):
       self.name = name
   @abstractmethod
   def speak(self):
       pass

class RobotToy(TalkingToy):
   def speak(self):
       print(f'{self.name} says beep boop! I am a robot!')

class TeddyBearToy(TalkingToy):
   def speak(self):
       print(f"{self.name} says hug me! I'm cuddly!")

class DinosaurToy(TalkingToy):
   def speak(self):
       print(f'{self.name} says ROOOOAR!')

# Create toys
rusty = RobotToy('Rusty')
fluffy = TeddyBearToy('Fluffy')
rex = DinosaurToy('Rex')

toys = [rusty, fluffy, rex]
for toy in toys:
   toy.speak()

# Output:
# Rusty says beep boop! I am a robot!
# Fluffy says hug me! I'm cuddly!
# Rex says ROOOOAR!
'''
Here:
  -We have an abstract base class TalkingToy that defines a blueprint for any toy that can speak.
  -The subclasses RobotToy, TeddyBearToy, and DinosaurToy implement the speak method in their own way.
  -When we create instances of these subclasses and call the speak method, each toy speaks in its own unique way.
'''
