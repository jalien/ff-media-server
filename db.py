__author__ = 'jalien'

import sys
import os
import constants

def db():
    # if restart wanted, return constants.RESTART_PROGRAM
    answer = input("restart? (y/n) ")
    if answer.strip() in "y Y yes Yes YES".split():
        return constants.RESTART_PROGRAM
    return


if __name__ == "__main__":
    print("program started.")
    retcode = db()
    if retcode == constants.RESTART_PROGRAM:
        print("restarting program.")
        python = sys.executable
        os.execl(python, python, * sys.argv)
