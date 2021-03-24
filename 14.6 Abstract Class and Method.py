from abc import ABC, abstractmethod
# In abstract class we only define methods and impliment them in another class
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Machine is Processing")

class Programmer:
    def Work(self, machine):
        machine.process()
        print("Im Worling on Machine")


machine = Laptop()

worker = Programmer()

worker.Work(machine)