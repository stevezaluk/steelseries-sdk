import os, sys
import usb.core

class Device(object):
    def __init__(self, product_name=None, product_id=None,
                device_type=None, resolution=None, oled_compatible=False):
        self.product_name = product_name
        self.product_id = product_id
        self.device_type = device_type
        self.oled_compatible = oled_compatible
        self.resolution = resolution

    def get_product_name(self):
        return self.product_name

    def get_product_id(self):
        return self.product_id

    def get_device_type(self):
        return self.device_type

    def get_resolution(self):
        return self.resolution

    def set_product_name(self, pn):
        self.product_name = pn

    def set_product_id(self, pid):
        self.product_id = pid

    def set_device_type(self, dt):
        self.device_type = dt

    def set_oled_compatible(self, oc):
        self.oled_compatible = oc

    def set_resolution(self, r):
        self.resolution = r

class DeviceTracker(object):
    def __init__(self):
        self.all_device_count = 0
        self.steelseries_device_count = 0

    @classmethod
    def discover_devices(self):
        device = usb.core.find(idVendor=0x1038, find_all=True)

        devices = []
        if device is None:
            return None
        else:
            for d in device:
                devices.append(d)

        return devices

    def init_device_objects(self):
        steelseries_devices = []
        devices = self.discover_devices()
        print('[DeviceTracker] Scanning for SteelSeries devices...')
        for d in devices:
            self.all_device_count = self.all_device_count + 1
            device = Device()

            if 'Rival 700' in d.product or 'Rival 710' in d.product:
                self.steelseries_device_count = self.steelseries_device_count + 1
                device.set_device_type('Mouse')
                device.set_resolution('128x36')
                device.set_oled_compatible(True)
                device.set_product_name(d.product)
                device.set_product_id(d.idProduct)
                steelseries_devices.append(device)
            elif 'Apex 7' in d.product or 'Apex 7 TKL' in d.product or 'Apex Pro' in d.product or 'Apex Pro TKL' in d.product:
                self.steelseries_device_count = self.steelseries_device_count + 1
                device.set_device_type('Keyboard')
                device.set_resolution('128x40')
                device.set_oled_compatible(True)
                device.set_product_name(d.product)
                device.set_product_id(d.idProduct)
                steelseries_devices.append(device)
            elif 'Arctis Pro' in d.product or 'Arctis Pro Wireless' in d.product:
                self.steelseries_device_count = self.steelseries_device_count + 1
                device.set_device_type('Keyboard')
                device.set_resolution('128x48')
                device.set_oled_compatible(True)
                device.set_product_name(d.product)
                device.set_product_id(d.idProduct)
                steelseries_devices.append(device)
            elif 'Rival 600' in d.product:
                self.steelseries_device_count = self.steelseries_device_count + 1
                device.set_device_type('Mouse')
                device.set_oled_compatible(False)
                device.set_product_name(d.product)
                device.set_product_id(d.idProduct)
                steelseries_devices.append(device)

        if len(steelseries_devices) == 0:
            print('[!] No SteelSeries devices found')
            sys.exit(0)

        return steelseries_devices

if __name__ == '__main__':
    d = DeviceTracker()
    d.init_device_objects()
