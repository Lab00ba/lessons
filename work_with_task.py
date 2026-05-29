###############################
# 1 Сохранить и прочитать имя
###############################
# 
# def save_and_read_names():
#     name = input("Как вас зовут?")
#     with open("name.txt", "a" , encoding="UTF-8") as file:
#         file.write(name + "\n")
#     with open("name.txt", "r" , encoding="UTF-8") as file:
#         names = file.readlines()
#     for name in names:
#         print(f"Привет, {name}😠")

# save_and_read_names()


########################
#2 Подсчет строк
########################

# def counting_lines():
#     with open("test.txt", "r" , encoding="UTF-8") as file:
#        words = file.readlines()
#     print(f"В файле {len(words)} строк")

# counting_lines()


#########################
# 3 Подсчет слов
#########################

def word_count():
    with open("test.txt", "r" , encoding="UTF-8") as file:
        words = file.read()
        count = words.split()
    print(f"В файле {len(count)} слов")

word_count()


#######################
#4 Поиск слова из файла
#######################

def Sherlock():
    name = input("Назовите нужный фрукт: ")
    with open("test.txt", "r" , encoding="UTF-8") as file:
        words = file.read().lower()
       
    if name in words:
        print(f"У нас есть {name}!")
    else:
        print("Нет")

# Sherlock()



#5 Нумеровать слова

def numbering():
    with open("test.txt", "r" , encoding="UTF-8") as file:
        words = file.read()
        count = words.split()

    for index, fruits in enumerate(count, start=1):
        print(f"{index}.{fruits}")

numbering()