# object = a "bundle" of related attributes (variables) and methods (functions)
#         ex. phone, cup, booking
#         You need a class to create many objects

#  class = (blueprint) used to design the structure and layout of an object
from car import *


car1 = Car(make="BMW",model="M3",year=2024,color="Red",for_sale=True)
car2 = Car(make="Toyota",model="Supra",year=2021,color="Black",for_sale=False)
print(car1.make)

car1.drive()
car1.describte()