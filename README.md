# Django Stripe API Backend

Этот проект представляет собой Django + Stripe API бэкенд с функционалом покупки товаров через Stripe.

## Запуск проекта

1. Клонировать репозиторий:
 - git clone https://github.com/KapetanVodichka/Stripe_API.git

2. Создать и активировать виртуальное окружение:
 - python -m venv venv
 - venv\Scripts\activate (Для Windows) или - source venv/bin/activate (Для Linux)

3. Установите необходимые зависимости:
 - pip install -r requirements.txt

4. Создайте БД и установите её настройки (Stripe_API/config/settings (82-85 строки)):
   *(Пример для PostgreSQL)*
 - psql -U your_username
 - CREATE DATABASE your_database_name;

5. Создайте и примените миграции:
 - python manage.py makemigrations
 - python manage.py migrate

6. Зарегистрируйтесь на сайте https://dashboard.stripe.com/test/apikeys, по ссылке https://dashboard.stripe.com/test/apikeys 
скопируйте значения publishable key и secret key в ваш проект по пути Stripe_API/config/settings (131-132 строки).

7. Запустите проект:
 - python manage.py runserver