#!/usr/bin/env python3

import os
import time
from serial.tools import list_ports

def _filterDevices(devices, filterDict):
    def filterByDict(dev):
        for key in filterDict:
            if getattr(dev, key) != filterDict[key]:
                return False
        return True
    return list(filter(filterByDict, devices))

def getCurrentDevices(filterDict=None):
    """
    Returns a (filtered) list of currently connected serial devices.
    :param filterDict: The filter to apply
    :type filterDict:  dict
    """
    devices = list_ports.comports()
    if filterDict is not None:
        return _filterDevices(devices, filterDict)
    return devices

def detect(filterDict=None, timeout=None):
    """
    Detects new serial devices.
    :param filterDict: The filter to apply
    :type filterDict:  dict
    :param timeout: The timeout value (in seconds)
    :type timeout:  float
    """
    print("Waiting for device to be plugged in ...", end="", flush=True)
    devBefore = getCurrentDevices()
    while(True):
        time.sleep(0.5)
        print(".", end="", flush=True)
        devAfter = getCurrentDevices()

        # If new device is detected - go for it!
        diff = [dev for dev in devAfter if dev not in devBefore]
        if len(diff) > 0:
            newDev = diff[0]
            print("\n")
            print("Detected new device:")
            print(newDev)
            if filterDict is None:
                return newDev.device
            else:
                filteredDevices = _filterDevices([newDev], filterDict)
                if len(filteredDevices) > 0:
                    return filteredDevices[0].device
                else:
                    devBefore = devAfter
                    # Not the device we are looking for. Continue ...
                    continue

        # If timeout is set: check devices by filter, if no new device was detected
        # If timeout is not set: wait for new device infinitely
        if timeout is not None:
            if timeout > 0:
                timeout -= .5
                continue

            # Timed out
            if filterDict is None:
                # Pretty pointless ;-)
                return []
            filteredDevices = getCurrentDevices(filterDict=filterDict)
            if len(filteredDevices) > 0:
                return filteredDevices[0].device
            return []


if __name__ == "__main__":
    detect()