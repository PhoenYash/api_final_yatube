# api_final_yatube

## Описание проекта
Представляет из себя соцсеть, в которой пользователи способны регестрироваться, делать/удалять/редактировать публикации, оставлять/удалять/редактировать комментарии и подписываться друг на друга.

## Сборка и установка проекта
Клонирование репозитория
>`git clone https://github.com/PhoenYash/api_final_yatube.git`

Создание виртуального окружения
>`python -m venv venv`

Активация виртуального окружения
>`source venv\Scripts\activate`

Установка зависимостей
>`pip install -r requirements.txt`

Обновление версии pip
>`python -m pip install --upgrade pip`

Применение миграций
>`python manage.py migrate`

Запуск сервера
>`python manage.py runserver`

## Примеры запросов
- Получение публикаций
<pre> GET /api/v1/posts/ 
  { 
    "limit": "5",
    "offset": "1"
  }  </pre>

- Создание публикации
<pre> POST /api/v1/posts/ 
  { 
    "text": "Моя публикация" 
  }  </pre>

- Получение публикации
<pre> GET /api/v1/posts/1/
</pre>

- Добавление комментария
<pre> POST /api/v1/posts/1/comments/
{
  "text": "string"
}</pre>

- Список сообществ
<pre> GET /api/v1/groups/
</pre>
