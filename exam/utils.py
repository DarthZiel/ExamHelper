import requests
import json

# URL API
url = 'http://0.0.0.0:1234/v1/chat/completions'

# Заголовки
headers = {
    'Content-Type': 'application/json',
}

# Данные запроса
data = {
    "model": "llama-3.2-1b-instruct",
    "messages": [
        {"role": "system", "content": "Always answer in rhymes."},
        {"role": "user", "content": "Introduce yourself."}
    ],
    "temperature": 0.7,
    "max_tokens": -1,
    "stream": True
}

# Преобразуем данные в формат JSON
json_data = json.dumps(data)

# Отправляем POST-запрос
response = requests.post(url, headers=headers, data=json_data)

# Печатаем ответ
print(response.json())  # или response.text, если нужно видеть сырой ответ
