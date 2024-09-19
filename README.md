## High-Speed Train Wireless Communication System with Environmental Awareness

### Contributors

- [Ozan Can Okay](https://github.com/Romuloyloy) - This project was completed with the joint efforts of the ozan can okay and myself

---

### Project Overview

In the routes of high-speed trains, particularly in challenging geographical areas, there are declines in the performance of cellular communication systems, which can lead to interruptions for passengers on the train. Wireless communication channels can be directly affected by geographical features and the mobility levels of users.

In this project, we have designed a system with high environmental awareness for high-speed trains. The developed system controls specific features of the wireless communication system. The uniqueness of this project lies in the attempt to control the wireless communication system using environmental data.

Given the interdisciplinary nature of the project, a demo was conducted using model trains. Sensors were deployed to detect the nodes where trains pass, and location information was transferred to a computer. Machine learning models were applied to determine the difficulty level of wireless communication in the relevant geography, and to identify whether additional relays are required.

This adaptable, environmentally aware system is visualized through an enhanced interface, allowing us to monitor the need for additional relays and optimize communication performance dynamically.

---

### Installation

Ensure you have the necessary dependencies installed. You can install them using the following command:

```bash
pip install -r requirements.txt
```

---

### File Descriptions

#### model_save.py

**Purpose:** This script trains machine learning models using the processed data and saves the models using the joblib library. This allows the trained models to be reused without needing to retrain them each time.

**Key Functions:**
Model fitting on the prepared dataset.
Saving models to disk for future use.

---

#### interface.py

**Purpose:** This script is developed using the Streamlit library. It provides a real-time interface to monitor the system's performance and adjust parameters on the fly. The interface updates with real-time changes in the wireless communication data, allowing users to monitor the need for additional relays dynamically.

**Key Features:**
Real-time data visualization and monitoring.
User-friendly interface for parameter adjustments and relay requirement insights.

---

#### functions.py

**Purpose:** This file contains essential utility functions needed for the project, such as generating synthetic dataframes, making predictions using the trained machine learning models, and other helper functions required by the interface.py.

**Key Functions:**

- Data generation: Create synthetic datasets that simulate real-world conditions.

- Prediction: Use trained models to predict communication difficulty levels.
  Other utilities for smooth operation of the interface.

---

#### model_selection.ipynb

**Purpose:** This Jupyter Notebook is where data analysis and model performance testing were conducted. The performances of 8 different machine learning models were evaluated on the dataset, and results were compared to select the best model for real-time prediction in the system.

**Key Functions:**
Data analysis and visualization to understand the dataset better.
Testing and comparing the performance of 8 different machine learning models.
Selection of the most appropriate model based on accuracy, F1-score, and other metrics.

---

#### data_to_sheet.ino

**Purpose:** This Arduino/ESP8266 script is responsible for collecting sensor data from various nodes along the train's route and transmitting that data to a Flask-based API. It establishes a secure connection to a Wi-Fi network and periodically sends sensor data (such as the node the train is currently passing through) to a web server for further processing and integration into the system.

**Key Functions:**

- Wi-Fi Connection Setup:
  The script connects to a specified Wi-Fi network using the provided SSID and password.
  On successful connection, the ESP8266 device retrieves and displays its local IP address.

- Sensor Data Collection:
  There are six sensor pins (D0, D1, D2 for Node A and D3, D4, D5 for Node B) used to detect the train's position.
  Based on the sensor inputs, the script determines which node the train is passing and prepares the corresponding data for transmission.

- Data Transmission to Flask API:
  The script uses the WiFiClientSecure library to send collected sensor data to a Flask API hosted on a web server. It constructs an HTTP POST request with JSON data, representing the current node's status.
  There are two functions (sendData and sendData2) to handle data from two different sets of nodes (node1 and node2), sending this information to different Flask API endpoints (/post_data and /post_data2).

- Real-Time Monitoring:
  The real-time data transmitted from the sensors helps update the environmental awareness model in real time, facilitating dynamic adjustment of the wireless communication system's relays.

---

#### flask_app.py

**Purpose:** This Flask-based web server serves as the backend API for receiving, storing, and providing access to sensor data from the ESP8266 devices (nodes) deployed along the train’s route. The application accepts data from two different sets of nodes, stores the latest values in memory, and allows other systems to retrieve the most recent data via HTTP GET requests.
