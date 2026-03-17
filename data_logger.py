import network
import urequests
import time
from machine import Pin, I2C
from bme280 import BMP280


# Setting up WIFI credentials
ssid = "malindu"
password = "malindu123"


# Web App URL for the Google sheet
SCRIPT_URL = "https://script.google.com/macros/s/AKfycbz-istKUmV62nXh8Y6eofC1GSIrHq3bHgEziP-Stg_lageGwpRc8UpaLp1q90yS0aYK/exec"


# Setting up the I2C for BMP280
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
bmp = BMP280(i2c=i2c)


# Connecting to the WIFI
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
print("waiting for the connection...")
while not wlan.isconnected():
    time.sleep(1)
    print("Connected Successfully! IP Address:", wlan.ifconfig()[0])
    def send_to_sheets(temp, pressure):
    """ Sending sensor readings to Google Sheet """
try:
    url = f"{SCRIPT_URL}?temp={temp}&pressure={pressure}"
    response = urequests.get(url)
    print("Response:", response.text)
    response.close()
except Exception as e:
    print("Error sending data:", e)
    
    
# Looping of reading and sending data
while True:
    temp = round(bmp.temperature, 2) # Reading the temperature and rounding off for 2 decimals
    pressure = round(bmp.pressure, 2) # Reading the pressure and rounding off for 2 decimals
    send_to_sheets(temp, pressure)
    print(f"Logged: {temp} °C, {pressure} hPa")
    time.sleep(10) # Waiting for 10 seconds