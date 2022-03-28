def Fun():
   yield 1
   yield 2
   yield 3

# x is a generator object
x = Fun()
print(next(x))
