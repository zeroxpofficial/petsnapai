FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY app.py /app/

EXPOSE 5000

CMD ["gunicorn", "app:app", "--reload", "-b", "0.0.0.0:5000"]
