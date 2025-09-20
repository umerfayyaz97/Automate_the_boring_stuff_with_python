
class Dog:
    """Attempt to model Dogs """
    def __init__(self, name, age):
        """Initialize attributies """
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting """
        print(f"{self.name} is now sitting")

    def roll(self):
        """Simulate rolling of a dog"""
        print(f"{self.name} rolled over!")

