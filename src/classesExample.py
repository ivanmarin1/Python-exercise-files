class myClass:
    "a simple class"
    i = 21                  #common variable
    #def __init__(self, n):
        #self.i = n
    
    def set(self, n):
        self.j = n      #unique variable to class instance
        
    def get(self):
        return self.j

    def fun(self):
        return self.i

#print("I just made", myClass().__doc__)
x = myClass()

name1 = "Ivan"
name2 = "Mia"

y = myClass()
x.set(name1)
y.set(name2)

print("I am", x.get())
print("My sister is", y.get())

print("My sister is", y.i, "years old!")
print("I am", x.i, "years old!")

class emptyClass:
    pass

john = emptyClass()
john.name = "John"

print("\nHello! My name is", john.name)





