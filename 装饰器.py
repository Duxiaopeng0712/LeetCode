def addition(func):
    def inner(a,b):
        print("numbers are",a,"and",b)
        return func(a,b)
    return inner

@addition
def add(a,b):
   print(a+b)

add(5,6)
