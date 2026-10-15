'''
Arrays:
 -All arrays store ordered collections of data, but depending on their type, they may work differently behind the scenes.

Static_arrays and its properties:
 -Static arrays have a fixed size. They store elements in adjacent memory locations.
 -The size of a static array is determined when the array is initialized. Once that specific block of memory is allocated, it's fixed
 -Storing elements in adjacent memory locations makes the data retrieval process more efficient.
 -Accessing the values of a static array takes constant time O(1), which is very efficient.
 -However, this data structure cannot grow or shrink, so if the number of elements that will be stored can vary, you should use a dynamic array instead.

Dynamic Arrays:
 -Dynamic arrays are more flexible because they can grow or shrink automatically while the program is running.
 -They work through an automatic resizing mechanism that copies the elements into a new array when the original array is full. 
 -The process is done efficiently because the size of the new array is chosen in an efficient way that makes these computationally expensive operations less frequent.
 -Accessing the elements of a dynamic array takes constant time O(1), so this operation is very efficient.
 -Inserting an element in the middle of the array takes linear time O(n) because the elements after it need to be relocated.
 -Dynamic Arrays in Python
  Python's built-in list data structure works as a dynamic array. You can create a list by writing the elements within square brackets, separated by commas.
  
  numbers = [3, 4, 5, 6]
  Accessing and Modifying Elements
  You can access an element by writing the name of the variable that holds the list, followed by square brackets, and within the square brackets, the corresponding index.
  
  Indices start from 0 for the first element and are incremented by 1 for each subsequent element:
  
  numbers[0]  # 3
  numbers[1]  # 4
  numbers[2]  # 5
  numbers[3]  # 6
  To update a value, you just need to reassign it:
  
  numbers[2] = 16
  You can append elements to the list with the .append() method:
  
  numbers.append(7)
  You can insert elements at a specific index with the .insert() method, passing the index as the first argument and the element itself as the second argument.
  
  numbers.insert(3, 15)
  You can remove an element at a specific index with the .pop() method:
  
  numbers.pop(2)
  If you don't specify the index, .pop() will remove the last element.
  
'''
