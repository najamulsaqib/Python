from array import *
"""
'b' --> Signed Char
'B' --> Unsigned Char
'u' --> Py Unicode
'h' --> signed Short
'H' --> unsigned Short
'i' --> signed int
'I' --> unsigned int
'l' --> signed ling
'L' --> unsigned long
'f' --> float
'd' --> double
"""

a = array('i', [])
a.append(12)
a.append(2)
a.append(1)
a.append(13)
a.append(112)
print(a)
print(a[0])

for i in range(len(a)):
    print(a[i], " ", end="")

print()

for i in a:
    print(i, " ", end="")