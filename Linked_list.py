'''
Linked List:
  -A linked list is a linear data structure in which each node is connected to the next node in the sequence.
  -Linked lists are commonly used for implementing other data structures, such as stacks, queues, and deques. They can also be used to implement essential graph algorithms, such as depth-first search and breadth-first search.
Singly Linked Lists:
  -A singly linked list is a type of linked list in which each node is connected to the next node in the sequence.
  -Each node is connected to the next one by storing a reference to it.
  -The search can only move forward, not backwards.
Inserting Nodes:
  -You can insert a node at the start, middle, and end of a linked list.
  -Linked lists don't necessarily need to store the nodes in a specific order. The order will be determined by the connections between the nodes.
    Inserting Conditions:
    -Inserting a node at the beginning of the linked list has a constant time complexity O(1) because it only requires updating the reference to the head node and the connection between the new head node and the next node in the sequence.
    -This operation has linear time complexity, O(n), where n is the number of nodes stored in the linked list, 
      because first you need to reach the end of the linked list to make the insertion and this would require going from one node to the next and so on until the end is reached.
    -The insertion operation has a constant space complexity O(1), since inserting a new node only requires creating it and updating the connections between the nodes. This operation doesn't depend on the size of the linked list itself.
Doubly Linked Lists:
  -In a doubly linked list, each node stores two references: a reference to the next node and a reference to the previous node in the sequence.
  -The insertion and deletion operations work exactly the same. The only difference is that now you will need to update two references per node and keep track of the 
    reference to the tail node to insert elements at the end of the doubly linked list very efficiently and start the traversal process from the back, if necessary.
'''
