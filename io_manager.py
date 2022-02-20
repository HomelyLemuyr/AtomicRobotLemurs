# Handle the input of numbers
import re

# Regular Expressions for inputs
HEX_REG_EX = "0x[0-9,A-F,a-f]+$"
BIN_REG_EX = "^[0-1]+$"
FP_REG_EX = "^[-+]?[0-9]+\.[0-9]+$"
DEC_REG_EX = "^[0-9]+$"

# Make this list into a dict like this:
"""
 {
    inputs: [
        "input1": {
            "type": "hex",
            "value": "0x19AC"
        },
        "input2": {
            "type": "hex",
            "value": "0xFFFF"
        }
    ]
}
"""

# create the input dict and set each inputs value in the dict
def get_inputs():
    nums = {"inputs": []}
    inputs = input("Please enter your digits: ")
    for i in inputs:
        if i != " ":
            nums.append(i)
    return nums

# take in the dict then set the type for each input
def classify_input(input, inputs):
    for input in inputs:
        if re.search(HEX_REG_EX, input) is True:
            # set inputx.type = hex
            pass
        elif re.search(BIN_REG_EX, input) is True:
            # set inputx.type = bin
            pass
        elif re.search(FP_REG_EX, input) is True:
            # self.input.type = float
            pass
        elif re.search(DEC_REG_EX, input) is True:
            # self.input.type = decimal
            pass
    return inputs
