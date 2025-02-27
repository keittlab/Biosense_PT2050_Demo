# Biosense_PT2050_Demo
Setup for a quick demo we used for the PT2050 workshop on Feb 27, 2025. This is based on using the Raspberry Pi OS 64-bit Desktop Port provided by the RPI imager utility. 

## Hardware
- Raspberry Pi 4 Model B
- Qwicc PiHat
- Vegetronix LT150 Light sensor
    - 12 Bit ADC - 4 Channel
    - Qwicc connect cable (double ended)
- BME280 Temp/Humidity/Pressure Sensor
- Mouse
- Keyboard
- Screen

*note: this set up only works with a full-size HDMI compatable desktop screen - can't use the 7inch HDMI LCD screens*

## Basic Software Setup
First image the OS onto a SD card for use in a PI model 4. Follow basic set up, set timezone, and connect to wifi or phone hotspot (easiest option). Don't worry about updating the system during the setup screen. Pi should reboot and open to a desktop.

### Enable I2C 
Open Command Line Interface

Run
```
sudo raspi-config
```
- Go to **Interfacing Options -> I2C -> Enable**

Reboot Pi:
```
sudo reboot
```
After reboot make sure i2c connections are functional
```
i2cdetect -y 1
```
you *should* see an output that broadly looks like this:
![image](https://github.com/user-attachments/assets/eb7b5639-66dc-4d5c-a56d-060d3f3edad0)

with a filled value at 48 (*LT150*) and 77 (*BME280*). You can unplug these and run the command again to make sure they are correctly showing up.

### Ensure time is correct - *must be connected to internet*
```
timedatectl
```
Give it a second to load

### Install necessary libraries
```
sudo apt update
sudo apt install -y python3-venv python3-smbus i2c-tools
```

### Create Virtural Environment
```
python3 -m venv pt2050
```
Activate the environment
```
source pt2050/bin/activate
```

Install a few additional libraries via pip
```
pip install adafruit-circuitpython-ads1x15 adafruit-circuitpython-bme280 matplotlib
```

### Running the python sensor scripts
I moved the python scripts to the desktop using a simple usb thumbdrive so they are easier to see for participants not used to interacting with commandline interface.

To run these (*assuming they are sitting on the device's desktop*) make sure you are in the previosly activated virtural environment and run:
```
python Desktop/bme280_logger.py

python Desktop/light_sensor.py
```
The program is a bit finicky to exit to you'll have to **CTRL+C** on the command line and then use the mouse to exit out of the matplotlib screen before you can run the alternate sensor script
