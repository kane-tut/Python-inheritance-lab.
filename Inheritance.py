# 1. Single Inheritance
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")

class Student(Person):
    def study(self):
        print(f"{self.name} is studying.")

# 2. Multiple Inheritance
class Employee:
    def __init__(self, company):
        self.company = company

    def work(self):
        print(f"Works at {self.company}.")

class Athlete:
    def __init__(self, sport):
        self.sport = sport

    def train(self):
        print(f"Trains in {self.sport}.")

class WorkingAthlete(Employee, Athlete):
    def __init__(self, company, sport):
        Employee.__init__(self, company)
        Athlete.__init__(self, sport)

    def info(self):
        print(f"Employee at {self.company} and athlete in {self.sport}.")

# 3. Multilevel Inheritance
class Animal:
    def eat(self):
        print("Animal is eating.")

class Mammal(Animal):
    def breathe(self):
        print("Mammal is breathing.")

class Dog(Mammal):
    def bark(self):
        print("Dog is barking.")

# 4. Hierarchical Inheritance
class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

class Motorcycle(Vehicle):
    def ride(self):
        print("Motorcycle is riding.")

# 5. Hybrid Inheritance
class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching.")

class TeachingAthlete(Teacher, Athlete):
    def __init__(self, name, sport):
        Teacher.__init__(self, name)
        Athlete.__init__(self, sport)

    def show_role(self):
        print(f"{self.name} teaches and plays {self.sport}.")

# OUTPUT TESTING
print("=== Single Inheritance ===")
s = Student("Juan")
s.introduce()
s.study()

print("\n=== Multiple Inheritance ===")
wa = WorkingAthlete("Tech Corp", "Basketball")
wa.work()
wa.train()
wa.info()

print("\n=== Multilevel Inheritance ===")
d = Dog()
d.eat()
d.breathe()
d.bark()

print("\n=== Hierarchical Inheritance ===")
c = Car()
m = Motorcycle()
c.move()
c.drive()
m.move()
m.ride()

print("\n=== Hybrid Inheritance ===")
ta = TeachingAthlete("Maria", "Volleyball")
ta.introduce()
ta.teach()
ta.train()
ta.show_role()
