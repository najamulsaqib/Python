from numpy import *
m = matrix('1,2,3;4,5,6;7,8,9')
m1 = matrix('11,12,13;14,15,16;17,18,19')
m2 = m + m1
print(m2)
print(diagonal(m)) # to find diagonal of matrix
print(m.min()) # to find min
print(m.max()) # to find max
print(m)