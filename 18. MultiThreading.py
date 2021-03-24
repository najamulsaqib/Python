# Multi Threading is way to perform multi tasking 
# We can call two functions of different class at same time
# 
from time import sleep
from threading import Thread

class Hello(Thread):
    def run(self): # For threading it is must to have a run() function
        for i in range(5):
            sleep(1) # Because its execution time is very fast we need to stop execution for 1 sec to see multiThreading.
            print("Hello")

class Hi(Thread):
    def run(self):
        for i in range(5):
            sleep(1) 
            print("Hi")

obj1 = Hello()
obj2 = Hi()

obj1.start()    # We are calling start because in threading it will automatically call run() function. 
                # Thats why it is must to have run() function inside a thread class
sleep(0.2)      # to avoid collosion between both tasks
obj2.start() 

print("What?") # it will be executed somewhere between Obj1 and obj2.


obj1.join() # join() will make sure that execution of Obj1 is completed 
obj2.join() # join() will make sure that execution of Obj2 is completed 

print("BYE") # it will be printed after execution of both obj1 and obj2