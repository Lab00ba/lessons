class Product: 
    def __init__(self, name , price):
        self.name = name 
        self.price = price
    
    def info(self):
        print(f"Название: {self.name}, Цена: {self.price}")


class Basket:
    def __init__(self):
        self.product = []

    def add_basket(self, product):
        self.product.append(product)
    
    def info(self):
        for i in self.product:
            print(i)

b1 = Basket()
p1 = Product("Ноутбук", 200000)
p2 = Product("Мышка", 40000)

b1.add_basket(p2)

p1.info()
p2.info()