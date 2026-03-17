import network
import socket
import time
from machine import Pin, I2C
from bme280 import BMP280


# Setting up WIFI credentials
ssid = "malindu"
password = "malindu123"


# Setting up the I2C for BMP280
i2c = I2C(0, scl=Pin(1), sda=Pin(0)) # I2C pins
bmp = BMP280(i2c=i2c) # Initializing BMP280


# Connecting to the to WIFI
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
print("waiting for the connection...")
while not wlan.isconnected():
    time.sleep(1)
    print("Connected Successfully! IP Address:", wlan.ifconfig()[0])


# Web page script in HTML
def webpage(temp, pressure):
html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="refresh" content="5">
        <title>IoT Project - Malindu</title>
        <style>
        
        body {{
            font-family: 'Arial', sans-serif;
            text-align: center;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: white;
            margin: 0;
            padding: 0;
        }}
        
        .container {{
            max-width: 450px;
            margin: 50px auto;
            padding: 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }}
        
        h1 {{
            font-size: 24px;
            margin-bottom: 10px;
        }}
        
        .sensor-box {{
            font-size: 26px;
            margin: 20px 0;
            padding: 15px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(255,255,255,0.2);
            font-weight: bold;
        }}
        
        .footer {{
            font-size: 14px;
            margin-top: 15px;
            opacity: 0.8;
        }}
        </style>
    </head>
    <body>
        <div class="container">
        <h1>Malindu - 20200646</h1>
        <div class="sensor-box">Temperature: {temp} °C</div>
        <div class="sensor-box">Pressure: {pressure} hPa</div>
        </div>
    </body>
    </html>
    """
return html


# Starting the Web Server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(5)
print("The web server is running...")
while True:
    try:
    conn, addr = s.accept()
    print("Client is connected from", addr)
    request = conn.recv(1024)
# Reading the sensor data
    temp = bmp.temperature
    pressure = bmp.pressure
# Sending HTTP Responses
    response = webpage(temp, pressure)
    conn.send("HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n" + response)
    conn.close()
except Exception as e:
    print("Error:", e)
    conn.close()