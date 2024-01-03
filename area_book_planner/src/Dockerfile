FROM python:3.10.12

RUN groupadd -r mygroup && useradd -r -g mygroup myuser

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install uwsgi
RUN chown -R myuser:mygroup /app
RUN chown myuser:mygroup /app/uwsgi.ini && chmod 644 /app/uwsgi.ini


EXPOSE 8000

USER myuser

CMD ["uwsgi", "--ini", "/app/uwsgi.ini"]