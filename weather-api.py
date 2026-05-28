import requests

base_url = "https://api.openweathermap.org/data/2.5/weather"
api_key = "cdcfd44eb7264a5baf177df410df3d0f"

def menu():
    print("----Информация о погоде----")
    print("1. Узнать погоду")
    print("0. Выйти")

def get_weather(city):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "ru"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "wind_speed": data["wind"]["speed"]
        }
    
    except Exception as e:
        print("Ошибка:", e)


def main():
    while True:
        menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            city = input("Напишите название города: ")
            weather = get_weather(city)
            
            print(f'Город: {weather["city"]}')
            print(f'Температура: {weather["temp"]} с')
            print(f'Ощущается как: {weather["feels_like"]} с')
            print(f'Скорость ветра: {weather["wind_speed"]} км/ч')


        elif choice == "0":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()


# weather = {
#         "city": data["name"],
#         "temp": data["main"]["temp"],
#         "feels_like": data["main"]["feels_like"],
#         "wind_speed": data["wind"]["speed"]
#     }