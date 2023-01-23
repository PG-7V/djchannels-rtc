
docker-compose up --build |
войти в контейнер _web docker exec -it <id conteiner> /bin/sh и загрузить фикстуры python manage.py loaddata dump.json |
авторизоваться http://127.0.0.1:8000/admin/ login/pass root |
перейти в чат http://127.0.0.1:8000/posts/chat1/ и отправить сообщение через форму внизу |
