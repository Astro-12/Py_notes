'''
Algorithm:
    -An algorithm is a set of unambiguous instructions for solving a problem or carrying out a task.
  Key_characterstics:
    -They cannot continue indefinitely. They must finish in a finite number of steps.
    -Each step must be precise and unambiguous.

What's Big O notation:
  -Big O notation describes the worst-case performance, or growth rate, of an algorithm as the input size increases.
  -Big O notation focuses on the worst-case performance because this case is very important to understand how efficient the algorithm can be, even in the worst case scenario, regardless of the input.

Input Size and Dominant Terms:
  - We usually denote input size with the letter n
  -The term that will dominate the overall behavior of the algorithm will be the highest order term with n, the input size.
  For ex:
    -Example would be an algorithm that takes 20n² + 15n + 7 operations to be completed. The term 20n² will tend to dominate as n grows, so this algorithm would have a quadratic time complexity because the dominant term has n².
'''
'''
Time Complexities:
    -'O(1)' is known as "Constant Time Complexity". When an algorithm has constant time complexity, it takes the same amount of time to run, regardless of input size.
      For ex:
'''
      def check_even_or_odd(number):
        if number % 2 == 0:
            return 'Even'
        else:
            return 'Odd'
'''
-O(log n) is known as "Logarithmic Time Complexity". This means that the time required by the algorithm increases slowly as the input size grows. 
This is common in problems in which the size of the problem is repeatedly reduced by a constant fraction.
  -For example, a popular search algorithm called Binary Search has O(log n) worst-case time complexity. This is because it eliminates half of the remaining elements in each comparison, which makes it more efficient overall.
'''
'''
-O(n) is known as "Linear Time Complexity". The running time of algorithms with this time complexity increases proportionally to the input size.
-For example, a for loop that iterates over all the elements of a list will perform more iterations as the number of list elements increases. If the list is doubled in size, the number of operations will approximately double as well.
'''
'''
-O(n log n) is known as "Log-Linear Time Complexity". This is a common time complexity of efficient sorting algorithms, like Merge Sort and Quick Sort.
'''
'''
-O(n²) is known as "Quadratic Time Complexity". The running time of these algorithms increases quadratically relative to the input size, which is generally not efficient for real-world problems.
'''
'''
Space Complexity:
-It describes how the memory space required by the algorithm grows as the input size grows.

-Algorithms with "Constant Space Complexity" O(1) always require a constant amount of memory space, even as the input gets larger.
-
'''
