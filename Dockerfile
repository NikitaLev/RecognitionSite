FROM python:3.11

ENV PYTHONBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python","taskmanager/manage.py","runserver","0.0.0.0:8080","--noreload"]
