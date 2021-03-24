# lambda function

# In lambda you can perform calculations
# x is name of lambda function
# a,b is parameters of lambda function there can be only one parameter
# instead of a*b any calculation

x = lambda a, b : a*b
print(x(2, 3))

x = lambda a: a*10
print(x(10))

x = lambda a,b,c: a+b-c
print(x(1,4,3))