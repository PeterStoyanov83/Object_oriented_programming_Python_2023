# class Stack:
#     def __init__(self):
#         self.data = []
#
#     def push(self, element):
#         if isinstance(element, str):
#             self.data.append(element)
#         else:
#             raise ValueError("Stack can only store strings.")
#
#     def pop(self):
#         if not self.is_empty():
#             return self.data.pop()
#         else:
#             raise IndexError("Stack is empty.")
#
#     def top(self):
#         if not self.is_empty():
#             return self.data[-1]
#         else:
#             raise IndexError("Stack is empty.")
#
#     def is_empty(self):
#         return len(self.data) == 0
#
#     def __str__(self):
#         stack_str = ", ".join(reversed(self.data))
#         return f"[{stack_str}]"


from typing import List


class BaseStack:
    def __init__(self):
        self.data: List[str] = []

    def is_empty(self):
        return False if self.data else True

    def __str__(self):
        return f' [{", ".join(reversed(self.data))}]'


class AddStack(BaseStack):
    def push(self, element: str):
        self.data.append(element)


class RemoveStack(BaseStack):
    def pop(self):
        return self.data.pop()

class TopStack(BaseStack):
    def top(self):
        return self.data[-1]


class Stack(AddStack, RemoveStack, TopStack):
    pass


