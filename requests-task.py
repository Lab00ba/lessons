import requests
import json
 
url  = "https://jsonplaceholder.typicode.com/posts"

def menu():
    print("1. получение одного поста")
    print("2. получение списка постов")
    print("3. создание поста")
    print("4. Выйти из программы")

def get_post(post_id: int):
    response = requests.get(f"{url}/{post_id}")
    if response.status_code == 200:
        print(response.json())
    else:
        print("Пост не найден")

def all_posts():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for i in data:
            print(f'title: {i["title"]}')
    else:
        print("Посты не найдены!!!!")

def create_post():
    title = input("Заголовок поста: ")
    body = input("Напишите содержимое текста: ")
    data = {
    "userId": 1,
    "title": title,
    "body": body
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(f"Пост отправлен {response.json()}")
    else:
        print("Ошибка созданиия поста!!")

def main():
    while True:
        menu()
        info = input("Веддите номер действия: ")
        if info == "1":
            post_id = int(input("Какой номер поста вы хотите: "))
            get_post(post_id)
        elif info == "2":
            all_posts()
        elif info == "3":
            create_post()
        elif info == "4":
            break
        else:
            print("Такой цыфры нет , попробуйте ещё раз:)")

if __name__ == "__main__":
    main()