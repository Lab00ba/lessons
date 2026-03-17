# try:
#     # код где может быть ошибка
# except:
#     # Код слоыит ошибку если она есть
# finally:
#     # код выполняеться в любом случае.

# try:
#     num = int(input("Введите число: "))
#     print(10/num)

# except:
#     print("Произошла ошибка")

# except: #вставить ошибку (Error)
#     print("Деление на ноль запрещено")
# except:
#     print("Произошла ошибка")
# finally:
#     print("Программма выполнена")


# try:
#     x = int("Hello")
# except ValueError as e:
#     print("Ошибка", e)

# while True:
#     try:
#         num = int(input("Введите число: "))
#         break
#     except ValueError:
#         print("Это не число")

# print("ВАше число", num)