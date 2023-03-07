"""
Package for encoding/decoding data
"""
codec_library = {
    'base64_character3': {
        'base': 64,
        'characters': 3,
        'library':
            ['0','1','2','3','4','5','6','7','8','9',
            'a','b','c','d','e','f','g','h','i','j',
            'k','l','m','n','o','p','q','r','s','t',
            'u','v','w','x','y','z','A','B','C','D',
            'E','F','G','H','I','J','K','L','M','N',
            'O','P','Q','R','S','T','U','V','W','X',
            'Y','Z','!','@']
        }
    }

def encode(data: list, codec: str = "base64_character3"):
    """
    Encode data using codec

    Parameters
    ----------
    data: list [int]
        The data to encode
    codec: str = "base64_character3"
        The codec in the codec_library to use for encoding the data
    
    Returns
    -------
    str
        The encoded ascii data string
    """
    # Grab values from codec library
    base = codec_library[codec]['base']
    characters = codec_library[codec]['characters']
    library = codec_library[codec]['library']

    # Determine if any values are outside of codec ability
    max_possible_value = 0
    for numerator in range(characters):
        max_possible_value += (base-1)*(base**numerator)
    if max(data) > max_possible_value:
        raise Exception(
            "Max data value is above codec ability to encode.\n \
            max data value: {0}\n \
            max possible codec value: {1}".format(str(max(data)),str(max_possible_value))
            )

    # Convert data to appropriate base and ascii character
    encoded_data_string = ''
    for value in data:
        temp = []
        for power in range((characters-1), -1, -1):
            temp.append(value//(base**power))
            value -= temp[-1]*(base**power)
        for character in temp:
            encoded_data_string += library[character]
    return encoded_data_string

def decode(encoded_data: str, codec: str = "base64_character3"):
    """
    Decode data using codec

    Parameters
    ----------
    encoded_data: str
        The encoded ascii data string to decode
    codec: str = "base64_character3"
        The codec in the codec_library to use for decoding the data
    
    Returns
    -------
    list
        The decoded data
    """
    # Grab values from codem library
    base = codec_library[codec]['base']
    characters = codec_library[codec]['characters']
    library = codec_library[codec]['library']

    # Decode data from ascii character to value
    data = []
    num_values = len(encoded_data)//characters
    for value in range(num_values):
        temp = 0
        for character in range(characters):
            coef = library.index(encoded_data[(value*characters)+character])
            temp += coef * (base ** (characters - 1 - character))
        data.append(temp)
    return data
