#Class initialization with default __init_ method
class Pet:
    def speak(self):
        #print("sound made")
        return ("pet spoke")

Rasmus = Pet()
Rasmus.name = "Rasmus"
print(Rasmus.name)
print(Rasmus.speak())

#A simple class to represent a dog with modified __init_
class Dog:

    species = "Canis familiaris"

    def __init__(self,name,breed,age="N/A"):
        self.name = name #instance attribute
        self.breed = breed
        self.age = age
       
    def speak(self):
        retutn ="{self.name} says Woof!"

koba = Dog("Koba","Pitbull",3) 
amada = Dog("Amada","Bulldog",)
koba.age = 4 
print(koba.speak)
print(koba.age)
print(amada.age)
print(amada.species)
print(amada.name)

print(koba.species)
print(koba.name)

class Cat:
    pass

class Rat:
    pass

