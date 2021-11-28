import os, sys, json, requests
import usb.core
import usb.util
from bs4 import BeautifulSoup
from colorama import Fore, Style

class Device(object):
    def __init__(self):
        self.vendor_id = 0x1038
        self.address = self.get_address()

    def get_address(self):
        with open('/Library/Application Support/SteelSeries Engine 3/coreProps.json', 'r') as file:
            _json = file.read()

        parser = json.loads(_json)

        return parser['address']

    def find_device(self):
        device = usb.core.find(idVendor=self.vendor_id, find_all=True)

        ret = []
        if device is None:
            print('No Steel Series Devices Connected')
            sys.exit(0)
        else:
            for d in device: # test this with only one steelseries device
                ret.append(d)

        return ret

    def info(self):
        devices = self.find_device()
        device_count = 0
        for d in devices:
            device_count = device_count + 1
            print('{g}==>{nc} Steel Series Device: #{i}'.format(i=device_count, g=Fore.GREEN, nc=Style.RESET_ALL))
            print('   Product: ', d.product)
            print('   Vendor ID: {}'.format(hex(self.vendor_id)))
            print('   Product ID: {}'.format(hex(d.idProduct)))
            print('   Version: {}\n'.format(hex(d.bcdDevice)))

def main():
    bind_address = 'http://127.0.0.1:65468/bind_game_event'
    event_address = 'http://127.0.0.1:65468/game_event'

    handler = {
      "game": "ADVENTURE",
      "event": "HEALTH",
      "handlers": [
        {
          "device-type": "screened",
          "zone": "one",
          "mode": "screen",
          "datas": [
            {
                "has-text": True,
                "suffix": "stuff",
                "icon-id":16
            }
          ]
        }
      ]
    }

    game = {
        "game":"ADVENTURE",
        "event":"HEALTH",
        "data": {
            "value": "Hello "
        }
    }

    print('Sending request to /bind_game_event')
    h = {"Content-Type": "application/json"}
    r = requests.post(bind_address, json=handler)
    print('Status Code: ', r.status_code)
    print('Response Headers: ', r.headers)
    print('JSON: ', r.json())
    print('\n Sending request to /game_event')
    r = requests.post(event_address, json=game)
    print('Status Code: ', r.status_code)
    print('Response Headers: ', r.headers)
    print('JSON: ', r.json())


def usage():
    print('')
    print(' commonsense : Interact with GameSense SDK easily')
    print(' Built on macOS   |   Written By: zbduid12')
    print('')
    print('     -i : Print info on connected devices')
    print('     -h : Print this page')
    print('     -v, --verbose : Increased verbosity')
    print('')
    print(' Devices:')
    print('')
    print('     -o, --oled : Device arg for the OLED screen')
    print('     -k, --keyboard : Device arg for the keyboard')
    print('     -m, --mouse : Device arg for the mouse')
    print('')
    print(' OLED Events: ')
    print('')
    print('     -t [text] : Send text to the screen')
    print('     -i [image] : Send an image to the screen')
    print('')
    print(' Keyboard & Mouse Events: ')
    print('')
    print('     -rgb [r] [g] [b] : Set the whole keyboard to a set r/g/b number')
    print('     -M [mode] : Set a visualization mode')
    print('     -r : Set a rate. Use this with -f and -rl')
    print('     -f, --frequency [int] : Set a frequency')
    print('     -rl, --repeat-limit : Set a repeat limit')
    # print('     -z, --zone [zone] : Specify a zone. Defaults will be used if empty')
    print('')
    print(' Custom Events: ')
    print('')
    print('     -c, --custom : Arg for a custom event')
    print('')
    print(' Debug & Misc: ')
    print('')
    print('     --bind-game-event [json] : Bind a game event')
    print('     --register-game-event [json] : Register a game event')
    print('     --go-game-event : Execute the binded game event')
    print('     --show-core-props : Show your coreProps.json file')
    print('     --save-event [path] : Save the event as JSON files')
    print('     --resolution [wxh] : Force a resolution for the OLED screen: 128x36, 128x40, 128x48, 128x52')
    print('')
    print(' Example Usage:')
    print('')
    print('     gamesense-api-toolkit -o 128x32 -t "Some text here"')
    print('     gamesense-api-toolkit -o 128x52 -i /path/to/image')
    print('     gamesense-api-toolkit -k -rgb 250 0 0')
    print('     gamesense-api-toolkit -k -rgb 250 0 0 -z ')

    # future features:
    # multiple text entries at once for oled screens
    # icon support for oled
    # choose your oled device
    # regenerate coreProps file
    # activate presets
    # progress bar support

if __name__ == '__main__':
    main()
