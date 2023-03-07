"""
Common data manipulation functions
"""

def data_16bit_to_binary_string(data: list) -> bytearray:
    """
    Converts a list of 16 bit data to high byte, low byte binary string

    Parameters
    ----------
    data: list
        List of data to convert to binary string

    Returns
    -------
    bytearray
        binary string of the converted 16 bit data
    """
    data_8bit = []
    for value in data:
        data_8bit.append(int(value/256))
        data_8bit.append(int(value%256))
    return bytearray(data_8bit)

def binary_string_to_16bit_data(byte_string: str) -> list:
    """
    Converts a string of high byte, low byte order values to 16 bit numbers

    Parameters
    ----------
    byte_string: str
        A string of high byte, low byte order values
    
    Returns
    -------
    list
        A list of the converted 16 bit values
    """
    converted = []
    for index in range(int(len(byte_string)/2)):
        converted.append((byte_string[2*index]*256) + byte_string[(2*index)+1])
    return converted
