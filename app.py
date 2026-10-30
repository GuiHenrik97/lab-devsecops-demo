import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Segredo lido do ambiente, nao escrito no codigo
API_KEY = os.environ.get("API_KEY")


def soma(a, b):
    return a + b


def get_user(name):
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (name TEXT)")
    conn.execute("INSERT INTO users VALUES ('ana')")
    # Consulta parametrizada: a entrada nunca vira comando SQL
    return conn.execute(
        "SELECT name FROM users WHERE name = ?", (name,)
    ).fetchall()


@app.route("/saude")
def saude():
    return "ok"


@app.route("/user")
def user():
    return str(get_user(request.args.get("name", "")))


if __name__ == "__main__":
    app.run()
