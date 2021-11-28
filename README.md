# steelseries-sdk
A broken SDK and toolchain that lets you interact with the steelseries REST API

# Update
Im pretty sure steelseries removed the REST API from there software. I havent looked too far into this tho, I could be wrong and the tool could just be broken.

# Also, Unfinished
Not completely unfinished there are somethings in here that work (or used to work)

Supported Devices:
  * Rival 600, 700, 710
  * Apex 7, Apex 7 TKL, Apex Pro
  * Arctis Pro, Arctis Pro Wireless

Tested Devices:
  * Rival 600
  * Apex 7 TKL

Usage:

  commonsense [device_type] [event_args] EVENT [modifiers]

Below are some common commands
  commonsense -o -t "Hello World" : Print Hello World to all OLED supported devices

  commonsense -o -t "Hello World" --resolution 128x48 --save-event ~/Desktop : Print Hell World to OLED's,
  force a 128x48 resolution, and save the event's JSON to your desktop

  commonsense -k -rgb 255 0 0 : Set the entire keyboard to a static red color
  commonsense -k -rgb 255 0 0 -m
