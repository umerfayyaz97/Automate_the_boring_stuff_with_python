
# class Dog:
#     """Attempt to model Dogs """
#     def __init__(self, name: str, age: int):
#         """Initialize attributies """
#         self.name  = name
#         self.age  = age 
#         self.play_streak = 0
    
#     def sit(self):
#         """Simulate a dog sitting """
#         print(f"{self.name} is now sitting")

#     def roll(self):
#         """Simulate rolling of a dog"""
#         print(f"{self.name} rolled over!")
    
#     def update_streak(self, days:int):
#         """Update days of streak"""
#         self.play_streak = days
        


# my_dog = Dog("tommy", 2)

# print(my_dog.name)
# my_dog.sit()

# my_dog.update_streak(5)
# print(my_dog.play_streak)



class Car:
    """Model a car"""

    def __init__(self,make:str, model:str, year:int):
        self.make = make
        self.model = model 
        self.year = year
        self.odo_meter = 0
        

    def get_descriptive_name(self):
        """Get full Name of Car"""
        long_name = f"{self.make} {self.model} {self.year} "
        return long_name.title()
    
    def  read_odometer(self):
        print(f"Car has {self.odo_meter} miles on it")

    def update_odometer(self, mileage:int):
        if mileage >= self.odo_meter:
            self.odo_meter = mileage
        else:
            print("You cannot reverse meter")
    


    

class ElectricCar(Car):
    """Represent electric car"""
    
    def __init__(self, make:str, model:str, year:int):
        #call the parents init to handle common attributes
        super().__init__(make,model,year)
        self.battery = Battery(65)


class Battery:

    """Model battery"""

    def __init__(self, batteryWatt: int):
        self.battery_watt = batteryWatt

    def describe_battery(self):
        print(f'This car has {self.battery_watt}-KWH battery')
    
    def get_miles(self):
        """Print range of car depending on battery size"""
        if self.battery_watt == 40:
            range = 80
        elif self.battery_watt == 65:
            range = 150

        print(f"This car can go {range} miles on a full charge")

    

my_prius = ElectricCar("Toyota", "Prius", 2004)

print(my_prius.get_descriptive_name())
my_prius.battery.describe_battery()
my_prius.battery.get_miles()


        


        