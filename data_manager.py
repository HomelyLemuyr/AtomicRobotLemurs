#
import io_manager as io_manager

class DataManager:
    def __init__(self):
        self.inputs = None

    def initialize(self):
        # Run the input manager
        self.inputs = io_manager.get_inputs()
        self.inputs = io_manager.classify_input(self.inputs)
        return True

    def check_input(self):
        for input in self.inputs:
            io_manager.classify_input(input)
