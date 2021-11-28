import os, sys

class ArgumentParser(object):

    def __init__(self, args):
        self.args = args

    def go(self):
        for arg in self.args:
            if '-k' in arg:
                self
