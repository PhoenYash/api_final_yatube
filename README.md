# api_final_yatube

## Описание проекта
Представляет из себя соцсеть, в которой пользователи способны регестрироваться, делать/удалять/редактировать публикации, оставлять/удалять/редактировать комментарии и подписываться друг на друга.

## Сборка и установка проекта
Клонирование репозитория
<pre>`git clone https://github.com/PhoenYash/api_final_yatube.git`<\pre>

Создание виртуального окружения
<pre>`python -m venv venv`<\pre>

Активация виртуального окружения
<pre>`source venv\Scripts\activate`<\pre>

Установка зависимостей
<pre>`pip install -r requirements.txt`<\pre>

Обновление версии pip
<pre>`python -m pip install --upgrade pip`<\pre>

Применение миграций
<pre>`python manage.py migrate`<\pre>

Запуск сервера
<pre>`python manage.py runserver`<\pre>

## Примеры запросов
Создание
<pre> POST /api/v1/posts/ 
  { 
    "text":
    "group": 
  }  </pre>
