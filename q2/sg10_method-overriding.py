class Animal: # creates Parent Class: Animal
    def __init__(self, name: str): # initializes the name attribute of the Animal class
        self._name = name

    def eat(self): 
        print(f"{self._name} eats.") # prints the name of the animal and that it eats

    def make_sound(self):
        print(f"{self._name} makes sounds.") # prints the name of the animal and that it makes sounds

# 1st Child Class
class Lion(Animal): # creates Child Class: Lion that inherits from the Parent Class: Animal
    def __init__(self, name: str):
        super().__init__(name) # inherits the name attribute from the Parent Class: Animal

    def make_sound(self):
        print(f"{self._name} roars loudly!") # prints the name of the lion and that it roars loudly

    def eat(self):
        print(f"{self._name} eats fresh meat.") # prints the name of the lion and that it eats fresh meat

# 2nd Child Class
class Elephant(Animal): # creates Child Class: Elephant that inherits from the Parent Class: Animal
    def __init__(self, name: str):
        super().__init__(name) # inherits the name attribute from the Parent Class: Animal

    def make_sound(self):
        print(f"{self._name} trumpets!") # prints the name of the elephant and that it trumpets

    def eat(self):
        print(f"{self._name} eats grass and fruits.") # prints the name of the elephant and that it eats grass and fruits

# 3rd Child Class
class Monkey(Animal): # creates Child Class: Monkey that inherits from the Parent Class: Animal
    def __init__(self, name: str):
        super().__init__(name) # inherits the name attribute from the Parent Class: Animal

    def make_sound(self):
        print(f"{self._name} chatters!") # prints the name of the monkey and that it chatters

    def eat(self):
        print(f"{self._name} eats bananas.") # prints the name of the monkey and that it eats bananas

# OBJECTS
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

# Calling methods
lion.make_sound()  # Output: Simba roars loudly!
lion.eat()         # Output: Simba eats fresh meat.
print("-----")

elephant.make_sound()  # Output: Dumbo trumpets!
elephant.eat()         # Output: Dumbo eats grass and fruits.
print("-----")

monkey.make_sound()  # Output: George chatters!
monkey.eat()         # Output: George eats bananas.
print("-----")