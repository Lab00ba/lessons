class Worker:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def name(self):
        return f"Имя {self.__name}"

    @name.setter
    def name(self, new_name):    
        self.__name = new_name

    @property
    def salary(self):
        return f"Зарплата {self.__salary}"

    @name.setter
    def salary(self, new_salary):    
        self.__salary = new_salary

class Manager(Worker):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def info(self):
        return f"Имя {self.name}, зарплата {self.salary}, отдел {self.department}"
    
class Developer(Worker):
    def __init__(self, name, salary, level):
        super().__init__(name, salary)
        self.level = level

    def info(self):
        return f"Имя {self.name}, зарплата {self.salary}, отдел {self.level}"
    
m = Manager("Max", 400000, "Машины")
d = Developer("Егор", 500000, "middle")

print(m.info())
print(d.info())
