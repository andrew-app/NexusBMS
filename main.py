import sys
from nyamuk import *

def nloop(client):
    client.packet_write()     # flush write buffer (messages sent to MQTT server)
    client.loop()             # fill read buffer   (enqueue received messages)
    return client.pop_event() # return 1st received message (dequeued)
def config():
    client = Nyamuk("Nexus_BMS", port=1883)
    ret = client.connect(version=3)
    ret = nloop(client) # ret should be EventConnack object
    if not isinstance(ret, EventConnack) or ret.ret_code != 0:
        print("Connection Failed")
        exit()
    return client

    

while(1):
    client = config()
    cmd = raw_input(">>")
    cmd = str(cmd).split()

    if "-l" in cmd and len(cmd) == 3:
        topic = "Lighting/Room_"
        if cmd[1].isdigit() is False:
            topic += cmd[1].upper()
            if cmd[2] is '0' or '1':
                client.publish(topic, cmd[2], qos=0)
                print("PUBLISH Sent")
                client.disconnect()
    
    elif "-l" in cmd and len(cmd) == 2:
        topic = "Lighting"  
        if cmd[1] is '0' or '1':
            client.publish(topic, cmd[1], qos=0)
            print("PUBLISH Sent")
            client.disconnect()

    elif "-q" in cmd:
        print("Shutting Down Nexus BMS")
        break
    else:
        print("Invalid")
    
    
    
    
