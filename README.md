##### 1. Клонировать репозиторий
`git clone https://github.com/Mornyi/blog_for_cook.git`
##### 2. Перейти в репозиторий и создать виртуалку
`cd blog_for_cook`
`python -m venv venv`
##### 3. Запустить виртуалку
`source venv/Script/Activate`
##### 4. Установить зависимости 
`pip install -r requirements.txt`
##### 5. Выполнить миграции
`python manage.py migrate`
##### 6. Создать админку
`python manage.py createsuperuser`
##### 7. Запустить сервер 
`python manage.py runserver`

