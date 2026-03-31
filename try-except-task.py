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
    except ValueError:
        print("Некоректный ввод")
    except ZeroDivisionError:
        print("На 0 делить нельзя")

def add_money(money):
    try:
        amount = int(input("Сумма пополнения: "))
        if amount < 0:
            print("Сумма пополнения не может быть отрицательной")
        else:
             money += amount
             print(f"Ваш счет равен {money}")
             return money
    except ValueError:
        print("Некоректный ввод")

def check_money(money):
    print(f"Ваш баланс: {money}")

def main():
    money = 10_000
    while True:
        menu()
        try:
            num = int(input("Введите число из списка: "))
            if num == 1:
                money = take_money(money)
            elif num == 2:
                money = add_money(money)
            elif num == 3:
                check_money(money)
            elif num == 4:
                print("Вы вышли из программы.")
                break
            else:
                print("Такой цыфры нет.")
        except ValueError:
            print("Введите число!")

if __name__ == "__main__":
    main()