from flask import Flask
import psycopg2
import redis
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Retail Inventory API is running!"

@app.route("/health")
def health():
    return {
        "application": "OK",
        "database": check_database(),
        "redis": check_redis()
    }

def check_database():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        conn.close()
        return "OK"
    except Exception as e:
        return "ERROR"

def check_redis():
    try:
        r = redis.Redis(
            host=os.getenv("REDIS_HOST"),
            port=6379
        )
        r.ping()
        return "OK"
    except Exception:
        return "ERROR"

app.run(host="0.0.0.0", port=5000)