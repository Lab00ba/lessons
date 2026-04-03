# class Product: 
#     def __init__(self, name , price):
#         self.name = name 
#         self.price = price
    
#     def info(self):
#         print(f"Название: {self.name}, Цена: {self.price}")


# class Basket:
#     def __init__(self):
#         self.product = []

#     def add_basket(self, product):
#         self.product.append(product)
    
#     def info(self):
#         for i in self.product:
#             print(i)
    
#     def remove_product(self, name_product):
#         for i in self.product:
#             if i.name == name_product:
#                 self.product.remove(i)
#                 print(f"Товар {i.name} удален")
#                 return
#         print("Товар не найден")    

# b1 = Basket()
# p1 = Product("Ноутбук", 200000)
# p2 = Product("Мышка", 40000)

# b1.add_basket(p2)

# b1.remove_product("Мышка")

# p1.info()
# p2.info()




class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages 

    def info(self):
        print(f"Название: {self.name}, Автор: {self.author}, Страницы: {self.pages}")

    def quantity(self):
        if self.pages > 400:
            print("Длинная книга")
        else:
            print("Маленькая книга")

    def description(self):
        return f"Название: {self.name}, Автор: {self.author}"
    

    def read(self, pages_read):
        pages_left = self.pages - pages_read
        print (f"Прочел страниц: {pages_read}, Осталось прочесть: {pages_left}")
    

if __name__ =="__main__":

    b1 = Book("Ром и смерть", "Доктор Лифси", 400)
    b2 = Book("Жанна киска", "Барбоскины", 560)

    # b1.info()
    # b2.info()

    b1.quantity()
    print(b1.description())

    # b2.quantity()
    # print(b2.description())

    b1.read(67)