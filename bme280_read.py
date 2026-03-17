from machine import I2C, Pin
import time
import bme280
# Initialize I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
# Initialize the BMP280 sensor
bme = bme280.BMP280(i2c=i2c)
while True:
temp = bme.temperature # Read temperature
pressure = bme.pressure # Read Pressure
print(f"Temperature: {temp}, Pressure: {pressure}")
time.sleep(2) # Waiting time