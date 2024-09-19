#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>

#define ON_Board_LED 2

const char* ssid = "wifi_name";   // Your wifi name
const char* password = "wifi_password"; // Your wifi password

// Flask API endpoint details
const char* apiHost = "<your_host>.pythonanywhere.com"; // Replace with your Flask API host, pythonanywhere is an option
const int apiPort = 443; // HTTPS port

WiFiClientSecure client; // Create a WiFiClientSecure object

// SENSORS (default = 1)
//// Node A
const int D0_Pin = D0;  
const int D1_Pin = D1;
const int D2_Pin = D2;
//// Node B
const int D3_Pin = D3;
const int D4_Pin = D4;
const int D5_Pin = D5;

int node1, node2;
int valueD0,valueD1,valueD2,valueD3,valueD4,valueD5;

void setup() {
  Serial.begin(115200);
  
  WiFi.begin(ssid, password); // Connect to your WiFi router
  Serial.println("");
    
  pinMode(ON_Board_LED,OUTPUT);     // On board LED port as output
  digitalWrite(ON_Board_LED, HIGH); // Turn off Led on board

  // Wait for connection
  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    // Make LED flashing when connecting to the wifi router
    digitalWrite(ON_Board_LED, LOW);
    delay(200);
    digitalWrite(ON_Board_LED, HIGH);
    delay(200);
  }
  // Turn off the LED when it is connected to the wifi router
  digitalWrite(ON_Board_LED, HIGH);
  Serial.println("");
  Serial.print("Successfully connected to: ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.println();

  client.setInsecure(); // For simplicity, not using secure certificates

  // SENSOR setup
  pinMode(D0_Pin, INPUT);
  pinMode(D1_Pin, INPUT);
  pinMode(D2_Pin, INPUT);
  pinMode(D3_Pin, INPUT);
  pinMode(D4_Pin, INPUT);
  pinMode(D5_Pin, INPUT);
}

void loop() {

  valueD0 = digitalRead(D0_Pin);
  valueD1 = digitalRead(D1_Pin);
  valueD2 = digitalRead(D2_Pin);
  valueD3 = digitalRead(D3_Pin);
  valueD4 = digitalRead(D4_Pin);
  valueD5 = digitalRead(D5_Pin);
  delay(50);
  node1 = !valueD0 + !valueD1 * 2 + !valueD2 * 4;
  node2 = !valueD3 + !valueD4 * 2 + !valueD5 * 4;
  
  if(node1 == 5){
    sendData(41,0);
  }
  else if(node2 == 5){
    sendData(40,0);    
  }
  else if (node1 == 2){
    sendData2(41,0);
  }
  else if(node2 == 2){
    sendData2(40,0);
  }



}

// Modified sendData function to send data to Flask API
void sendData(int node_1, int node_2) {
  if (!client.connect(apiHost, apiPort)) {
    Serial.println("Connection to API failed");
    return;
  }

  String postData = "{\"node_1\":" + String(node_1) + ", \"node_2\":" + String(node_2) + "}";
  String request = String("POST ") + "/post_data" + " HTTP/1.1\r\n" +
                   "Host: " + apiHost + "\r\n" +
                   "Content-Type: application/json\r\n" +
                   "Content-Length: " + postData.length() + "\r\n" +
                   "Connection: close\r\n\r\n" + postData;

  client.print(request);
  Serial.println("Data sent to Flask API");
  // delay(500); // Wait for the server response (optional)

  // Read the server's response (optional, for debugging)
  // while(client.available()){
  //   String line = client.readStringUntil('\r');
  //   Serial.print(line);
  // }
  Serial.println("Sent to 1");
}

void sendData2(int node_3, int node_4) {
  if (!client.connect(apiHost, apiPort)) {
    Serial.println("Connection to API failed");
    return;
  }

  String postData = "{\"node_3\":" + String(node_3) + ", \"node_4\":" + String(node_4) + "}";
  String request = String("POST ") + "/post_data2" + " HTTP/1.1\r\n" +
                   "Host: " + apiHost + "\r\n" +
                   "Content-Type: application/json\r\n" +
                   "Content-Length: " + postData.length() + "\r\n" +
                   "Connection: close\r\n\r\n" + postData;

  client.print(request);
  Serial.println("Data sent to Flask API");
  // delay(500); // Wait for the server response (optional)

  // Read the server's response (optional, for debugging)
  // while(client.available()){
  //   String line = client.readStringUntil('\r');
  //   Serial.print(line);
  // }
  Serial.println("Sent to 2");
}
