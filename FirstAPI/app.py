from flask import Flask
import logging as logger
logger.basicConfig(level="DEBUG")

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World, This is from Flask App!"