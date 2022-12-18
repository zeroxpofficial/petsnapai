from flask import Flask
import psycopg2
import os


DB_HOST = 'db' # this will be the name of the service in the docker-compose file
DB_NAME = os.environ["POSTGRES_DB"]
DB_USER = os.environ["POSTGRES_USER"]
DB_PASSWORD = os.environ["POSTGRES_PASSWORD"]

# app = Flask(__name__)
# app.config["SERVER_NAME"] = "localhost"
# app.config["APPLICATION_ROOT"] = "/app"
# app.config["X_FORWARDED_PROTO"] = "https"
# app.config["X_FORWARDED_FOR"] = True


def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"


if __name__ == '__main__':
    app.run()
