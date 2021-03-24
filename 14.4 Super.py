class a:
    def A(self):
        print("A")
class b(a):
    def B(self):
        super().A()
        print("B")

class c(b):
    def C(self):
        super().B()
        print("C")


obj = c()
obj.C()