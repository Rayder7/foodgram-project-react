FROM python:3.7

WORKDIR /app

COPY . ./

RUN apt-get update && apt-get upgrade -y && \
    pip install --upgrade pip && pip install -r requirements.txt

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"]