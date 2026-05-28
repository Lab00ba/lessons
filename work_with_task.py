def save_and_read_names():
    name = input("Как вас зовут?")
    with open("name.txt", "a" , encoding="UTF-8") as file:
        file.write(name + "\n")
    with open("name.txt", "r" , encoding="UTF-8") as file:
        names = file.readlines()
    for name in names:
        print(f"Привет, {name}😠")

save_and_read_names()