# Car Class
# by Luis Amador
# 11/5/24

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0


    def accelerate(self, speed):
        self.__speed = speed + 5

    def brake(self, speed):
        self.__speed = speed - 5

    def get_speed(self):
        return self.__speed

def main():
    # gathering the base info
    year = int(input("What year was your car made?: "))
    make = input("What is the make of your model?: ")

    car = Car(year,make)
    print("List of speed changing: ")
    
    for i in range(6):
        car.accelerate(1)
        print(car.get_speed())
        car.brake(1)
        print(car.get_speed())

    print(" ")
    print("Year:", year)
    print("Make:", make)
    print(car.get_speed())


main()