# NexusBMS
BMS Simulation interfacing with OpenHAB and mosquitto MQTT.

## Requirements
-OpenHAB 3.1 for windows, download [here](https://www.openhab.org/download/).

-Eclipse Mosquitto MQTT message broker, [download](https://mosquitto.org/files/binary/win64/mosquitto-2.0.12-install-windows-x64.exe)

## Set-Up

After installing all required software.

### OpenHAB
1. Navigate to OpenHAB location in terminal and run `start.sh`
2. Open browser and go to ` http://localhost:8080`
3. In this generic MQTT thing navigate to the channels tab.
### To add a utility to a room:
1. Choose a channel identifier and label of your choice. 
2. Choose on/off switch channel type.
3. Set an MQTT state and set topic they can both be same. Currently configured in python script to use the following topic to control a light: `Lighting/Room_<Room Letter>`
4. Set custom on to value 1 and custom off to value 0 and click done in top right.
5. Press add link to item 
![Capture](https://user-images.githubusercontent.com/54277779/133573320-b3c98e7b-f9b3-49ea-acb1-ebe8a955bef9.JPG)
