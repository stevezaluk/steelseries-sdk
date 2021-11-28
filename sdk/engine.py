import os, sys, json
from events import BaseGameEvent
from device import DeviceTracker, Device

class Engine(object):
    def __init__(self):
        self.verbose = False
        self.save_event = False
        self.selected_device = None
        self.force_resolution = False

class EventHandler(DeviceTracker):
    """
        Engine - Binds/registers game events and activates the event
    """
    def __init__(self, event:BaseGameEvent, engine:Engine):
        DeviceTracker.__init__(self)
        self.engine = engine
        self.event = event
        self.core_props = '/Library/Application Support/SteelSeries Engine 3/coreProps.json'
        self.address = self.get_core_props()[0]
        self.encrypted_address = self.get_core_props()[1]
        self.endpoints = ['/bind_game_event', '/register_game_event', '/game_event', '/game']

    def init(self):
        print('[i] Address: ', self.address)
        print('[i] Encrypted Address: ', self.encrypted_address)

        for d in self.init_device_objects():
            print('==> Device Found!')
            print(' Name: ', d.product_name)
            print(' Device Type: ', d.device_type)
            print(' Product ID: ', d.product_id)
            print(' OLED Compatible: ', d.oled_compatible)
            if d.oled_compatible:
                print(' OLED Resolution: ', d.resolution)
            print()

    def get_core_props(self):
        if os.path.exists(self.core_props):
            ret = []

            with open(self.core_props, 'r') as file:
                _json = file.read()

            parser = json.loads(_json)

            ret.insert(0, parser['address'])
            ret.insert(1, parser['encrypted_address'])

            return ret
        else:
            print('[!] coreProps.json does not exist!')
            sys.exit(0)
