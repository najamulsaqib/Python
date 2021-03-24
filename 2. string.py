x = "nAjAm"

print(x.title())  # It will capitalize first letter and lower others
print(x.upper())  # it will convert all letters to upper case
print(x.lower())  # it will convert all letters to lower case

# with triple quotes the same format will be printed
x = """
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are
"""
print(x)

# \ (Backslash) can be used to print " or ' (Double or single quotation) in print function
print("'")  # inside double quotes you can use single quotes
print("\"")

print('"')  # inside single quotes you can use double quotes
print('\'')

# Raw String
print(r" \t \n ")  # r can be use to print raw string (It will ignore \t \n )
# You can also store raw string in a variable
raw = r"\t\n Najam"
print(raw)
