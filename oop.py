# variable list tuple all include in python is object oriented programming(oop)

# oop two part 1 property 2 method

# (.) diye property and method ke indicate kore
"""

li = [1,2,3]
print(dir(li))

"""
"""

li =[1,2,3]
li.reverse()  
print(li)

x = 7
print(dir(x))    # __add__ [magic method] , 'imag'

"""
"""
class myclass:
    pass
a_obj = myclass()
print(type(a_obj))


"""

"""
class myclass:
    value1 = 10
    value2 = 10023

a_obj = myclass
print(a_obj.value1)
b_obj = myclass
print(b_obj.value1)
c = myclass
print(c.value2)

"""
"""

class car:
    color = "white"

car1 = car ()   
car2 = car ()   
car3 = car ()
print(car1.color)
print(car1.color,car2.color,car3.color)  


class car:
    color = "white"

car1 = car ()   
car2 = car ()   
car3 = car ()
car1.color = "red"
print(car1.color)
print(car1.color,car2.color,car3.color) 

class car:
    color = "white"
    manufacturer = "toyata"
    brand = "corolla"

car1 = car ()   
car2 = car ()   
car3 = car ()
car1.color = "red"
print(car1.color)
print(car1.color,car2.manufacturer,car3.brand) 

class car:
    color = "white"
    manufacturer = "toyata"
    brand = "corolla"
    def __init__ (self):        # constructor method (this method called automatically)
        print("I am called")

car1 = car ()   
car2 = car ()   
car3 = car ()
car1.color = "red"
print(car1.color)
print(car1.color,car2.manufacturer,car3.brand) 


"""


"""

class car:
    color = "white"
    manufacturer = "toyata"
    brand = "corolla"
    def __init__ (self):        # constructor method (this method called automatically)
        print("I am called")

car1 = car()

print(car1.color)

car1 = car ()   
car2 = car ()   
car3 = car ()
car1.color = "red"
print(car1.color)
print(car1.color,car1.manufacturer,car1.brand)

class car:
    def __init__(self,a,b,c):
        self.make = a
        self.model = b
        self.color = c

car1 = car("subaru","forester","bronze")
print(car1.color,car1.make,car1.model)        


class car:
    def __init__(self,a,b,c= "red"):
        self.make = a
        self.model = b
        self.color = c

car1 = car("subaru","forester","bronze")
car1.color = "blue"
print(car1.color,car1.make,car1.model)  


class car:
    def __init__(self,a,b,c= "red"):
        self.make = a
        self.model = b
        self.color = c

car1 = car("forester","bronze")

print(car1.color,car1.make,car1.model)

class car:
    def __init__(self,a,b,c= "red",d = 2023):
        self.make = a
        self.model = b
        self.color = c
        self.year = d

car1 = car("forester","bronze")


print(car1.color,car1.make,car1.model,car1.year)



class car:
    def __init__(self,a,b,c= "red",d = 2023):
        self.make = a
        self.model = b
        self.color = c
        self.year = d

car1 = car("forester","bronze")
car2 = car ("white","toyota","parado")
car1.year = 2024


print(car1.color,car1.make,car1.model,car1.year)
print(car2.color,car2.make,car2.model,car2.year)

"""
"""

import time
class car:

    year = 2024
    def __init__(self,a,b,c= "red",d = 2023):
        self.make = a
        self.model = b
        self.color = c
        self.year = d
    
    def __str__(self):
        return f'{self.make}-{self.model}-{self.year}'

#  function bitor method use(start_rngin)method
    def start_engine(self , t=1):
        self.year = 1900
        print(self.year)
        print("starting engine....")
        time.sleep(t)
        print("engine started!")
           

car1 = car("forester","bronze")
car2 = car ("white","toyota","parado")
car3 = car("toyota","co")
car1.year = 2024


print(car1.color,car1.make,car1.model,car1.year)
print(car2.color,car2.make,car2.model,car2.year)
print(car3)
print("before start ergine", car1.year)

car1.start_engine()
print("after start ergine", car1.year)

car1.start_engine() # 1 s gape by defolt 1
car2.start_engine(0) # on time
car1.start_engine(5)  # 5 s late


"""

"""
# Inharitance

class A:
    def __init__(self):
        print("Creating object for class A")

a = A() 
b = A()       
"""


"""
class A:
    def __init__(self):
        print("Creating object for class A")

class AA(A):
    pass
a = A() 
b = A() 
c = AA()
"""

"""
class A:
    def __init__(self):
        print("Creating object for class A")

class AA(A):
         def __init__(self):
             print("Creating object for class AA")
a = A() 
b = A() 
c = AA()

"""


class A:
    def __init__(self):
        print("Creating object for class A")
   
    def jump (self):
         print("i am jumping")
class AA(A):
         def __init__(self):
             print("Creating object for class AA")
a = A() 
b = A() 
c = AA()
a.jump()
c.jum()






