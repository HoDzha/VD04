from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    now = datetime.now()  # Получаем текущие дату и время
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Форматируем дату и время
    return f"<h1>Текущие дата и время: {formatted_time}</h1>"


if __name__ == '__main__':
    app.run(debug=True)