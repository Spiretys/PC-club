# GameZone — Компьютерный клуб

Сайт компьютерного клуба с 5 игровыми станциями.

## Технологии

- **HTML** — шаблон страницы (`templates/index.html`)
- **CSS** — стили (`static/css/style.css`)
- **JavaScript** — форма бронирования, мобильное меню (`static/js/main.js`)
- **Python (Flask)** — сервер и API (`app.py`)

## Запуск

```bash
cd computer-club
pip install -r requirements.txt
python app.py
```

Откройте в браузере: http://127.0.0.1:5000

## Структура

```
computer-club/
├── app.py              # Flask-сервер
├── requirements.txt
├── templates/
│   └── index.html      # Главная страница
└── static/
    ├── css/style.css
    └── js/main.js
```
