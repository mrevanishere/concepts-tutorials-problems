 '''
 can count:
 logical comparisons
 data interchanges
 arithmetic operations
 etc
 '''
# Big-O
 '''
 Big-O based on ORDER OF MAGNITUDE (highest "degree")
 assume O(f(n)) is a function that
 cf(n), where cn>inf, f(n) is dominated by the highest order term
 so O(f(n)) = O(2n^2) maps 2n^2 to n^2
 so O(f(n)) = O(cm^n) maps cn^m to n^m
 and O(f(n)) = O(n) = n
so
 '''
 # Common
 '''
 1 constant
 log n logarithmic
 n linear
 nlogn log linear
 n^2 quadratic
 n^3 cubic
 n^m polynomial
 a^n exponential
 1 < logn < n < nlogn < n^m < a^n 
'''
# In python
'''
most string operations are proportional to len of string.
print() is constant.
logarithmic2 time happens when halves are made.
nlogn happens when a full loop with a halving.
Different cases have different run times (best, worst, avg)
Python list operations are mostly O(n) worst case, except for index O(1) and initialization O(1)
'''
# Armortized Analysis
'''

'''


