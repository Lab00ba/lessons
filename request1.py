import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/1"


response = requests.get(url)
data = response.json()

print(f'title: {data["title"]}')
print(f'body: {data["body"]}')

# print(json.dumps(response.json(), indent=4))

# for post in response.json()[:10]:
#     print(json.dumps(post, indent=4))

# print(response.status_code)

# if response.status_code == 200:
#     print("Все успешно")
# else:
#     print("Ошибка!")


# title = input("Напишите заголовок: ")
# body = input("Придумайте основной текст: ")

# data = {
#     "userId": 1,
#     "title": title,
#     "body": body
# }

# response = requests.post(url, data=json)

# print(response.json())
