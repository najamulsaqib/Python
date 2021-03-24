def add(a,b):
    print( a/b)

def decor(add):
    def smart(a, b):
        if a<b:
            a,b = b,a
        return add(a, b)
    return smart

add = decor(add)
add(3,1)