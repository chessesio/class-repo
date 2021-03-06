# class ElectricSocket:
#     pass

# class USSocket(ElectricSocket):
#     pass

# class UKSocket(ElectricSocket):
#     pass

# andrew = USSocket()

# edem = UKSocket()

# print(isinstance(andrew,ElectricSocket))
# print(isinstance(edem,ElectricSocket))

#_______________________________________________________________________________________________________________________________________________________________________

# Polymorphism: ability for an object to take different forms

# class Person:

#     def __init__(self,complaint="no internet:\("):
#         self.complaint = complaint

#     def complain(self):
#         print(self.complaint)


# class EIT(Person):
#     pass

# class Fellow(Person):
#     pass

# class Cat:
#     pass
# people = list()

# for _ in range(7):
#     people.append(Fellow())

# for _ in range(58):
#     people.append(EIT())

# for _ in range(5):
#     people.append(Cat())

# for person in people:
#     if isinstance(person,Person):
#         person.complain()
#     else:
#         print("You're not human :\(")

#______________________________________________________________________________________________________________________________________


# Enscapulation: Restricting how fields are accessed and modified outside a class

# 1. Create a method that lets you change password given the current password
# 2. Hash the password when secret is created
# class Secret:

#     def __init__(self,secret,password):
#         self.__secret = secret
#         self.__password = password

#     def get_secret(self, password):
#         if password == self.__password:
#             print(self.__secret)

#         else:
#             print("Wrong password!")

#     def change_password(self, old_password, new_password):
#         if old_password == self.__password:
#             self.__password = new_password
#             print("Password changed successfully.")

#         else:
#             print ("Wrong password!!")

# andrew_secret = Secret("I am beautifull","thetruth")
# andrew_secret.get_secret("thetruth")
# andrew_secret.change_password("thetrutth","issalie")

#_________________________________________________________________________________________________________________________________________

# Class composition: The concept that a class can contaion and operate instances of another class or itself.

class Egg:

    def __init__(self,color,is_broken=False):
        self.__color = color
        self.__is_broken = is_broken

    def drop(self):
        self.__is_broken = True

class Carton:

    def __init__(self):
        self.eggs = []

    def add_egg(self, egg):
        self.eggs.append(egg)

    def drop_egg(self):
        egg = self.eggs.pop()
        egg.drop()
        return egg