# There are only 2 loops in python
# For loop
# While loop
i = 0
while i <= 10:
    print(i,end='')
    i += 3
print("")

for i in range(0, 10, 3):
    # range(a,b) function will provide numbers staring from a till b-1
    # range(a,b,c) it will start from a end till b-1 with increment of c
    # Here it will start numbers from 0 to 10 with increment of 3
    # Value of range() function will be saved in i
    print(i, end='')
print("")

list = [0, 3, 6, 9]
for i in list:
    # values of list will be allocated to i
    print(i, end='')
print("")