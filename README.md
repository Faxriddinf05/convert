WebP to JPEG Converter API
API для конвертации изображений WebP в JPEG и изменения их размера. Поддерживает пять операций:

Конвертация отдельных WebP файлов в JPEG (без изменения размера).
Конвертация WebP файлов из ZIP-архива в JPEG (без изменения размера).
Конвертация отдельных WebP файлов в JPEG с изменением размера до 1080x1440.
Конвертация WebP файлов из ZIP-архива в JPEG с изменением размера до 1080x1440.
Изменение размера JPEG файлов до 1080x1440 (поддерживает отдельные файлы или ZIP).

Требования

Python 3.8+
Git
Зависимости из requirements.txt:
fastapi==0.115.0
uvicorn==0.30.6
pillow==10.4.0



Установка

Клонируйте репозиторий:git clone https://github.com/Faxriddinf05/convert.git
cd convert



Создайте и активируйте виртуальное окружение:python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows


Установите зависимости:pip install -r requirements.txt


Запустите API:uvicorn main4:app --host 0.0.0.0 --port 8000



Использование
После запуска API откройте http://localhost:8000/docs в браузере, чтобы использовать Swagger UI для тестирования эндпоинтов.
Эндпоинты

POST /convert-webp/Конвертирует отдельные WebP файлы в JPEG (оригинальный размер).  

Вход: Один или несколько .webp файлов.  
Выход: ZIP-архив (converted_images.zip) с JPEG файлами.  
Пример:curl -X POST "http://localhost:8000/convert-webp/" -F "files=@image1.webp" -F "files=@image2.webp" -o converted_images.zip




POST /convert-zip/Конвертирует WebP файлы из ZIP-архива в JPEG (оригинальный размер).  

Вход: Один .zip файл, содержащий .webp файлы.  
Выход: ZIP-архив (converted_images.zip) с JPEG файлами.  
Пример:curl -X POST "http://localhost:8000/convert-zip/" -F "file=@images.zip" -o converted_images.zip




POST /convert-webp-resize/Конвертирует отдельные WebP файлы в JPEG с изменением размера до 1080x1440 (с сохранением пропорций и белым фоном).  

Вход: Один или несколько .webp файлов.  
Выход: ZIP-архив (converted_images.zip) с JPEG файлами.  
Пример:curl -X POST "http://localhost:8000/convert-webp-resize/" -F "files=@image1.webp" -F "files=@image2.webp" -o converted_images.zip




POST /convert-zip-resize/Конвертирует WebP файлы из ZIP-архива в JPEG с изменением размера до 1080x1440.  

Вход: Один .zip файл, содержащий .webp файлы.  
Выход: ZIP-архив (converted_images.zip) с JPEG файлами.  
Пример:curl -X POST "http://localhost:8000/convert-zip-resize/" -F "file=@images.zip" -o converted_images.zip




POST /resize-jpeg/Изменяет размер JPEG файлов до 1080x1440 (поддерживает отдельные файлы или ZIP).  

Вход: Один или несколько .jpg/.jpeg файлов или один .zip с JPEG.  
Выход: ZIP-архив (resized_images.zip) с JPEG файлами.  
Пример:curl -X POST "http://localhost:8000/resize-jpeg/" -F "files=@image1.jpg" -F "files=@image2.jpg" -o resized_images.zip





Тестирование

Запустите API:uvicorn main:app --host 0.0.0.0 --port 8000


Откройте http://localhost:8000/docs в браузере.
Используйте Swagger UI для загрузки .webp, .jpg или .zip файлов и проверки результатов.
Проверьте скачанные ZIP-архивы:
Для /convert-webp/ и /convert-zip/: JPEG файлы сохраняют оригинальный размер.
Для /convert-webp-resize/, /convert-zip-resize/ и /resize-jpeg/: JPEG файлы имеют размер 1080x1440.



Примечания

Изменение размера сохраняет пропорции изображения, добавляя белый фон, если нужно.
Качество JPEG установлено на 95.
Для использования с фронтендом добавьте CORS в app.py:from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
