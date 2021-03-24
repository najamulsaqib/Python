class dad:
    def __init__(self):
        print("Dad's Init")
    def dad_fun(self):
        print("Dad is Brown")

class mom:
    def __init__(self):
        print("Mom's Init")

    def mom_fun(self):
        print("Mom is Brown")

class child(dad, mom): # in this class if you call parent's method if both super classes have same named function it will access to left ones function
    #in this case which is dad
    def child_fun(self):
        super().__init__()
        print("I'm also Brown")

#parent Class Cannot acces child class's methods
dad = dad()
#dad.dad_fun()

#Child class can acces parent class's methods
child = child()
child.dad_fun()
child.mom_fun()
child.child_fun()




class a:
    def A(self):
        print("A")
class b(a):
    def B(self):
        print("B")

class c(b):
    def C(self):
        print("C")


c = c()
c.A()
c.B()
c.C()
