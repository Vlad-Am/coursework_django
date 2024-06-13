 # Веб-сервис по управлению рассылками 


## Usage

Перед запуском web-приложения создайте базу данных, создайте и примените миграции,
установите необходимые пакеты из файла 

#### pip install requirements.txt

и заполните файл .env.sample переименовав до .env
Используйте команду 

Для загрузки данных используйте команду 
#### python manage.py loaddata db_blog.json 
#### python manage.py loaddata db_mail.json 
#### python manage.py loaddata db_users.json 

и
Для запуска сервера 
#### python manage.py runserver 
