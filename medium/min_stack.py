# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int value) pushes the element value onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.


class MinStack:

    def __init__(self):
      self.stack = []
      self.min_stack = []
    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(
                min(value, self.min_stack[-1])
            )
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None
    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None
