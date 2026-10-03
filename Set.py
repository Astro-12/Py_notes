'''
A set in Python is an unordered, mutable, and unique collection of elements. It does not allow duplicate values.
How to create a set:
'''
# Empty set (must use set(), not {})
empty_set = set()
 
# Set with elements
numbers = {1, 2, 3, 4, 5}
 
# Mixed data types
mixed_set = {1, "Hello", 3.14, True}
 
# Creating a set from a list
unique_numbers = set([1, 2, 2, 3, 4, 4, 5])
print(unique_numbers)  # {1, 2, 3, 4, 5}
'''
Common Set Methods
Method	                        Description	                                          Example
add(x)	            Adds an element x to the set.	                                   my_set.add(10)
update(iterable)	  Adds multiple elements from an iterable.	                my_set.update([6, 7, 8])
remove(x)	          Removes x from the set (raises an error if not found).	      my_set.remove(3)
discard(x)	        Removes x from the set (does not raise an error if not found).	my_set.discard(3)
pop()	              Removes and returns a random element.                            	my_set.pop()
clear()	            Removes all elements from the set.	                              my_set.clear()
copy()	            Returns a shallow copy of the set.	                        new_set = my_set.copy()
