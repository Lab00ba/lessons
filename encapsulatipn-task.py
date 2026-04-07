class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        print(f"Имя {self.__name}")

    @name.setter
    def name(self, new_name):    
        self.__name = new_name

    @property
    def age(self):
        print(f"Возрост {self.__age}")

    @age.setter
    def age(self, new_age):
        if not (0 <= new_age <= 120):
            print("Должен быть в диопозоне от 0 до 120 лет.")
        else:
            self.__age = new_age

p = Person("Biber", 15 )

# p.get_name()
# p.set_name("Lioois")
# p.get_name()

# p.get_age()
# p.set_age(50)
# p.get_age()

print(p.name)
p.name = "Lassos"
print(p.name)
print(p.age)