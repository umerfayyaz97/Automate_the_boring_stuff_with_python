
class Dog:
    """Attempt to model Dogs """
    def __init__(self, name: str, age: int):
        """Initialize attributies """
        self.name  = name
        self.age  = age 
        self.play_streak = 0
    
    def sit(self):
        """Simulate a dog sitting """
        print(f"{self.name} is now sitting")

    def roll(self):
        """Simulate rolling of a dog"""
        print(f"{self.name} rolled over!")
    
    def update_streak(self, days:int):
        """Update days of streak"""
        self.play_streak = days
        


my_dog = Dog("tommy", 2)

print(my_dog.name)
my_dog.sit()

my_dog.update_streak(5)
print(my_dog.play_streak)