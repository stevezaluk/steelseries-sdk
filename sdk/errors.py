import os, sys

class BaseGameEventError(Exception):
    pass

class KeyboardEventError(Exception):
    pass

class OLEDEventError(Exception):
    pass

class MouseEventError(Exception):
    pass

class IlluminationEventError(Exception):
    pass
