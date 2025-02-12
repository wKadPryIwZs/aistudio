import google.generativeai as genai
import os

instruction = "инструкция: вы глупый мальчик"

ai_history_memory = []
my_history_memory = []

# Установи свой API-ключ как переменную окружения (лучше хранить в .env)
API_KEY = os.getenv("GOOGLE_API_KEY", "AIzaSyCFrJnrjtiRy189rXljAx680iEBTstfF-Y")  # <-- замени на свой ключ

# Конфигурация клиента
genai.configure(api_key=API_KEY)

# Выбор модели
model = genai.GenerativeModel("gemini-2.0-pro-exp-02-05")  # или "gemini-1.5-pro"

while True:
    # Генерация ответа
    myAnswear = input()
    my_history_memory.append(myAnswear)

    try:
        response = model.generate_content(instruction + str(ai_history_memory) + str(my_history_memory))
    except:
        break
    ai_history_memory.append(response)
    # Вывод результата
    print(response.text)
