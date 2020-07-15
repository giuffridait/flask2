import adafruit_dht
import board
from time import sleep
from flask import Flask

app = Flask(__name__)

dhtDevice = adafruit_dht.DHT22(board.D18)
h = dhtDevice.humidity
t = dhtDevice.temperature

@app.route("/")
def index():
        return ('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(t,h))


if __name__ == '__main__':
        app.run()


