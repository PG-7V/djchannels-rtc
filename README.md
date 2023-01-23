## Build images

    $ docker-compose up --build
    
## Войти в контейнер _web
    $ docker ps
    $ docker exec -it <id conteiner> /bin/sh
## Загрузить фикстуры
    $ python manage.py loaddata dump.json
## Авторизоваться
- http://127.0.0.1:8000/admin/ login/pass root
- перейти в чат http://127.0.0.1:8000/posts/chat1/
- отправить сообщение через форму внизу
