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
- Go to *Interfacing Options -> I2C -> Enable

Reboot Pi:
```
sudo reboot
```
