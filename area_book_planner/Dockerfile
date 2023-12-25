FROM python:3.10.12

RUN groupadd -r mygroup && useradd -r -g mygroup myuser

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install uwsgi
RUN chown -R myuser:mygroup /app

EXPOSE 8000

USER myuser

CMD ["uwsgi", "--http", ":8000", "--module", "area_book_planner.wsgi:application", "--master", "--enable-threads"]


