class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            raise ValueError("цена не может быть отрицательной!!!")
    def info(self):
        return f"Название: {self.name}, Цена: {self._price} "

class Electronic(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand
    def info(self):
        return f"Название: {self.name}, Цена: {self._price}, Бренд: {self.brand} "
    
class Clothes(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
    def info(self):
        return f"Название: {self.name}, Цена: {self._price}, Размер: {self.size}"
    

class Card:
    def __init__(self):
        self.products = []
        self.sale = 0

    def add(self,product):
        self.products.append(product)

    def delattr(self, product_name):
        for product in self.products:
            if product_name.lower() == product.name.lower():
                self.products.remove(product)
            else:
                print("Товар не найден")

    def discount(self,percent):
        if percent >= 0 and percent <= 100:
            self.sale = percent
        else:
            raise ValueError("Скидка должна быть в диапозоне от 0 до 100")
        
    def cost(self):
        count = 0
        for product in self.products:
           count += product.price 

        return count*(1-self.sale/100)
    
    def show(self):
        for product in self.products:
            print(product.info())
        print(f"Скидка в процентах.{self.sale}")
        print(f"Общая стоимость {self.cost()}")

e1 = Electronic("Телефон", 400000 , "Apple")
c1 = Clothes("Свитшот", 30000, "L")

card = Card()
card.add(e1)
card.add(c1)

card.show()
card.delattr("Телефон")
card.show()