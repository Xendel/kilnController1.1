# kiln - Controller1.1
Kiln Controller with MAX31856 included
Includes 4 digit 7 segment display

#####################################

This project is a work in progress. I am still facing issues with Temp readings and troubleshooting.

Board is a Raspberry PI Zero w V1.1 connected to an adafruit MAX31855


#####################################


This is a kilncontroller copy of (https://github.com/jbruce12000/kiln-controller) see reference project build here https://www.instructables.com/Build-a-Web-Enabled-High-Temperature-Kiln-Controll/


Many of these dependancies are listed in the other git projects.


These are just a few that I noticed I needed to make sure I imported or installed for the drivers of MAX31856 to work.


If you are using a Raspberry Pi Zero W, you will need to enable the I2C and SPI interfaces before running the script. You can do this by running the following commands:

sudo raspi-config nonint do_i2c 0

sudo raspi-config nonint do_spi 0


The Adafruit Pi Installer Script is a script that can be used to install CircuitPython on a Raspberry Pi. It is a convenient way to install CircuitPython, as it takes care of all of the necessary steps, such as installing the required dependencies and configuring the Raspberry Pi.


To run the Adafruit Pi Installer Script, simply open a terminal window and navigate to the directory where the script is located. Then, run the following command:

sudo pip install --upgrade adafruit-python-shell

wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py

sudo python raspi-blinka.py
