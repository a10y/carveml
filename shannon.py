#!/usr/bin/env python3
import sys
from binary_utils import get_binary_data
from byte_frequency import construct_frequency_table
import math
"""
Calculates the Shannon entropy (http://rosettacode.org/wiki/Entropy) of
a provided file
"""

def shannon_entropy(bytes):
    """
    performs the calculation
    """
    byte_frequency = construct_frequency_table(bytes)
    entropy = 0
    for i in range(len(byte_frequency)):
        if byte_frequency[i] != 0:
            entropy += -byte_frequency[i] * math.log(byte_frequency[i], 2)
    return entropy


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Must provide filename to calculate entropy for as argument")
        sys.exit(0)
    bytes = get_binary_data(sys.argv[1])
    entropy = shannon_entropy(bytes)
    print("File {} has Shannon entropy: {}".format(sys.argv[1], entropy))
