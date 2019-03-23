from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from cpkf.key_object import KeyObject

class VOL(KeyObject):
    consumer_control = ConsumerControl()
    
    def __init__(self, code):
        self.code = code
        
    def press(self, kbd, t):
        self.consumer_control.send(self.code)
        self.last_exec = t
        self.repeated = False
        
    def release(self, kbd, time):
        pass
        
    def tick(self, kbd, time):
        threshold = 0.1 if self.repeated else 0.5
        if time - self.last_exec > threshold:
            self.consumer_control.send(self.code)
            self.repeated = True
            self.last_exec = time

class VOLU(VOL):
    def __init__(self):
        super().__init__(ConsumerControlCode.VOLUME_INCREMENT)

class VOLD(VOL):
    def __init__(self):
        super().__init__(ConsumerControlCode.VOLUME_DECREMENT)


