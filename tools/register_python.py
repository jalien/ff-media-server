__author__ = 'jalien'

#
# script to register Python 2.0 or later for use with win32all
# and other extensions that require Python registry settings
#
# written by Joakim Löw for Secret Labs AB / PythonWare
#
# source:
# http://www.pythonware.com/products/works/articles/regpy20.htm

import sys

from winreg import *

# tweak as necessary
version = sys.version[:3]
installpath = sys.prefix

regpath = "SOFTWARE\\Python\\Pythoncore\\%s\\" % version
installkey = "InstallPath"
pythonkey = "PythonPath"
pythonpath = "%s;%s\\Lib\\;%s\\DLLs" % (
    installpath, installpath, installpath
    )

def RegisterPy():
    try:
        reg = OpenKey(HKEY_LOCAL_MACHINE, regpath)
    except EnvironmentError:
        try:
            reg = CreateKey(HKEY_LOCAL_MACHINE, regpath)
            SetValue(reg, installkey, REG_SZ, installpath)
            SetValue(reg, pythonkey, REG_SZ, pythonpath)
            CloseKey(reg)
        except Exception as e:
            print("*** Unable to register!")
            print(e)
            return
        print("--- Python", version, "is now registered!")
        return
    if (QueryValue(reg, installkey) == installpath and
        QueryValue(reg, pythonkey) == pythonpath):
        CloseKey(reg)
        print("=== Python", version, "is already registered!")
        return
    else:
        print("registered key (install): %s" % QueryValue(reg, installkey))
        print("    expected: %s" % installpath)
        print("registered key (python) : %s" % QueryValue(reg, pythonkey))
        print("    expected: %s" % pythonpath)
    CloseKey(reg)
    print("*** Unable to register!")
    print("*** You probably have another Python installation!")

if __name__ == "__main__":
    RegisterPy()