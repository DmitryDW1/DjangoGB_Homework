from datetime import datetime
import logging
from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)

def index(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>

        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Мой первый Django-сайт</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
                background: linear-gradient(to bottom,  #cdeb8b 0%,#cdeb8b 100%);
                
            }
            
            h1 {
                color: #333;
            }
            
            p {
                color: #777;

            }
        </style>
    </head>
    <body>
        <h1>Здравствуйте</h1>
    
        <h2>О сайте</h2>
        
        <p>
            Это мой первый сайт, разработанный с помощью Django. Данный сайт является домашней работой по курсу "Фреймворк Django". Буду создавать интернет-магазин.<br> По мере развития проекта будут добавлятся страницы, переработан дизайн.
        </p>
    
        <footer>
        <p>&copy; Все права защищены. 2024</p>
        </footer>
    </body>
    </html>
    """
    logger.info(f'посещение страницы index в: {datetime.now()}')
    return HttpResponse(html)

def about(request):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Обо мне</title>
</head>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
                background: linear-gradient(to bottom,  #cdeb8b 0%,#cdeb8b 100%);
            }
            
            h1 {
                color: #333;
            }
            
            p {
                color: #777;
            }
        </style>
<body>
    <header>
        <h1>Здравствуйте! Меня зовут Дмитрий Деденев</h1>
    </header>

    <main>
        <p>
            Я студент GeekBrains. Учусь профессии "Разработчик". В данный момент прохожу курс специализации "Веб-разработка на Python".
        </p>
        <p>
            Мне 42 года. Образование среднее-специальное. С компьютерной техникой дружу примерно лет с 5))). Начиналось всё с Радио-РК86, затем Spectrum, Profi, потом IBM-486 и так далее.
        </p>
    </main>

    <footer>
        <p>&copy; Все права защищены. 2024</p>
    </footer>
</body>
</html>
"""
    logger.info(f'посещение страницы about в: {datetime.now()}')
    return HttpResponse(html)
