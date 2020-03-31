#!/usr/bin/env python3

import os
import time

def getCurrentDevices():
    return ["/dev/" + dev for dev in os.listdir("/dev") if "tty" in dev]

def detect():
    print("Waiting for tty devices to be plugged in ...", end="", flush=True)
    devBefore = getCurrentDevices()
    while(True):
        time.sleep(0.5)
        print(".", end="", flush=True)
        devAfter = getCurrentDevices()
        diff = [dev for dev in devAfter if dev not in devBefore]
        if len(diff) > 0:
            newDev = diff[0]
            print("\n")
            print("Detected new device:")
            print(newDev)
            return newDev

if __name__ == "__main__":
    detect()