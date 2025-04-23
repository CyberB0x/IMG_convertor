# 🖼️ Image to JPG Converter

Простой веб-сервис для конвертации изображений в формат JPG.  
Построен на Flask, с использованием Docker и Nginx.

---

## 🚀 Возможности

- Загрузка изображений через веб-интерфейс
- Автоматическая конвертация в формат `.jpg`
- Возврат готового файла пользователю
- Обёртка через Docker и проксирование через Nginx

---

## 📂 Структура проекта

```plaintext
IMG_convertor/
├── app/
│   ├── app.py                 # Flask-приложение
│   ├── templates/
│   │   └── index.html         # HTML-форма
│   ├── static/
│   │   └── style.css          # Стили для страницы
├── nginx/
│   └── default.conf           # Конфигурация Nginx
├── Dockerfile                 # Сборка backend-контейнера
├── docker-compose.yml         # Запуск через Docker Compose
├── requirements.txt           # Python-зависимости
└── uploads/                   ← создаются автоматически
└── converted/                 ← создаются автоматически
```

---

## ⚙️ Установка и запуск

Убедитесь, что у вас установлен Docker и Docker Compose.

### Шаги:

1. Клонируйте репозиторий:

```bash
git clone https://github.com/CyberB0x/IMG_convertor.git
cd IMG_convertor
```

2. Постройте и запустите контейнеры:

```bash
docker-compose up --build
```

3. Перейдите в браузере:

```
http://localhost
```

---

## 🌐 Интерфейс

Интерфейс очень простой:

1. Загрузите любое изображение (`.png`, `.webp`, `.bmp`, и т.д.)
2. Нажмите "Convert"
3. Получите JPG-файл

---

## 🛠️ Используемые технологии

- [Python 3.10](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Pillow](https://python-pillow.org/)
- [Docker](https://www.docker.com/)
- [Nginx](https://nginx.org/)

---

## 📌 Примечания

- Папки `uploads/` и `converted/` создаются автоматически.
- Проект можно дополнить функцией удаления временных файлов или логированием.

---

## 📄 Лицензия

MIT © 2025 — [Arslonbek Erkinov (CyberB0x)](https://github.com/CyberB0x)
