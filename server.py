from flask import Flask, request, jsonify
from pymongo import MongoClient
import lib.gpio.RPi.GPIO as GPIO
import time

# Flask App
app = Flask(__name__)

# GPIO Pins
LED_PIN = 12

@app.route("/", methods=["GET"])
def root():
    return "", 418

@app.route("/on", methods=["GET", "POST"])
def on():
    on = is_on()

    if request.method == "POST":
        return "", 200
    else:
        return jsonify(state=on), 200

def is_on():
    GPIO.setup(LED_PIN, GPIO.IN)

    timeout = time.time() + 4
    while time.time() <= timeout:
        if GPIO.input(LED_PIN):
            return True

    return False

if __name__ == "__main__":
    app.run()