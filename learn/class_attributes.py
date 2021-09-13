
# Attributes on the fly
class User:
    pass


user_1 = User()
user_1.username = "Chandra"

user_2 = User()
user_2

# NOTE 1 : You can define "object" attributes on the fly
print(user_1.username)
# AttributeError: 'User' object has no attribute 'username'
# print(user_2.username)


# Class Attributes
class Person:
    count_male = 0

    def __init__(self, is_male):
        if is_male:
            Person.count_male += 1


chandra = Person(True)
sireesha = Person(False)
print(Person.count_male)
mohan = Person(True)
print(Person.count_male)


# Object Attributes
class Employee:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


e_chandra = Employee("Chandra")
e_sireesha = Employee("Sireesha")
print(e_chandra.name)
print(e_sireesha.name)

# AttributeError: type object 'Employee' has no attribute 'name'
# print(Employee.name)

e_mohan = e_chandra  # Reference to the same object
print(e_mohan.name)
e_mohan.name = "Mohan"
print(e_mohan.name)
print(e_chandra.name)
