import os
import time
from data_manager import DataManager

def main():
    manager = DataManager()
    if manager.initialize() is False:
        print("Failed to initialize project")
        os._exit(1)

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt as kb:
            print("\nUser Exit Intiated")
            os._exit(0)

if __name__ == '__main__':
    main()
