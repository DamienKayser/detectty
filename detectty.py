#!/usr/bin/env python3

import os
import time

def getCurrentDevices():
    return ["/dev/" + dev for dev in os.listdir("/dev") if "tty" in dev]

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
        print("")
        print("Setting environment variable:")
        os.environ["NEW_TTY_DEV"] = newDev
        print("NEW_TTY_DEV='{0}'".format(os.environ["NEW_TTY_DEV"]))
        exit(0)
