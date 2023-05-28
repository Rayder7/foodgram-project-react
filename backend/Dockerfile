FROM python:3.7

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"]