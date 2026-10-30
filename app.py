import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Falha 1 (Gitleaks): segredo exposto no codigo
API_KEY = "x9Kp2mQ7vL4nR8tZ1wY6cB3dF5hJ0sA"


def soma(a, b):
    return a + b


def get_user(name):
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (name TEXT)")
    conn.execute("INSERT INTO users VALUES ('ana')")
    # Falha 2 (Semgrep/SAST): SQL injection por concatenacao
    return conn.execute(
        "SELECT name FROM users WHERE name = '" + name + "'"
    ).fetchall()


@app.route("/saude")
def saude():
    return "ok"


@app.route("/user")
def user():
    return str(get_user(request.args.get("name", "")))


if __name__ == "__main__":
    app.run()
