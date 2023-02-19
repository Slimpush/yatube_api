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
