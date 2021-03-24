from numpy import *

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

print("Enter %d values separated by spaces: " %(r*c), end='')
a = list(map(int, input().split()))
m1 = array(a).reshape(r, c)

print("Enter %d values separated by spaces: " %(r*c), end='')
a = list(map(int, input().split()))
m2 = array(a).reshape(r, c)
m3 = []
for i in range(0, c):
    for j in range(0, r):
        m = m1[i][j] * m2[i][j]
        m3.append(m)
m3 = array(m3).reshape(r, c)
print("Multiplication of Matrix are: ")
print(m3)
