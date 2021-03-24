#When we add two thingns in backend it calls __add__() function. 
# Like add python have many more functions __mul__(), __sub__() and others
# So with function overloading we can change functionalites of there functions.

class student:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    def __add__(self, other):
        n1 = self.n1 + other.n1
        n2 = self.n2 + other.n2
        return n1 + n2
        
    def __sub__(self, other):
        n1 = self.n1 - other.n1
        n2 = self.n2 - other.n2
        return n1 - n2

    def __eq__(self, other):
        if self.n1 == other.n1:
            return "Both Are Equal"
        else:
            return "Both are not equal"
s1 = student(5, 3)
s2 = student(3, 6)

print(s1 + s2)
print(s1 - s2)
print(s1 == s2)
    