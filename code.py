import sys
import board
import supervisor
import os

import adafruit_ble
from adafruit_ble.advertising import Advertisement
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.standard.hid import HIDService
from adafruit_ble.services.standard.device_info import DeviceInfoService

try:
    # Use default HID descriptor
    hid = HIDService()
    device_info = DeviceInfoService(
        software_revision=adafruit_ble.__version__, manufacturer="Adafruit Industries"
    )
    advertisement = ProvideServicesAdvertisement(hid)
    advertisement.appearance = 961
    scan_response = Advertisement()
    ble = adafruit_ble.BLERadio()
    if ble.connected:
        for c in ble.connections:
            c.disconnect()
    print("advertising")
    ble.start_advertising(advertisement, scan_response)

    supervisor.set_rgb_status_brightness(8)
    from cpkf.cpkf import CPKFKeyboard
    import keyboard
    if "keymap.py" in os.listdir():
        import keymap
        kbd = CPKFKeyboard(keymap=keyboard.layouts(keymap.keymap), scan_method=keyboard.Scan.scan, ble=ble, hid=hid)
    else:
        import keyboard.default_keymap
        kbd = CPKFKeyboard(keymap=keyboard.layouts(keyboard.default_keymap.keymap), scan_method=keyboard.Scan.scan, ble=ble, hid=hid)

    kbd.start()

except Exception as err:
    try:
        kbd.release_all();
    except NameError as err2:
        print("Keyboard not Running.")
    else:
        pass
    
    try:
        with open("/log/error.txt", "w") as fp:
            sys.print_exception(err, fp)
    except OSError as err2:
        print("Can't write file.")
    else:
        raise

    raise(err)
