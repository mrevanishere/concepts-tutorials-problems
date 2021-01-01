from array import ArrayType
import random
import ctypes

ArrayType1 = ctypes.py_object * 5
slots = ArrayType1()
print(slots) # has 5 elements

pyList = [ 4, 12, 2, 34, 17 ]

pyList.append(50) # append
pyListB = [ 5, 10, 3 ]
pyList.extend(pyListB) # extend with B
# insert(index, value)
# pop(index=last)

# Array Implementation