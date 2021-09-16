# NexusBMS
BMS Simulation interfacing with OpenHAB and mosquitto MQTT.

## Requirements
-OpenHAB 3.1 for windows, download [here](https://www.openhab.org/download/).

-Eclipse Mosquitto MQTT message broker, [download](https://mosquitto.org/files/binary/win64/mosquitto-2.0.12-install-windows-x64.exe)

-Python 2.7

-Nyamuk MQTT client library for python download from source [here](https://github.com/iwanbk/nyamuk)

## Set-Up

After installing all required software.

### OpenHAB
1. Navigate to OpenHAB location in terminal and run `start.bat`
2. Open browser and go to ` http://localhost:8080`
3. Create a local username and password.
4. Navigate to Settings >> Things and press + icon in bottom right of screen. 
5. Add the MQTT Binding to OpenHAB.
6. Add the MQTT Broker thing.
7. Set the Broker hostname to `localhost`
8. Create new generic MQTT thing and bridge with MQTT broker. 
9. In this generic MQTT thing navigate to the channels tab.
### To add a light for a room:
10. Choose a channel identifier and label of your choice. 
11. Choose on/off switch channel type.
12. Set an MQTT state and set topic they can both be same. Currently configured in python script to use the following topic to control a light: `Lighting/Room_A`
13. Set custom on to value 1 and custom off to value 0 and click done in top right.
14. Press add link to item 
![Capture](https://user-images.githubusercontent.com/54277779/133573320-b3c98e7b-f9b3-49ea-acb1-ebe8a955bef9.JPG)
