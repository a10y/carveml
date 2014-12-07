import json
import os
import sys
import re
from binary_utils import get_binary_data
from byte_frequency import construct_frequency_table
from shannon import shannon_entropy

TRAINING_DATA_FILE = "train.csv"
LABELS = [ "csv",
        "dbase3",
        "doc",
        "eps,"
        "f",
        "gif",
        "gls",
        "gz",
        "hlp",
        "html",
        "java",
        "jpg",
        "kml",
        "kmz",
        "log",
        "pdf",
        "png",
        "ppt",
        "ps",
        "rtf",
        "swf",
        "text",
        "tmp",
        "troff",
        "txt",
        "unk",
        "xls",
        "xml" ]

if __name__ == "__main__":
    full_file = sys.argv[1]
    label = re.match('.*\.(.*)$', full_file).groups()[0]
    class_label = LABELS.index(label)
    binary_file = get_binary_data(full_file)
    frequency_table = construct_frequency_table(binary_file)
    entropy = shannon_entropy(binary_file)
    with open(TRAINING_DATA_FILE, 'a') as training_file:
        line = ','.join([ str(x) for x in frequency_table])
        line += ',' + str(entropy)
        line += ',' + str(class_label)
        training_file.write(line + '\r\n')
    print("Wrote {} to {}".format(full_file, TRAINING_DATA_FILE))
