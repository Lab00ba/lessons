# file = open("test.txt", "r")
# text = file.read()
# print(text)
# file.close()


# Методы работы с файлами (Режими открытия)
# "r" - чтение файла
# "w" - запись (очищает файл)
# "a" - добавляет в конец 
# "x" - создает новый файл
# "b" - бинарный режим
# "t" - текстовый режим

# file = open("test.txt", "w", encoding="UTF-8")
# file.write("Привет мир!")
# file.close()

# file = open("test.txt", "a", encoding="UTF-8")
# file.write("\nqweqreqw")
# file.close()

# with open("test.txt", "r", encoding="UTF-8") as file:
#     text = file.read()
#     print(text)

# list = [1, 2, 3, 4, 5]
# with open("test.txt", "w") as file:
#     for num in list:
#         file.write(str(num) + "\n")

# with open("test.txt", "r") as file:
#     numbers = file.readlines()
    
#     print(numbers[2])


import json

# .dump(Отправить данные)
# .load(Показать данные)

user = {
    "name":"Alex",
    "age":19,
    "gender":"M"
}

with open("user.json", "w") as file:
    json.dump(user,file)

with open("user.json", "r") as file:
    data = json.load(file)
print(data)