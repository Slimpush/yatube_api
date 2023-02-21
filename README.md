=======
# Описание проекта:

***Проект api_finale_yatube - это API для социальной сети проекта yatube.
С его помощью можно запрашивать информацию о постах, группах, подписках в пределах социальной сети yatube, а так же самому создавать новые посты.***

**Как запустить проект:**

**Клонировать репозиторий и перейти в него командой CD:**

>git clone git@github.com:Slimpush/api_final_yatube.git 

>cd api_final_yatube

**Cоздать и активировать виртуальное окружение:**

>python -m venv venv

>source venv/Scripts/activate

**Установить зависимости из файла requirements.txt:**

>pip install -r requirements.txt

**Выполнить миграции:**

>python manage.py migrate

**Запустить проект:**

>python manage.py runserver

**Примеры запросов**

Авторизированному пользователю необходимо получить токен для полного функционала запросов, для этого нужно сделать POST запрос к эндпоинту /api/v1/jwt/create/ и передать username и password пользователя. При отправке запроса необходимо передать свой токен в заголовок Authorization: Bearer <ваш токен>


get запрос к api/v1/posts/

**Пример ответа:**

>{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}

post запрос к api/v1/posts/

>{
  "text": "string",
  "image": "string",
  "group": 0
}

Пример ответа:

>{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}

Доступные эндпоинты:

>/api/v1/posts/ (GET, POST, PUT, PATCH, DELETE)
/api/v1/posts/{post_id}/comments/ (GET, POST, PUT, PATCH, DELETE)
/api/v1/groups/ (GET)
/api/v1/follow/ (GET, POST)
api/v1/jwt/create/ (POST)

