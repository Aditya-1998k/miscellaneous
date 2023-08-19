import zlib

def decompress(data):
    """
    this method will return decompressed data
    """
    parsed_data = zlib.decompress(data).decode('utf-8')

    return parsed_data


data_to_be_decompress = b'x\x9c\xf3H\xcd\xc9\xc9W\x08\xcf\xcf)J\x01\x00\x18\x05\x04\x1d'
print(decompress(data_to_be_decompress))