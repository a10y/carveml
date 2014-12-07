
def get_binary_data(filename):
    data = [];
    with open(filename, "rb") as f:
        byte = f.read(1)
        while byte:
            data.append(ord(byte))
            byte = f.read(1)
    return data
