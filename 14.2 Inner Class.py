class car:
    tyres = 4

    def __init__(self, company, model, engine):
        self.company = company
        self.modle = model
        self.engine = engine
        self.inner = self.Seats()

    def show(self):
        print("Yor car is {} {} {} which have {} tyres and {} seats".format(self.company, self.modle, self.engine, car.tyres, self.inner.seat))
    # to call inner clss variable (self.inner.seat)
    # InnerClass
    class Seats:

        def __init__(self):
            self.seat = 5
car = car("Toyota", "Corolla", "1.5")

car.show()
