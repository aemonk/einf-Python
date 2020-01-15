class Person:
    def __init__(self, name, age): #object properties
        self.name = name
        self.age = age

    def myfunc(self): # method
        return "Hello my name is " + self.name

p1 = Person("John", 30) # object

print(p1.__dict__)
print(p1.name) # calling object
print(p1.age) # calling object
print(p1.myfunc()) # calling method

# modify object properties
p1.age = 40
print(p1.age)
print(p1.__dict__)

# delete object properties
del p1.age
#print(p1.age)
print(p1.__dict__)

# delete Objects
#del p1

class Printlist:
    def __init__(self, numberlist):
        self.numberlist = numberlist

    def print_list(self):
        for item in self.numberlist:
            print(f"item {item}")

A = Printlist([1,2,3])
A.print_list()


test = {
    1:1/6,
    2:1/6,
    3:1/6,
    4:1/6,
    5:1/6,
    6:1/6,
}

def mumu(d):
    for key in d:
        print("Key: {}, Val: {:%}".format(key, d[key]))

print(mumu(test))

def foo(d):
    return list(d.items())

print(foo(test))