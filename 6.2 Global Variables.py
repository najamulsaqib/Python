a = 10
print(a)


def global_():
    global a
    a = 15
    print(a)
    globals()['a'] = 17
    print(a)


global_()
