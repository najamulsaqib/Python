# if else
# Program to check  number is positive, negative or Zero

i = int(input("Enter a number: "))
if i < 0:
    print("Your number is Negative")
elif i == 0: # elif is used in python  instead of else if
    print("Number is Zero")
else:
    print("Number is Positive")