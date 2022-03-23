from distutils.log import debug


debugLog = False

def printDebug(*s):
    if debugLog:
        print(s)