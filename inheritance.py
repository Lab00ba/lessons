# class Animal:
#     def speak(self):
#         print("Животное издает звуки")

# class Dog(Animal):
#     def bark(self):
#         super().speak()
#         print("Собака лает")

# class Cat(Animal):
#     def meow(self):
#         super().speak()
#         print("Кошека мяукает")

# dog = Dog()
# cat = Cat()

# cat.speak()
# cat.bark()

# class Animal:
#     def __init__(self,name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self,name, bread):
#         super().__init__(name)
#         self.bread = bread

# dog = Dog("Rex", "Овчарка")

# print(dog.name)
# print(dog.bread)