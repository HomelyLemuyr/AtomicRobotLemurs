# Handle the input of numbers
import re

# Regular Expressions for inputs
HEX_REG_EX = r"^0x[0-9a-fA-F]+$"
BIN_REG_EX = r"^[0-1]+$"
FP_REG_EX  = r"^[-+]?[0-9]+\.[0-9]+$"

# Make this list into a dict like this:
"""
 {
    inputs: [
        'input1': {
            'type': 'hex',
            'value': '0x19AC'
        },
        'input2': {
            'type': 'hex',
            'value': '0xFFFF'
        }
    ]
}
"""
input1_dict = {'value': '', 'type': ''}

# May have to make an empty one then push new dict per input
input_dict = { 'input1': { },
               'input2': { }}

# create the input dict and set each inputs value in the dict
def get_inputs():
    inputs = input("Please enter your digits: ")
    # We recieved a string. Need to split the string at the white space
    inputs = inputs.split()
    print(f"This the inputs::{inputs}")
    id = 0
    for value in inputs:
        print(value)
        type = classify_input(value)
        print(f"This is the type::[{type}]")
    print(input1_dict)
    return True

# take in the dict then set the type for each input
def classify_input(input):
    if re.fullmatch(HEX_REG_EX, input or "") is not None:
        return "hexidecimal"
    elif re.fullmatch(BIN_REG_EX, input or "") is not None:
        return "binary"
    elif re.fullmatch(FP_REG_EX, input) is not None:
        return "floating point"
    # elif re.search(DEC_REG_EX, input) is True:
    #     return "SEM"
    return None
