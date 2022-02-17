#
from io_manager import *

class DataManager:
    def __init__(self):
        self.inputs = None

    def initialize(self):
        # Run the input manager
        self.inputs = get_inputs()
        print(f"These are the inputs: {self.inputs}")
        return True
