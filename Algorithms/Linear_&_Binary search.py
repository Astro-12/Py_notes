'''
Linear Search:
  -Linear search starts at the beginning of a list and iterates through each item until it finds the target value it is looking for. 
  -After getting found the index of the target item is returned.If the target value isn't found, -1 is returned.
'''
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
'''
Time space complexity of linear search:
  -The time complexity of linear search is O(n) because the time it takes to search through the list grows linearly with the size of the list.
-The space complexity of linear search is O(1) because it only uses a constant amount of extra space, like the loop variable i. The amount of extra storage does not grow with the length of the list.
'''
'''
Binary Search:(List should be ordered in ascending order)
  -Binary search works by dividing the list in half and checking if the target value is in the middle of the list. If the target value is in the middle of the list, 
    the index of the target value is returned. Otherwise, the algorithm checks if the target value is in the left or right half of the list.
  -It continues to divide the remaining parts of the list into halves until the target value is found. If the target value is not in the list, it returns -1.
''' 
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
'''
  -Binary search basically works on the formula [low + (high - low) // 2]
  -While low <= high, binary search checks the mid element—returning its index if it matches, moving low = mid + 1 to search right if too small,
  or high = mid - 1 to search left if too large. If low passes high without a match, it stops and returns -1.
'''
'''
Time and Space Complexity of Binary Search:
  -The time complexity of binary search is O(log n) because the time it takes to search through the list grows logarithmically with the size of the list.
  -The space complexity of binary search is O(1) because it only uses a constant amount of extra space for the low, high, and mid variables. 
    The amount of extra storage does not grow with the length of the list.
'''
