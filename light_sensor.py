import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import matplotlib.pyplot as plt

# Initialize I2C (Bus 1 for ADS1015)
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
channel = AnalogIn(ads, ADS.P0)  # LT150 connected to A0

timestamps = []
light_readings = []
start_time = time.time()

plt.ion()
fig, ax = plt.subplots()

def update_plot():
    ax.clear()
    ax.set_title("Light Level Over 60 Seconds")
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Light Intensity (Lux)")
    ax.plot(timestamps, light_readings, '-o')
    plt.draw()
    plt.pause(0.1)

try:
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > 60:
            timestamps.pop(0)
            light_readings.pop(0)

        voltage = channel.voltage
        lux = voltage * 1000  # Adjust based on LT150 specs

        timestamps.append(elapsed_time)
        light_readings.append(lux)

        update_plot()
        time.sleep(1)

except KeyboardInterrupt:
    plt.ioff()
    plt.show()
