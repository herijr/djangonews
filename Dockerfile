FROM python:3.11
EXPOSE 8000
WORKDIR /app

COPY requirements.txt /app

RUN python3 -m pip install -r requirements.txt

COPY . /app

EXPOSE 8000

ENTRYPOINT ["python3"]

CMD ["manage.py", "runserver", "0.0.0.0:8000"]