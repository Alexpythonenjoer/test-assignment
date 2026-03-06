import os
import requests
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()


def send_telegram_message(file_path):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    if token:
        token = token.strip().replace("bot", "")

    if not token or not chat_id:
        return "Ошибка: Проверьте TELEGRAM_TOKEN и CHAT_ID в файле .env"

    # 1. Проверка наличия файла
    if not os.path.exists(file_path):
        return f"Ошибка: Файл {file_path} не найден."

    # 2. Чтение текста
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().strip()
    except Exception as e:
        return f"Ошибка при чтении файла: {e}"

    if not text:
        return "Файл пуст, нечего отправлять."

    # 3. Отправка через Bot API
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()  # Вызовет ошибку при плохом HTTP статусе
        return "Сообщение успешно отправлено в Telegram!"
    except requests.exceptions.RequestException as e:
        return f"Ошибка при отправке: {e}"


if __name__ == "__main__":
    # Указываем путь к файлу с текстом
    TEXT_FILE = "message.txt"

    print("Запуск отправки...")
    result = send_telegram_message(TEXT_FILE)
    print(result)
