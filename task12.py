class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Salom, men {self.name}, yoshim {self.age} da.")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self):
        print(f"Salom, men {self.name}, yoshim {self.age} da, bahoyim {self.grade}.")

person1 = Person("Ali", 25)
person1.introduce()

student1 = Student("Vali", 18, "A")
student1.introduce()