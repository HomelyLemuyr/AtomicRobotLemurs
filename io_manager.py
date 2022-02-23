# Handle the input of numbers
import re

# Regular Expressions for inputs
HEX_REG_EX = r"^0x[0-9a-fA-F]+$"
BIN_REG_EX = r"^[0-1]+$"
FP_REG_EX  = r"^[-+]?[0-9]+\.[0-9]+$"

# Mak one dict the main input holder. The other will be overwritten as we add new inputs
input_dict = {}
holding_dict = {}

# create the input dict and set each inputs value in the dict
def get_inputs():
    inputs = input("Please enter your digits: ")
    # We recieved a string. Need to split the string at the white space
    inputs = inputs.split()
    id = 0
    for value in inputs:
        type = classify_input(value)
        holding_dict[f"input{id}"] = {'type': f'{type}',
                                    'value': f'{value}'}
        input_dict.update(holding_dict)
        id +=1
    return input_dict

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
