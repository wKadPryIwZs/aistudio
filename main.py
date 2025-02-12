import google.generativeai as genai
import os

# Установи свой API-ключ как переменную окружения (лучше хранить в .env)
API_KEY = os.getenv("GOOGLE_API_KEY", "Твой API-ключ здесь")  # <-- замени на свой ключ

# Конфигурация клиента
genai.configure(api_key=API_KEY)

# Выбор модели
model = genai.GenerativeModel("gemini-1.5-flash")  # или "gemini-1.5-pro"

# Генерация ответа
response = model.generate_content("Explain how AI works")

# Вывод результата
print(response.text)
