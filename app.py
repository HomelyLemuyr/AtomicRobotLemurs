"""
Dev Environment:
    Machine:            MacBook Pro M1 Chip
    OS:                 macOS Monterey V12.1
    Text Editor:        Atom Text Editor
    Language:           Python
    Version:            3.8.9
    Run Environment:    Terminal

"""

import os
import time
from data_manager import DataManager

def main():
    data_manager = DataManager()
    if data_manager.initialize() is False:
        print("Failed to initialize project")
        os._exit(1)

    # while True:
    try:
        if data_manager.start() is False:
            print("Failed to start app")
            os._exit(2)
        time.sleep(1)
        print("Done")
    except KeyboardInterrupt as kb:
        print("\nUser Exit Intiated")
        os._exit(0)

if __name__ == '__main__':
    main()
