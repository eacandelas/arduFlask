# arduFlask
Display arduino data using using pyserial and flask

##Setup.

This mainly works on linux but should have not problem on mac.

clone arduFlask project
`$git clone https://github.com/greenoneo0/arduFlask.git`
move to directory
`$cd arduFlask`
install virtualenv
`$sudo apt-get install virtualenv`
create environment
`$virtualenv env`
activate environement
`$source env/bin/activate`
install flask and pyserial on environment
`$pip install pyserial flask`

The environment should be ready.
Now use arduino IDE to load arduFlask.ino to arduino based board (tested on UNO).

Run flask application using
`$python run.py`

App will be running on http://localhost:5000

Enjoy.

ToDo:

Create a page for selecting serial port.
Save port on session.
Handle no port exception.
Handle no data exception.
Handle wrong answer exception.
Add conection sequence to validate there is the correct sketch on the arduino.




