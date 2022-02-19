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
        ret = val1 ^ val2
        return ret

    def multiply(self, val1, val2):
        mult = val1 * val2
        return mult
