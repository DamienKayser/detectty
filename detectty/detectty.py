#!/usr/bin/env python3

import os
import time
from serial.tools import list_ports

def getCurrentDevices():
    return list_ports.comports()

def detect():
    print("Waiting for device to be plugged in ...", end="", flush=True)
    devBefore = getCurrentDevices()
    while(True):
        time.sleep(0.5)
        print(".", end="", flush=True)
        devAfter = getCurrentDevices()
        diff = [dev.device for dev in devAfter if dev not in devBefore]
        if len(diff) > 0:
            newDev = diff[0]
            print("\n")
            print("Detected new device:")
            print(newDev)
            return newDev

if __name__ == "__main__":
    detect()