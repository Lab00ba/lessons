class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        print(f" имя {self.__name}")

    def set_name(self, new_name):
        if len(new_name) <= 2:
           print("Имя слишком короткое")
        else:   
            self.__name = new_name


p = Person("Alex")

p.get_name()
p.set_name("Gecab")
p.get_name()