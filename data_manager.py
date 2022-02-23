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

    # It might be easier to convert the inputs to dec. Preform math operations. Then convert back to different formats
    def convert_to_dec(self):
        inputs = self.inputs["inputs"]
        for input in inputs:
            if input["type"] == "hex":
                pass

    def xor(self, val1, val2):
        return val1 ^ val2

    def multiply(self, val1, val2):
        return val1 * val2

    def and_op(self, val1, val2):
        return val1 & val2

    def sub(self, val1, val2):
        return val1 - val2

    def div(self, val1, val2):
        return val1 / val2
