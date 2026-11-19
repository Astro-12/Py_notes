'''
Recursion:
  -Technique in which a function calls itself.
  -Each calls work on a smaller version of the original problem until it reaches a condition, which breaks the recursion.
  -the breaking condition is known as base case
'''
def recursive_countdown(number):
    if number < 1:#base case
        return
    print(number)
    recursive_countdown(number - 1)#recursive case
    #recursive case calls the function again with an argument that moves it toward the base case
recursive_countdown(5)
#Output: 5,4,3,2,1
'''
Changing the order of execution:
'''
def recursive_countdown(number):
    if number < 1:
        return
    recursive_countdown(number - 1)
    print(number)

recursive_countdown(5)
#Output: 1,2,3,4,5
'''
What's call stack:
  -Call stack is a last-in, first-out data structure that Python uses to keep track of active function calls.
  -When a function is called, Python adds a frame for that call to the top of the stack. The frame contains information such as the function's arguments and local variables.
'''
