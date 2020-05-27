#!/usr/bin/env python3

import os
import time
from serial.tools import list_ports

def getCurrentDevices(filterDict=None):
    """
    Returns a (filtered) list of currently connected serial devices.
    :param filterDict: The filter to apply
    :type filterDict:  dict
    """
    devices = list_ports.comports()
    if filterDict is not None:
        def filterByDict(dev):
            for key in filterDict:
                if getattr(dev, str(key)) != filterDict[key]:
                    return False
            return True
        return list(filter(filterByDict, devices))
    return devices

def detect(filterDict=None, timeout=None):
    """
    - If timeout is None: Wait for new device forever
    - If timeout is set:
        - Wait accordingly for new device
        - If no new device found, filter current ones by filterDict, return first match
    """
    print("Waiting for device to be plugged in ...", end="", flush=True)
    devBefore = getCurrentDevices()
    while(True):
        time.sleep(0.5)
        print(".", end="", flush=True)
        devAfter = getCurrentDevices()

        # If new device is detected - go for it!
        diff = [dev.device for dev in devAfter if dev not in devBefore]
        if len(diff) > 0:
            newDev = diff[0]
            print("\n")
            print("Detected new device:")
            print(newDev)
            return newDev

        # If timeout is set: check devices by filter, if no new device was detected
        # If timeout is not set: wait for new device infinitely
        if timeout is not None:
            if timeout > 0:
                timeout -= .5
                continue

            if filterDict is None:
                # Pretty pointless ;-)
                return None
            return getCurrentDevices(filterDict=filterDict)[0]

if __name__ == "__main__":
    detect()