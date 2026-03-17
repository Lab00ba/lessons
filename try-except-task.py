def menu():
    print("1.Снять деньги")
    print("2.Пополнить боланс")
    print("3.Проверить баланс")
    print("4.Выйти")

def take_money(money):
    try:
        amount = int(input("Сумма снятия: "))
        if amount < 0 :
            print("Сумма снятия не может быть меньше 0")
        elif money < amount :
            print("Недостаточно средст.")
        else:
            operations = int(input("Введите количество операций: "))
            comishns = amount / operations 
            money -= amount
            print(f"Снято {amount}")
            print(f"Комиссия {comishns}")





def main():
    money = 10_000
    while True:
        menu()
        try:
            num = int(input("Введите число из списка: "))
            if num == 1:
                /
            elif num == 2:
                /
            elif num == 3:
                /
            elif num == 4:
                print("Вы вышли из программы.")
                break
            else:
                print("Такой цыфры нет.")
        except ValueError:
            print("Введите число!")

if __name__ == "__main__":
    main()