import os
import string
from art import *

class nbms:
    def __init__(self):
        self.cmd = {"-l": "Lighting", "-hvac": "HVAC"}
        self.rooms = string.ascii_uppercase[:20]
    def getcmd(self, item):
        try:
            return self.cmd[item]
        except KeyError:
            print("Invalid type ", item)
            return 0

    def getroom(self, id):
        if len(str(id)) == 1 and id.upper() in self.rooms:
            return id.upper()
        else:
            print("Invalid Room ID.", id)
            return 0



if __name__ == "__main__":
    tprint("NBMS")
    print("Welcome to Nexus Building Managment System.")
    n = nbms()
    base_cmd = "mosquitto_pub -t"

    while(1):
        usrin = input(">>>")

        if usrin == "-q":
            print("Exiting...")
            break

        out = list(map(str,usrin.split()))

        if len(out) == 3 and out[2] == '0' or out[2] == '1':

            t1 = n.getcmd(out[0])
            t2 = n.getroom(out[1])
            mqtt = f"{t1}/Room_{t2} '{out[2]}'"
            cmd = f"{base_cmd} {mqtt}"
            
            if t2 != 0:
                print(cmd)
                os.system(cmd)
            

        else:
            print("Invalid command.")
