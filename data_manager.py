import io_manager as io_manager

class DataManager:
    def __init__(self):
        self.inputs = None
        self.op_values = []

    def initialize(self):
        # Run the input manager
        self.inputs = io_manager.get_inputs()
        return True

    def check_input(self):
        pass

    def start(self):
        print(self.inputs)
        for key in self.inputs:
            type = self.inputs[key]['type']
            value = self.inputs[key]['value']
            num = self.convert_to_dec(value, type)
            self.op_values.append(num)

        return True

    # It might be easier to convert the inputs to dec. Preform math operations. Then convert back to different formats
    def convert_to_dec(self, value, type):
        if type == "hexidecimal":
            return int(value, 16)
        elif type == "binary":
            return int(value, 2)
        elif type == "floating point":
            return value

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

    # recieve a decimal and convert it to the correct formata
    def convert_to_output(self, output):
        hex_ = hex(output)
        bin_ = bin(output).replace("0b", "")
