class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.name + " says " + self.sound)

animal1 = Animal("Dog", "Woof")
animal1.make_sound()

animal2 = Animal("Cat", "Meow")
animal2.make_sound()