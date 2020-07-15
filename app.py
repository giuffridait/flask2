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
	for i in range(10):
		try:
			h = dhtDevice.humidity
			t = dhtDevice.temperature
			result = ('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(t,h))
		except RuntimeError:
			result = ('no bananas for you!')
	return result

if __name__ == '__main__':
        app.run()


