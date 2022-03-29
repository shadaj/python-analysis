from distutils.log import debug

showPlot = False

def isShowPlot():
    return showPlot

debugLog = False

def printDebug(*s):
    if debugLog:
        print(s)