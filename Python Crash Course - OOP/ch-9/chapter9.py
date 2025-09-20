
class Dog:
    """Attempt to model Dogs """
    def __init__(self, name: str, age: int):
        """Initialize attributies """
        self.name  = name
        self.age  = age 
    
    def sit(self):
        """Simulate a dog sitting """
        print(f"{self.name} is now sitting")

    def roll(self):
        """Simulate rolling of a dog"""
        print(f"{self.name} rolled over!")


my_dog = Dog("tommy", 2)

print(my_dog.name)
my_dog.sit()