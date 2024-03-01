# Django Stripe API Backend (advanced)

Этот проект представляет собой Django + Stripe API бэкенд с функционалом покупки товаров через Stripe.

## Запуск проекта

1. Клонировать репозиторий:
 - git clone https://github.com/KapetanVodichka/Stripe_API.git

2. В директории проекта создать файл .env по шаблону .env.sample и заполнить все пустые переменные

3. Создайте аккаунт на (https://dashboard.stripe.com/test/apikeys) и скопируйте API-ключи в .env

4. Запустите приложение с помощью Docker Compose:
 - docker-compose up --build


Проект будет доступен по адресу "http://localhost:8001/"

При развертывании Docker применяются команды:
 - python manage.py create_test_data
 - python manage.py createsuperuser
.Создается admin-аккаунт login: admin password: admin
.Создаются 2 объекта Item для тестирования
