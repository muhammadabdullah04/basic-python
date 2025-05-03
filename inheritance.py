class Animal:
    def __init__(self, name):
        self.name = name

    def habitat(self):
        print(f"{self.name} lives on land.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def display(self):
        print(f"Dog Name: {self.name}")
        print(f"Breed: {self.breed}")
        super().habitat()  

d = Dog("Tommy", "German Shepherd")
d.display()
