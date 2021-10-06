# Global Variables
x = "awesome" # outside function

def myfunc():
  print("Python is " + x)

myfunc()

# Ex2
x = "awesome"

def myfunc():
  x = "fantastic" # same name variable global
  print("Python is " + x)

myfunc()

print("Python is " + x)

# The global Keyword
def myfunc():
    global x # create x in function, mark it as global
    x = "fantastic"

myfunc()

print("Python is " + x)


# The global Keyword 2
x = "awesome"

def myfunc():
  global x # change value global in function
  x = "fantastic"

myfunc()

print("Python is " + x)