import sys
import random
import re
from binary_utils import get_binary_data
from byte_frequency import construct_frequency_table
from shannon import shannon_entropy

TESTING_DATA_FILE = "test.csv"
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

def get_random_fragment(binary_data):
    rand_frag_start = random.randint(0, len(binary_data)/2 - 1)
    rand_frag_length = random.randint(1, len(binary_data) - rand_frag_start)
    return binary_data[rand_frag_start:(rand_frag_start+rand_frag_length)]


if __name__ == "__main__":
    full_file = sys.argv[1]
    label = re.match('.*\.(.*)$', full_file).groups()[0]
    if label not in LABELS:
        sys.exit(0)
    class_label = LABELS.index(label)
    binary_file = get_binary_data(full_file)
    fragment = get_random_fragment(binary_file)
    frequency_table = construct_frequency_table(fragment)
    entropy = shannon_entropy(fragment)
    with open(TESTING_DATA_FILE, 'a') as training_file:
        line = ','.join([ str(x) for x in frequency_table])
        line += ',' + str(entropy)
        line += ',' + str(class_label)
        training_file.write(line + '\r\n')
    print("Wrote {} to {}".format(full_file, TESTING_DATA_FILE))
