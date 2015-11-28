from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "", 418

if __name__ == "__main__":
    app.run()