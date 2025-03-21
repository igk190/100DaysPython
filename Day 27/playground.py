# def add(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     print(total)
#     print(numbers[1])
#     # use loop to sum all the arguments insid the funcon

# add(1,2,4,6,7)

# def add(*args):
#     print(type(args))

# add(1,2,3,5,6)

def calc(n, **kwargs):
    print(kwargs)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)

calc(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="VW")
print(my_car.make, my_car.model)