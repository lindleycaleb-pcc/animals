__author__ = "Caleb Lindley"

# This program creates the class Animal and uses two objects, Dog and
# Cat. It then displays the name of the animal, the animal's color,
# and the sound each animal makes.
#
# Input List: None
# Output List: self._type, self._name, self._color, makeSound()
#
# Class Animal
#   Private String _type = "Animal"
#   Private String _name
#   Private String _color
#
#   Public Module Animal(String name, String color)
#       Set _name = name
#       Set _color = color
#   End Module
#
#   Public Function String get_type()
#       return _type
#   End Function
#
#   Public Function get_name()
#       return _name
#   End Function
#
#   Public Function get_color()
#       return self.color
#   End Function
#
#   Public Module set_name(String value)
#       Set _name = value
#   End Module
#
#   Public Module set_color(String value)
#       Set _color = value
#   End Module
#
#   Public Module (display)
#       Display "A ", self._type, " named ", self._name, "is the color ", self._color
#   End Module
# End Class


class Animal:
    _type = "Animal"
    _name = ""
    _color = ""

    def __init__(self, name, color):
        self._name = name
        self._color = color

    def get_type(self):
        return self._type

    def get_name(self):
        return self._name

    def get_color(self):
        return self._color

    def set_name(self, value):
        self._name = value

    def set_color(self, value):
        self._color = value

    def display(self):
        print(
            "A ",
            self._type,
            " named ",
            self._name,
            " is the color ",
            self._color,
            ".",
            sep="")


# Class Dog Extends Animal
#   Declare Private _type = "Dog"
#
#   Public Module makeSound()
#       Display "self.name, says Woof! Woof!"
#   End Module
# End Class


class Dog(Animal):
    _type = "Dog"

    def makeSound(self):
        print(self._name, "says Woof! Woof!")


# Class Cat Extends Animal
#   Declare Private _type = "Cat"
#
#   Public Module makeSound()
#       Display "self.name, says Meow"
#   End Module
# End Class


class Cat(Animal):
    _type = "Cat"

    def makeSound(self):
        print(self._name, "says Meow")


# Module Main()
#   Declare Animal rocket
#   Declare Animal animals[3]
#
#   Set rocket = New Dog("No name yet", "No color yet")
#   Call rocket.set_name("Rocket")
#   Call rocket.set_color("Black")
#
#   Call rocket.display()
#
#   Set animals = rocket,
#                 New Cat("Theodore", "Orange")
#                 New Dog("Rugor", "Brown")
#
#   Display ""
#   Display "-- All Animals --"
#   For animal in animals
#       Call animal.display()
#       Call animal.makeSound()
#       Display ""
#   End For
# End Module


def main():
    rocket = None
    animals = [None] * 3

    rocket = Dog("No name yet", "No color yet")
    rocket.set_name("Rocket")
    rocket.set_color("Black")

    rocket.display()

    animals = [rocket, Cat("Thoedore", "Orange"), Dog("Rugor", "Brown")]

    print()
    print("-- All Animals --")
    for animal in animals:
        animal.display()
        animal.makeSound()
        print()


main()
