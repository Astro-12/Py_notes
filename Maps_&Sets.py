'''
Abstract data types:
  -An Abstract Data Type (ADT) is a conceptual representation of a data type, including what operations can be performed on the data and the properties of that data.
  -ADT is like blueprints that describe what operations can be performed, not how they are performed.
'''
'''
Maps:
  -A map is an ADT that manages collections of key-value pairs and their operations in a very specific and efficient way.
  -One of the key characteristics of maps is that every key must be unique. This uniqueness allows for direct lookups,
    which makes the process of retrieving information much more efficient.
  -The map Abstract Data Type also defines important operations, such as inserting key-value pairs, getting the value associated with a key, 
    updating the value associated with a key, removing a key-value pair, and checking if a key exists in the map.  
'''
'''
Hash Maps:
  -A concrete implementation of the Map ADT using a technique called hashing.
  -How Hashing Works:
    -A hash function generates a hash value based on the key.
    -This hash value calculates an index in an underlying array where the key-value pair is stored.
  -Handling Collisions:
    -Chaining: Each array index points to a linked list storing all elements with that same index.
    -Open Addressing: Searches for the next available array index based on a predefined sequence.
  -Complexity:
    -Average Case: $O(1)$ Constant Time for insertion, retrieval, and deletion; $O(1)$ space for insertion.
    -Worst Case: $O(n)$ Linear Time (due to frequent collisions requiring multiple scans) and $O(n)$ space (due to array resizing).
'''
'''
Python Dictionaries:
  -Python's dictionaries are implemented as hash maps behind the scenes.
  -To create a Python dictionary, you just need to write the key-value pairs within curly brackets and separate them with a comma.
'''
'''
Sets:
-Sets are unordered collections of unique elements.
-The elements of a set are not stored in any specific order, so you cannot access them through indices.
-Sets only contain unique elements. If you try to add the same value twice, only one copy of the value will be kept.

'''
