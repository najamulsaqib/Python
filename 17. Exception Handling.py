a = 8
b = 2

try :
    print("File open")
    print(a/b)
    n = int(input("Enter a number: "))
except ZeroDivisionError:
    print("Number cannot be divided with Zero")
    
except ValueError:
    print("Invalid Input")

except Exception as e:
    print(e)

finally:
    print("File closed")

# ----- Custom Exception 
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")