#!/usr/bin/env python3
import sys
from binary_utils import get_binary_data

def construct_frequency_table(raw_data):
    """
    Takes as input a raw string of binary data, and returns a
    256 element array, where the i-th entry of the array is the
    floating point proportion of bytes that take on value i.
    """
    frequencies = [0] * 256
    for i in range(len(raw_data)):
        frequencies[raw_data[i]] += 1
    for i in range(len(frequencies)):
        frequencies[i] /= float(len(raw_data))
    return frequencies


def print_histogram(arr):
    for i in range(len(arr)):
        line = "{0:03d}: ".format(i)
        exes = "X" * arr[i]
        print(line + exes)

def print_usage():
    print("Usage: {} filename".format(sys.argv[0]))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(0)
    print("Opening {}" .format(sys.argv[1]))
    byte_arr = get_binary_data(sys.argv[1])
    print("Constructing frequency table...")
    freq = construct_frequency_table(byte_arr)
    #print("Created frequency table:")
    #print_histogram(freq)
