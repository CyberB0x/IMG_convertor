from crypt import methods

from flask import Flask, request, render_template, send_file
from PIL import Image
import os

app = Flask(__name__)

# Создаем папки для хранения загруженных и ковертированых  фалов
UPLOAD_FOLDER = "uploads"
CONVERTED_FOLDER = "converted"

# Создаем папки, если они не существует
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Получаем файл из формы
        file = request.files.get("image")
        if file:
            #Сохраняем загруженное изображение
            original_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(original_path)

            # Получаем имя файла без расширения
            filename_wo_ext = os.path.splitext(file.filename)[0]
            # Новое имя файла с расширением JPG
            new_filename = filename_wo_ext + ".jpg"
            new_path = os.path.join(CONVERTED_FOLDER, new_filename)

            #Конвертация файла в JPG
            with Image.open(original_path) as img:
                rgb_im = img.convert("RGB")
                rgb_im.save(new_path, format="JPEG")

            # Отправляем пользователю
            return send_file(new_path, as_attachment=True)

        # Отображаем HTML-файл с формой
        return render_template("index.html")


