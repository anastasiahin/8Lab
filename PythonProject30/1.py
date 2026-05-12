import requests
import random

# Генерація випадкового ID від 1 до 100
post_id = random.randint(1, 100)

# Динамічний URL API
url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

# GET-запит
response = requests.get(url)

# Парсинг JSON в об'єкт
post = response.json()

# Вивід даних
print("ID:", post["id"])
print("TITLE:", post["title"])
print("BODY:", post["body"])