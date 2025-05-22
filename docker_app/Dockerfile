
# Указываем базовый образ
FROM kuchaser/myapp:latest
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONPATH=/app
ENV MY_SERVER="http://kuchukov-s.ru/"

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app
COPY ./.env ./backend/.env
RUN cd ./backend/config
RUN sed -i 's/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = \["${{ MY_SERVER }}"\]/1' settings.py 
RUN cd ../

# Копируем файл с зависимостями и устанавливаем их
RUN pip install poetry
RUN cd ./backend/
RUN poetry install --no-root

RUN mkdir /static  && chown -R /static

RUN cd ../
# COPY . .


COPY ./backend/docker/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./backend/docker/celery/worker/start /start_celeryworker
RUN sed -i 's/\r$//g' /start_celeryworker
RUN chmod +x /start_celeryworker

COPY ./backend/docker/celery/beat/start /start_celerybeat
RUN sed -i 's/\r$//g' /start_celerybeat
RUN chmod +x /start_celerybeat 

EXPOSE 8000
# ENTRYPOINT ["/start"]
#CMD ["/start"]