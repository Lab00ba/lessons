class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            raise ValueError("цена не может быть отрицательной!!!")
    def info(self):
        return f"Название: {self.name}, Цена: {self.__price} "

class Electronic(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand
    def info(self):
        return f"Название: {self.name}, Цена: {self.__price}, Бренд: {self.brand} "
    
class Clothes(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
    def info(self):
        return f"Название: {self.name}, Цена: {self.__price}, Размер: {self.size}"
    

class Card:
    def __init__(self):
        self.products = []
        self.sale = 0