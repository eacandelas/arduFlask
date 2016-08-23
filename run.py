from flask import Flask
import serial
import time

arduino = serial.Serial('/dev/ttyACM0') 

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
	arduino.write('a')
	time.sleep(1)
	c = arduino.readline()
	print c
    except:
	print 'falla en serial'

    str = "Para el buen @gerghas <br> <br> valor: " + c

    return str

if __name__ == '__main__':
   app.run()
