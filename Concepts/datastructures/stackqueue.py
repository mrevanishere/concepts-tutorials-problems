from collections import deque
from queue import LifoQueue

# list stack - not a good implementation - fast indexing
# list is not thread-safe
list_stack  = []
list_stack.append('a')
list_stack.append('b')
list_stack.append('c')
print(list_stack.pop())
print(list_stack.pop())
print(list_stack.pop())

# deque stack - built upon double linked list - indexing is slower, but adding and removing is fatser
# other methods in deque are not thread-safe
deque_stack  = []
deque_stack.append('a')
deque_stack.append('b')
deque_stack.append('c')
print(deque_stack.pop())
print(deque_stack.pop())
print(deque_stack.pop())
# popleft() for queue
# write dequeue to remove something from queue
# write enqueue to add something to queue

# write push to add something to stack
# write pop to remove something from stack

# lifoqueue - good for multi-thread
# thread-safe, but takes longer than deque
q_stack = LifoQueue()
q_stack.put('a')
q_stack.put('b')
q_stack.put('c')
print(q_stack.get())
print(q_stack.get())
print(q_stack.get())
