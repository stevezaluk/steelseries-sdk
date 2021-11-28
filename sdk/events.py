import os, sys

sys.path.insert(1, '/Users/szaluk/lab/projects/steelseries')

from errors import BaseGameEventError

keyboard_zones = ['function-keys', 'main-keyboard', 'keypad', 'number-keys', 'macro-keys']
mouse_zones = ['wheel', 'logo', 'base']
resolutions = ['128x36', '128x40', '128x48', '128x52']

class BaseGameEvent(object):
    def __init__(self, game, event, value=None):
        self.game = game
        self.event = event
        self.value = value
        self.event_ticket = self.build_game_event()

    def set_game(self, g):
        self.game = game

    def get_game(self):
        return self.game

    def set_event(self, e):
        self.event = e

    def get_event(self):
        return self.event

    def set_value(self, v):
        self.value = v

    def get_value(self):
        return self.value

    def build_game_event(self):
        game = {
            "game":self.game,
            "event":self.event,
        }
        if self.value is None:
            return game
        else:
            game.update({"data":{"value":self.value}})
            return game

class IlluminationEvent(BaseGameEvent):
    def __init__(self):
        BaseGameEvent.__init__(self, 'gamesense-sdk', 'ILLUMINATION')
        self.red = '0'
        self.green = '0'
        self.blue = '0'
        self.mode = None
        self.rate = False
        self.frequency = 0
        self.repeat_limit = 0
        self.handler_ticket = self.build_event_handler()

    def build_event_handler(self): pass

class OLEDEvent(BaseGameEvent):
    def __init__(self):
        BaseGameEvent.__init__(self, 'gamesense-sdk', 'OLED')
        self.text = None
        self.image_path = None
        self.resolution = False
        self.handler_ticket = self.build_event_handler()

    def build_event_handler(self):
        handler = {
            "game":self.game,
            "event":self.event,
            "handlers": [
                {
                    "device-type": "screened",
                    "zone": "one",
                    "mode":"screen",
                    "datas": [
                        {
                            "has_text":True
                        }
                    ]
                }
            ]
        }
        if isinstance(self.resolution, str):
            handler['handlers'][0].update({"device-type": "screened-{}".format(self.resolution)})

        if isinstance(self.image_path, str):
            handler['handlers'][0]['datas'][0].update({"has-text":False})
            bitmap = image_to_bitmap(self.image_path)
            handler['handlers'][0]['datas'][0].update({"image-data":bitmap})

        if isinstance(self.text, str):
            self.set_value(self.text)

class CustomEvent(BaseGameEvent):
    def __init__(self):
        pass


if __name__ == '__main__':
    words = 'This is my sentence'
    print(words.split())
