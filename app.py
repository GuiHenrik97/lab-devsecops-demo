from flask import Flask

app = Flask(__name__)


def soma(a, b):
    return a + b


@app.route("/saude")
def saude():
    return "ok"


if __name__ == "__main__":
    app.run()
