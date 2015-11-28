from flask import Flask, request, jsonify
from pymongo import MongoClient
import lib.gpio.RPi.GPIO as GPIO
import time

# Flask App
app = Flask(__name__)

# GPIO Pins
ON_OFF_PIN = 11
LED_PIN = 12

@app.route("/", methods=["GET"])
def root():
    return "", 418

@app.route("/on", methods=["GET", "POST"])
def on():
    on = is_on()

    if request.method == "POST":
        if on:
            return "", 409
        else:
            GPIO.setup(ON_OFF_PIN, GPIO.OUT)
            GPIO.output(ON_OFF_PIN, True)
            GPIO.output(ON_OFF_PIN, False)

            return "", 204
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