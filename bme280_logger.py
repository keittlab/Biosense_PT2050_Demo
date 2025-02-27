import time
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280
import matplotlib.pyplot as plt

#use default I2C bus (i2c-1)
i2c = board.I2C()

# Initialize BME280 on second I2C bus (adjust if needed)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

bme280.sea_level_pressure = 1019

timestamps = []
temperature_readings = []
humidity_readings = []
pressure_readings = []
start_time = time.time()

plt.ion()
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 8))

def update_plot():
    ax1.clear()
    ax2.clear()
    ax3.clear()
    
    ax1.set_title("Temperature Over 60 Seconds")
    ax1.set_xlabel("Time (seconds)")
    ax1.set_ylabel("Temperature (°C)")
    ax1.plot(timestamps, temperature_readings, '-o', color='red')

    ax2.set_title("Humidity Over 60 Seconds")
    ax2.set_xlabel("Time (seconds)")
    ax2.set_ylabel("Humidity (%)")
    ax2.plot(timestamps, humidity_readings, '-o', color='blue')

    ax3.set_title("Pressure Over 60 Seconds")
    ax3.set_xlabel("Time (seconds)")
    ax3.set_ylabel("Pressure (hPa)")
    ax3.plot(timestamps, pressure_readings, '-o', color='green')

    plt.tight_layout()
    plt.draw()
    plt.pause(0.1)

try:
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > 60:
            timestamps.pop(0)
            temperature_readings.pop(0)
            humidity_readings.pop(0)
            pressure_readings.pop(0)

        temperature = bme280.temperature
        humidity = bme280.relative_humidity
        pressure = bme280.pressure

        timestamps.append(elapsed_time)
        temperature_readings.append(temperature)
        humidity_readings.append(humidity)
        pressure_readings.append(pressure)

        update_plot()
        time.sleep(1)

except KeyboardInterrupt:
    plt.ioff()
    plt.show()
