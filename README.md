# detectty
Detect freshly plugged tty devices.

# Usage
1. Make sure your device is unplugged.
2. Call `./detectty.py`.
3. Plug in your device.
4. You device will show up:
```
Detected new device:
/dev/tty.xxxxxxxXXXXXXXXXX

Setting environment variable:
NEW_TTY_DEV='/dev/tty.xxxxxxxXXXXXXXXXX'
```
5. You can also use the freshly set `NEW_TTY_DEV` environment variable to reference your device.
