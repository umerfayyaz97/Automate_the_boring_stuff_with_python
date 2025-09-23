class Car:
    # This is a CLASS attribute, shared by all instances.
    total_cars_produced = 0

    def __init__(self, model):
        # This is an INSTANCE attribute, unique to each car.
        self.model = model
        # When a new car is made, we call our class method to update the total.
        Car.increment_car_count()

    @classmethod
    def increment_car_count(cls):
        """Increments the total count of cars produced."""
        cls.total_cars_produced += 1

    @classmethod
    def get_total_production(cls):
        """Returns the total number of cars produced."""
        return cls.total_cars_produced

# We can call this method directly on the class, even before any cars are made.
print(f"Total cars produced so far: {Car.get_total_production()}")

print("Producing new cars...")
car1 = Car("Corolla")
car2 = Car("Civic")

# We call the method again to get the updated class attribute.
print(f"Total cars produced now: {Car.get_total_production()}")