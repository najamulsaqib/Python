# Traditional way to perform Iteratord        
# x = [1,2,3,4,5,6]

# v = iter(x)

# for i in v:
#     print(i)
    

class Val:
    def __init__(self):
        self.num = 1
    
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
            
        
    
val = Val()

for i in val:
    print(i)
