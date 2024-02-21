class Person:
    def __init__(self):
        self.name = input("Enter your name:")
        self.number = int(input("Enter your number:"))
        self.age = int(input("Enter your age:"))

    def display(self):
        print("My name is "+self.name+"; My Number is",self.number,"and My Age is",self.age,".")

Shahanas = Person()
Shahanas.display()