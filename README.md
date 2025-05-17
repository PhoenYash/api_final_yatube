# api_final_yatube

## Описание проекта


## Сборка и установка проекта
Клонирование репозитория
`git clone https://github.com/PhoenYash/api_final_yatube.git`

Создание виртуального окружения
`python -m venv venv`

Активация виртуального окружения
`source venv\Scripts\activate`

Установка зависимостей
`pip install -r requirements.txt`

Обновление версии pip
`python -m pip install --upgrade pip`

Применение миграций
`python manage.py migrate`

Запуск сервера
`python manage.py runserver`

## Примеры запросов
Создание
<pre> POST /api/v1/posts/ 
  { 
    "text":
    "group": 
  }  </pre>
