#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1) Inheritance in OOps :  is like a family tree, where new classes (children) can inherit traits and behaviors from existing classes (parents). It's used to reuse code, extend functionality, and organize classes into hierarchies, making programming more efficient and flexible.


# In[ ]:


#2) Single Inheritance:
- A class can inherit from only one superclass.
- Simplifies class hierarchy and avoids ambiguity.

Multiple Inheritance:
- A class can inherit from more than one superclass.
- Allows for combining features from multiple sources but can lead to complexity and ambiguity.

Advantages:
- Single Inheritance: Simplicity and clarity.
- Multiple Inheritance: Flexibility and code reuse.



# In[ ]:


#3) Base Class:
- The class that is used as a foundation or template for other classes.
- It defines common attributes and methods that are shared by its derived classes.

Derived Class:
- A class that inherits attributes and methods from a base class.
- It can extend the functionality of the base class by adding new features or modifying existing ones.


# In[ ]:


#4) Protected Access Modifier:
- Allows access to members within a class and its subclasses.
- Provides a balance between encapsulation and inheritance.
- Members are not accessible outside the class hierarchy.

Private Access Modifier:
- Restricts access to members to only within the class where they are defined.
- Provides the highest level of encapsulation and data hiding.
- Members are not accessible in subclasses or outside the class.

Public Access Modifier:
- Allows access to members from anywhere, both within and outside the class hierarchy.
- Members can be accessed and modified by instances of the class, subclasses, and any other code with access to the class.


# In[1]:


#5)  the super keyword in inheritance is used to access and call methods or constructors of the parent class (superclass) from within a subclass. This allows for reusing code and extending the functionality of the parent class.
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I'm {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        super().greet()
        print(f"I am {self.age} years old")

child = Child("Alice", 10)
child.greet()



# In[2]:


#6) 
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle: {self.year} {self.make} {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()
        print(f"Fuel Type: {self.fuel_type}")


# Creating an instance of Car
car = Car("Toyota", "Camry", 2022, "Gasoline")
car.display_info()


# In[3]:


#7)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: ${self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

# Creating instances of Manager and Developer
manager = Manager("Alice", 90000, "HR")
developer = Developer("Bob", 80000, "Python")

# Displaying information
manager.display_info()
print()
developer.display_info()


# In[4]:


#7)
class Shape:
    def __init__(self, colour, border_width):
        self.colour = colour
        self.border_width = border_width

    def display_info(self):
        print(f"Shape Colour: {self.colour}")
        print(f"Border Width: {self.border_width} units")


class Rectangle(Shape):
    def __init__(self, colour, border_width, length, width):
        super().__init__(colour, border_width)
        self.length = length
        self.width = width

    def display_info(self):
        super().display_info()
        print(f"Rectangle Length: {self.length} units")
        print(f"Rectangle Width: {self.width} units")


class Circle(Shape):
    def __init__(self, colour, border_width, radius):
        super().__init__(colour, border_width)
        self.radius = radius

    def display_info(self):
        super().display_info()
        print(f"Circle Radius: {self.radius} units")


# Creating instances of Rectangle and Circle
rectangle = Rectangle("Red", 2, 10, 5)
circle = Circle("Blue", 1, 7)

# Displaying information
rectangle.display_info()
print()
circle.display_info()


# In[5]:


#8) 
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")


class Phone(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size

    def display_info(self):
        super().display_info()
        print(f"Screen Size: {self.screen_size} inches")


class Tablet(Device):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} mAh")


# Creating instances of Phone and Tablet
phone = Phone("Samsung", "Galaxy S21", 6.2)
tablet = Tablet("Apple", "iPad Pro", 9720)

# Displaying information
phone.display_info()
print()
tablet.display_info()


# In[6]:


#9)
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")


class Phone(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size

    def display_info(self):
        super().display_info()
        print(f"Screen Size: {self.screen_size} inches")


class Tablet(Device):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} mAh")


# Creating instances of Phone and Tablet
phone = Phone("Samsung", "Galaxy S21", 6.2)
tablet = Tablet("Apple", "iPad Pro", 9720)

# Displaying information
phone.display_info()
print()
tablet.display_info()


# In[7]:


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest calculated: ${interest:.2f}")
        print(f"New Balance: ${self.balance:.2f}")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, fee):
        super().__init__(account_number, balance)
        self.fee = fee

    def deduct_fees(self):
        self.balance -= self.fee
        print(f"Fees deducted: ${self.fee:.2f}")
        print(f"New Balance: ${self.balance:.2f}")


# Creating instances of SavingsAccount and CheckingAccount
savings_account = SavingsAccount("SA123456", 1000, 1.5)
checking_account = CheckingAccount("CA654321", 500, 5)

# Displaying information
savings_account.display_info()
print()
savings_account.calculate_interest()
print()
checking_account.display_info()
print()
checking_account.deduct_fees()


# In[ ]:




