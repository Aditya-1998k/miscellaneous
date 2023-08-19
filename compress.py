import zlib

def compress(data):
    """
    args: string data to be compressed
    return: compressed data
    """
    if not isinstance(data, str):
        data = str(data)

    compressed_data = zlib.compress(data.encode('utf-8'))

    return compressed_data


data_to_be_compressed ='Hello Wolrd'
print(compress(data_to_be_compressed))
