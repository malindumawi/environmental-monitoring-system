# environmental-monitoring-system

🌡️ IoT Temperature & Pressure Monitoring System
==================================================

🚀 Project Overview
--------------------------------------------------
This project is a complete IoT-based environmental monitoring system built using the Raspberry Pi Pico W and BME280 sensor. It captures real-time temperature and pressure data, displays it via a web dashboard, and logs it to Google Sheets for cloud-based storage and analysis.

--------------------------------------------------
✨ Key Features
--------------------------------------------------
✔ Real-time sensor data monitoring  
✔ Embedded web server (live dashboard)  
✔ Cloud data logging (Google Sheets)  
✔ Auto Wi-Fi reconnect & error handling  
✔ Lightweight and scalable IoT architecture  

--------------------------------------------------
🛠️ Tech Stack
--------------------------------------------------
Hardware:
- Raspberry Pi Pico W
- BME280 Sensor

Software:
- MicroPython
- Python
- HTML / CSS
- Google Apps Script

--------------------------------------------------
📂 Project Structure
--------------------------------------------------
/project-root
│── bme280_read.py        -> Sensor reading script
│── web_server.py         -> Live dashboard server
│── data_logger.py        -> Cloud logging script
│── apps_script.gs        -> Google Sheets API
│── Malindu_IOT_CW.pdf    -> Report
│── README.txt            -> Documentation

--------------------------------------------------
⚙️ Setup Guide
--------------------------------------------------
1. Hardware Connections:
   SDA -> GP0  
   SCL -> GP1  
   VCC -> 3.3V  
   GND -> GND  

2. Software Setup:
   - Install MicroPython firmware
   - Upload project files to Pico W
   - Configure Wi-Fi credentials

3. Run System:
   - Step 1: Run bme280_read.py (test sensor)
   - Step 2: Run web_server.py (start dashboard)
   - Step 3: Run data_logger.py (enable logging)

--------------------------------------------------
🌐 Web Dashboard
--------------------------------------------------
- Displays temperature (°C) and pressure (hPa)
- Auto-refresh enabled
- Accessible via device IP address

--------------------------------------------------
☁️ Cloud Logging
--------------------------------------------------
- Sends data via HTTP requests
- Stores in Google Sheets
- Includes:
  • Timestamp
  • Temperature
  • Pressure

--------------------------------------------------
🧪 Testing & Validation
--------------------------------------------------
✔ Sensor accuracy verified with external devices  
✔ Real-time web updates confirmed  
✔ Data logging validated with timestamps  
✔ Wi-Fi reconnection implemented for reliability  

--------------------------------------------------
📊 Outcomes
--------------------------------------------------
- Successfully monitored environmental changes
- Enabled trend analysis using collected data
- Demonstrated full IoT pipeline (Device → Web → Cloud)

--------------------------------------------------
🔮 Future Enhancements
--------------------------------------------------
- Add air quality sensors (MQ-135, PMS5003)
- Integrate humidity sensor (DHT22)
- Build advanced analytics dashboard
- Deploy to cloud IoT platforms (AWS IoT, Firebase)

--------------------------------------------------
👤 Author
--------------------------------------------------
Malindu Wijayarathna
BEng(Hons) in Software Engineering

--------------------------------------------------
📄 License
--------------------------------------------------
This project is for academic and educational purposes only.

==================================================
