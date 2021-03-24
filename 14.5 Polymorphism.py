#Mathod Over-loading and method over-riding
# method overloading is not supported in python so ve can use a trick to perform it.
#Method overloadig
class A:
    def sum(self, a=None, b=None, c=None):
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s
        

a = A()
print("sum is ",a.sum(10,12,14))
print("sum is ",a.sum(10,14))
print("sum is ",a.sum(14))


# Methos over riding

class B: 
    def a(self):
        print("In B Class")
        
class C(B): # Class C extends Class B
    def a(self):
        print("In C Class")
        super().a()
        
x = B()
y = C()

x.a()
y.a()

