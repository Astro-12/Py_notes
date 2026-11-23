'''
Divide and conquer:
  -divide and conquer paradigm in computer science is a technique for recursively breaking down problems into smaller sub-problems. 
  -One of the key aspects of this technique is recursion, which happens when a function calls itself repeatedly until a base case is reached.
  -Base Case in Merge Sort: A list with 0 or 1 element (len(arr) <= 1). Single-element lists are already sorted by definition.
2. How Merge Sort Works 
Divide: Find the midpoint (mid) and split the list into left and right halves until every piece has length 1.
Conquer (Recurse): Recursively sort the left and right halves.
Combine (Merge): Walk through both sorted halves using two pointers (i and j), repeatedly picking the smaller current element into a new sorted_list, then appending any remaining elements.

'''
def merge_sort(arr):
    # Base case: lists of size 0 or 1 are already sorted
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge two sorted halves
    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list
  '''
  Time complexity:O(nlogn):logn levels of halving, with O(n) merging work per level
  Space complexity:O(n):Allocates new lists during merging (not an in-place sort)
  '''
