def func():  # without parameters
    print("Function one")


def func2(fname):  # with parameters
    print("Mty first name is %s" % fname)


def func3(fname, lname):  # with parameters and return
    name = fname + " " + lname
    return name


def func4(name, age=18):  # by default value of age
    print(name + " ", end='')
    print(age)


def func5(*b):  # *b is tuple here. You can pass as much values as you want
    c = 0
    for i in b:
        c += i
    print(c)


def func6(**data):  # multiple variables with keyword (Keyword variable length argument method)
    print(data)
    print("Another method")
    for i in data:
        print(i)
    for i, j in data.items():
        print(i, " : ", j)

fn = "Najam"
ln = "Ul Saqib"

func()
func2(fn)
name = func3(fn, ln)
print(name)
name = func3(lname=ln, fname=fn)  # you can call by defining variables (Keywords method)
func4(name)
func4(name, 21)
func5(1, 2, 3, 4, 5, 6, 7, 8, 9)
func6(name='Najam Ul Saqib', age=21, city='Lalian', Nationality='Pakistan')
