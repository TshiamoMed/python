class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am a {self.gender}, nice to meet you, how are you?.")

# Create an instance of Person
person = Person("Tshiamo", 21, "Male")

# Call the introduce method
person.introduce()
